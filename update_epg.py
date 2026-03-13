import os
import gzip
import xml.etree.ElementTree as ET
import requests

# Settings
NAME = "light"
SAVE_AS_GZ = True

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

def fetch_and_parse(url):
    try:
        print(f"Fetching: {url.split('/')[-1]}")
        response = requests.get(url, timeout=60)
        if response.status_code != 200:
            return None
        content = response.content
        if url.endswith('.gz'):
            content = gzip.decompress(content)
        return ET.fromstring(content)
    except Exception as e:
        print(f"  ! Error: {e}")
        return None

def main():
    master_root = ET.Element('tv', {"generator-info-name": "BuddyChewChew-Light-Merger"})

    for url in URLS:
        epg_data = fetch_and_parse(url)
        if epg_data is None: continue

        for channel in epg_data.findall('channel'):
            master_root.append(channel)

        for prog in epg_data.findall('programme'):
            title_node = prog.find('title')
            if title_node is not None and title_node.text:
                if title_node.text in ['NHL Hockey', 'Live: NFL Football']:
                    subtitle = prog.find('sub-title')
                    if subtitle is not None and subtitle.text:
                        title_node.text = f"{title_node.text} {subtitle.text}"
            master_root.append(prog)

    tree = ET.ElementTree(master_root)
    tree.write(OUTPUT_FILE, encoding='utf-8', xml_declaration=True)

    if SAVE_AS_GZ:
        with gzip.open(OUTPUT_FILE_GZ, 'wb') as f:
            tree.write(f, encoding='utf-8', xml_declaration=True)
    print("Process Complete.")

if __name__ == "__main__":
    main()
