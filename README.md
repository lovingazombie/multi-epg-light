# 📺 EPG Light: Smart EPG Harvester

**EPG Light** is a streamlined, automated tool that creates a custom TV guide (EPG) specifically for your unique playlist. Instead of downloading thousands of channels you don't own, this script "looks" at your playlist and only grabs the data you actually need.

## 🌟 Why use this?
* **Tiny File Size:** Generates a compressed `.gz` file to stay under GitHub's 100MB limit.
* **Smart Filtering:** Uses your own M3U playlist as a map so your guide is never cluttered.
* **Fully Automated:** Updates itself every 6 hours.
* **Sports Enhancement:** Merges sub-titles for NHL and NFL games for a better look in TiviMate.

---

## 🛠️ How to Set This Up

### ⚠️ IMPORTANT: Do NOT "Fork" this Repo
If you **Fork** this repo, you will inherit the original settings. Instead, **Clone** it or download the files manually and upload them to your own **New** repository. This ensures your setup is clean and private.

### 1. Prepare your Repository
* Create a new repository on GitHub (Public or Private).
* Upload `update_epg.py` and the `.github` folder to your repo.

### 2. Add your Secret Playlist Link
1.  In your GitHub repo, go to **Settings** > **Secrets and variables** > **Actions**.
2.  Click **New repository secret**.
3.  **Name:** `M3U_URL`
4.  **Value:** Paste the raw link to your `.m3u` or `.m3u8` file.

### 3. Enable the Automation
1.  Go to **Settings** > **Actions** > **General**.
2.  Scroll to **Workflow permissions** and select **Read and write permissions**.
3.  Save your changes.

---

## ⚙️ Customizing your EPG Sources
Not every playlist uses the same channel IDs. If your guide is empty, you can edit the sources inside `update_epg.py`. 

Find this block at the top of the script:

```python
URLS = [
    '[https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz](https://epgshare01.online/epgshare01/epg_ripper_US2.xml.gz)',
    '[https://epgshare01.online/epgshare01/epg_ripper_US_LOCALS1.xml.gz](https://epgshare01.online/epgshare01/epg_ripper_US_LOCALS1.xml.gz)',
    '[https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz](https://epgshare01.online/epgshare01/epg_ripper_CA2.xml.gz)',
    '[https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz](https://epgshare01.online/epgshare01/epg_ripper_UK1.xml.gz)',
    '[https://epgshare01.online/epgshare01/epg_ripper_DUMMY_CHANNELS.xml.gz](https://epgshare01.online/epgshare01/epg_ripper_DUMMY_CHANNELS.xml.gz)',
    '[https://raw.githubusercontent.com/matthuisman/i.mjh.nz/refs/heads/master/PlutoTV/all.xml](https://raw.githubusercontent.com/matthuisman/i.mjh.nz/refs/heads/master/PlutoTV/all.xml)'
]
