import os
import gzip
import re
import xml.etree.ElementTree as ET
import requests

# Settings
NAME = "light"
SAVE_AS_GZ = True
# Get URL from GitHub Secret (falls back to None if not set)
M3U_URL = os.getenv("M3U_URL")

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "epgs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

OUTPUT_FILE = os.path.join(OUTPUT_DIR, f"{NAME}-epg.xml")
OUTPUT_FILE_GZ = OUTPUT_FILE + '.gz'

URLS = [
    'https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz',
    'https://epgshare01.online/epgshare01/epg_ripper_US_LOCALS1.xml.gz',
    'https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz',
    'https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz',
    'https://epgshare01.online/epgshare01/epg_ripper_DUMMY_CHANNELS.xml.gz',
    'https://raw.githubusercontent.com/matthuisman/i.mjh.nz/refs/heads/master/PlutoTV/all.xml'
]

def get_tvg_ids_from_remote_m3u():
    """Downloads M3U from GitFlic and extracts tvg-id values."""
    tvg_ids = set()
    if not M3U_URL:
        print("No M3U_URL provided. Processing full EPG instead.")
        return None

    print(f"Downloading M3U from GitFlic...")
    try:
        response = requests.get(M3U_URL, timeout=30)
        if response.status_code != 200:
            print(f"Failed to download M3U: {response.status_code}")
            return None
        
        # Extract tvg-id="value"
        pattern = re.compile(r'tvg-id="([^"]+)"')
        matches = pattern.findall(response.text)
        for val in matches:
            tvg_ids.add(val)
            
        print(f"Successfully mapped {len(tvg_ids)} channels from your .ru playlist.")
        return tvg_ids
    except Exception as e:
        print(f"Error fetching M3U: {e}")
        return None

def fetch_and_parse(url):
    try:
        print(f"Fetching EPG: {url.split('/')[-1]}")
        response = requests.get(url, timeout=60)
        if response.status_code != 200: return None
        content = response.content
        if url.endswith('.gz'):
            content = gzip.decompress(content)
        return ET.fromstring(content)
    except Exception as e:
        print(f"  ! Error: {e}")
        return None

def main():
    valid_ids = get_tvg_ids_from_remote_m3u()
    master_root = ET.Element('tv', {"generator-info-name": "BuddyChewChew-Dynamic-Filter"})

    for url in URLS:
        epg_data = fetch_and_parse(url)
        if epg_data is None: continue

        for channel in epg_data.findall('channel'):
            if valid_ids is None or channel.get('id') in valid_ids:
                master_root.append(channel)

        for prog in epg_data.findall('programme'):
            if valid_ids is None or prog.get('channel') in valid_ids:
                title = prog.find('title')
                if title is not None and title.text in ['NHL Hockey', 'Live: NFL Football']:
                    sub = prog.find('sub-title')
                    if sub is not None and sub.text:
                        title.text = f"{title.text} {sub.text}"
                master_root.append(prog)

    tree = ET.ElementTree(master_root)
    tree.write(OUTPUT_FILE, encoding='utf-8', xml_declaration=True)

    if SAVE_AS_GZ:
        with gzip.open(OUTPUT_FILE_GZ, 'wb') as f:
            tree.write(f, encoding='utf-8', xml_declaration=True)
    print("M3U-Filtered EPG generation complete.")

if __name__ == "__main__":
    main()
