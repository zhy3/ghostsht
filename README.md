# ghostsht
# GhostSheet Framework

**Nothing.**

---

## 🚀 Modules Overview

1. **Crawler / Botnet Logger**

   * Logs each bot’s OS info, IP, timestamp, and actions.
   * Sends data via `curl` or Python (`requests` or Sheets API).
   * Central Google Sheet provides a live log dashboard.

2. **Command & Control (C2) Simulator**

   * Bots poll the sheet for commands (e.g., `echo`, `dir`, `netstat`).
   * Executes commands locally and posts results back to the sheet.
   * Uses Google Apps Script Web App + cron/task scheduler or Python loops.

3. **Basic Recon Scanner**

   * Performs domain WHOIS, IP geolocation, and optional Shodan queries.
   * Logs target metadata (IP, ASN, ISP, country) to the sheet.

4. **Payload Rotator / Distributor**

   * Sheet holds payload URLs, hashes, and execution rules (OS match, rotate per bot).
   * Clients poll sheet, verify hashes, download, and run safe/test scripts.

---

## ⚙️ Prerequisites

* Google account with access to Google Sheets and Apps Script.
* Python 3.x (with `gspread`, `requests`) or Bash (with `curl`).
* Optional: Shodan API key for advanced recon.

---

## 🛠️ Setup & Usage

1. **Clone Repo**

   ```bash
   git clone https://github.com/zhy3/ghostsht.git
   cd GhostSheet-Framework
   ```

2. **Configure Google Sheet**

   * Create a new sheet with separate tabs for logs, commands, recon, and payloads.
   * Deploy Apps Script Web App for read/write access.

3. **Install Dependencies**

   ```bash
   pip install gspread requests
   ```

4. **Run Modules**

   * **Logger**: `python crawler.py --sheet-id <ID>`
   * **C2**: `python c2.py --sheet-id <ID> --interval 60`
   * **Recon**: `python recon.py --sheet-id <ID> --targets targets.txt`
   * **Payload**: `python payload_rotator.py --sheet-id <ID>`

---

## 📖 Notes

* Intended for lab/testing only. Use safe/test payloads.
* Ensure proper credentials and OAuth scopes for Sheets API.
* Customize polling intervals and command sets as needed.
