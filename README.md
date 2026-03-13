# 📺 EPG Light: Smart EPG Harvester

**EPG Light** is a streamlined, automated tool that creates a custom TV guide (EPG) specifically for your unique playlist. Instead of downloading thousands of channels you don't own, this script "looks" at your playlist and only grabs the data you actually need.

## 🌟 Why use this?
* **Tiny File Size:** It generates a compressed `.gz` file to stay under GitHub's 100MB limit and load faster on your devices.
* **Smart Filtering:** Uses your own M3U playlist as a map so your TV guide is never cluttered with "No Information" channels.
* **Fully Automated:** Updates itself every 6 hours—set it and forget it.
* **Sports Enhancement:** Automatically merges sub-titles for NHL and NFL games (e.g., "NHL Hockey: Rangers vs Capitals") for a better look in TiviMate.

---

## 🛠️ How to Set This Up

You don't need to be a programmer to host this yourself. Follow these steps to get your own automated EPG server running for free.

### 1. Prepare your Repository
* Create a new repository on GitHub (Public or Private).
* Upload the `update_epg.py` file to the main folder.

### 2. Add your Secret Playlist Link
To keep your playlist URL private, we use GitHub "Secrets":
1.  In your GitHub repo, go to **Settings** > **Secrets and variables** > **Actions**.
2.  Click **New repository secret**.
3.  **Name:** `M3U_URL`
4.  **Value:** Paste the raw link to your `.m3u` or `.m3u8` file (e.g., your GitFlic or Bitbucket link).

### 3. Enable the Automation
1.  Go to **Settings** > **Actions** > **General**.
2.  Scroll to **Workflow permissions** and select **Read and write permissions**.
3.  Click **Save**.
4.  Upload the `.github/workflows/update.yml` file to your repository.

### 4. Run it for the first time
1.  Go to the **Actions** tab at the top of your GitHub page.
2.  Select **Update Light EPG** from the sidebar.
3.  Click the **Run workflow** dropdown and hit the button.
4.  Once the green checkmark appears, a new folder named `epgs` will appear in your repo containing your fresh TV guide!

---

## 🔗 How to use it in your IPTV Player
In **TiviMate**, **OTT Navigator**, or any IPTV player, add a new EPG source using the "Raw" link to your compressed file. It will look like this:

`https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO_NAME/main/epgs/light-epg.xml.gz`

---

## ⚠️ Important Limits & Safety
* **100MB Safety Stop:** GitHub has a strict 100MB limit per file. This script is hard-coded to **stop** if it cannot find your M3U filter. This prevents the script from accidentally pulling 400MB of data and breaking your repository.
* **GZ Only:** The script only saves the `.gz` version to save space. Most modern players (TiviMate, Sparkle, etc.) handle this perfectly.
* **Privacy:** Because you used a GitHub Secret, your playlist URL is never visible to the public.
