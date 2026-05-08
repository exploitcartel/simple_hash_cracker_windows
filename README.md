# 🔐 Cracking Station

> A lightweight, single-file Python GUI hash cracker — built for educational and lab use.

**Author:** Edison Plaku  
**Language:** Python 3.x  
**Dependencies:** None (standard library only)

---

## 📸 Preview

![Cracking Station GUI](preview.png)

> *Dark-themed GUI with hash input, wordlist loader, and real-time results table.*

---

## ✨ Features

- 🔍 **Automatic hash detection** — identifies MD5, SHA-1, SHA-224, SHA-256, SHA-384, SHA-512 by length and confidence score
- 📂 **Wordlist support** — load any `.txt` wordlist file or type passwords manually
- ⚙️ **Cracking options:**
  - Case-sensitive / case-insensitive matching
  - Auto whitespace trimming
  - Stop on first match
- 📊 **Live results table** — shows hash, cracked password, algorithm used, and time elapsed
- 🖥️ **No external libraries** — runs on any machine with Python 3

---

## 🚀 Getting Started

### Option 1 — Run from source (Python)

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/cracking-station.git
cd cracking-station

# Run directly
python cracking_station.py
```

> Requires **Python 3.x**. No pip installs needed.

---

### Option 2 — Run the prebuilt executable

A standalone `.exe` is included for Windows users (no Python required).

```
cracking_station.exe
```

> ⚠️ Windows may show a SmartScreen warning for unsigned executables — click **"More info" → "Run anyway"** to proceed. The file is clean; you can verify by scanning it on [VirusTotal](https://www.virustotal.com).

---

## 🛠️ How to Use

1. **Paste** one or more hashes into the *Hash input* box (one per line)
2. **Load a wordlist** (`.txt` file) or type candidate passwords manually
3. *(Optional)* Click **"Identify hash type"** to auto-detect the algorithm
4. Choose algorithm from the dropdown or leave it on **Auto**
5. Click **Run** — results appear in the table on the right

---

## 🔐 Supported Hash Algorithms

| Algorithm | Hash Length |
|-----------|------------|
| MD5       | 32 chars   |
| SHA-1     | 40 chars   |
| SHA-224   | 56 chars   |
| SHA-256   | 64 chars   |
| SHA-384   | 96 chars   |
| SHA-512   | 128 chars  |

---

## 📁 Project Structure

```
cracking-station/
├── cracking_station.py     # Main application (source code)
├── cracking_station.exe    # Prebuilt Windows executable
├── README.md               # This file
└── wordlists/              # (Optional) Place your .txt wordlists here
```

---

## ⚠️ Disclaimer

This tool is intended **strictly for educational purposes** and authorized security lab environments.  
**Do not use it against systems or accounts you do not own or have explicit permission to test.**  
The author is not responsible for any misuse of this software.

---

## 📜 License

© Edison Plaku — All rights reserved.  
Redistribution or commercial use without permission is prohibited.
