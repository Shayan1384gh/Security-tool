<div align="center">

# 🦅 Security Tool

### Recon • OSINT • Web Security Toolkit

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Version](https://img.shields.io/badge/Version-2.0-green?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey?style=for-the-badge)

---

> A Python-based security framework designed for reconnaissance, OSINT gathering, web assessment, and educational security testing.

</div>

---

# 📦 Features

this tool combines multiple security modules into a single command-line framework.

```text
│
├
├── 📡 Scanning
|
│   ├── Port Scanner
│   ├── Directory Scanner
│   └── Subdomain Finder
│
├── 🌐 OSINT
│   ├── Username Finder
│   └── IP Lookup
│
├── 🕸️ Web
│   └── XSS Scanner
│
└── 📊 main.py
```

---

# 🛠 Included Modules

## 🔎 Recon Scanner

Collects basic information about a target website.

### Features

- Server Detection
- HTTP Headers Analysis
- Response Information
- Basic Fingerprinting

---

## 🚪 Port Scanner

Scans a target host for open ports.

### Features

- Fast TCP Port Scanning
- Open Port Detection
- Service Identification
- Progress Tracking

### Example Output

```text
Port 80   -> OPEN
Port 443  -> OPEN
Port 22   -> OPEN
```

---

## 📁 Directory Scanner

Attempts to discover hidden directories and files.

### Features

- Common Directory Enumeration
- Admin Panel Discovery
- Backup Folder Detection
- Configuration Path Discovery

### Example

```text
/admin/
/backup/
/dashboard/
/api/
```

---

## 🌐 Subdomain Finder

Performs DNS-based subdomain enumeration.

### Features

- DNS Resolution
- Common Subdomain Wordlist
- IP Address Discovery
- Fast Enumeration

### Example

```text
api.example.com
mail.example.com
cdn.example.com
dev.example.com
```

---

## 👤 Username Finder

Searches for usernames across multiple platforms.

### Supported Platforms

- GitHub
- GitLab
- Reddit
- Twitch
- Steam
- Kaggle
- Medium
- Codeforces
- HackerRank
- LeetCode
- Behance
- Pinterest
- Patreon
- And many more...

### Example

```text
Found on GitHub
Found on Reddit
Found on Steam
```

---

## 📍 IP Lookup

Retrieves information about a public IP address.

### Features

- Country
- City
- Region
- Timezone
- Latitude / Longitude
- Public / Private Detection

### Example

```text
IP Address : 8.8.8.8
Country    : United States
City       : Mountain View
Timezone   : America/Los_Angeles
```

---

## 🕸️ XSS Scanner

Performs basic reflected XSS testing.

### Features

- GET Parameter Testing
- POST Parameter Testing
- Header-Based Injection Testing
- Reflection Detection
- Context Analysis

### Tested Vectors

```text
GET Parameters
POST Parameters
HTTP Headers
```

---

# 🖥 Main Menu

```text
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                  🛡️ security tool                            ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫

 🔎 SCANNING

  1 ▸ Recon Scanner
  2 ▸ Port Scanner
  3 ▸ Directory Scanner
  4 ▸ Subdomain Finder

 🌐 OSINT

  5 ▸ Username Finder
  6 ▸ IP Lookup

 ⚔️ WEB

  7 ▸ XSS Scanner
  8 ▸ DDos Scanner

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  0 ▸ Exit

┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

---

# ⚙️ Installation

## 1️⃣ Install Python

Download and install Python:

🔗 https://www.python.org/downloads/

Verify installation:

```bash
python --version
```

or

```bash
python3 --version
```

---

## 2️⃣ Clone Project

---

## 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run Framework

```bash
python main.py
```

# ⚠️ Disclaimer

This project is intended for:

- Educational purposes
- Security research
- Authorized testing
- Learning Python security development

Do not use this framework against systems you do not own or have explicit permission to test.

The author is not responsible for misuse of this software.

---

# 👨‍💻 Author

### Security Team

📧 Contact: shayanghojoghi85@gmail.com

---

<div align="center">

# ⭐ Hack Responsibly • Learn Continuously • Stay Ethical ⭐

</div>

