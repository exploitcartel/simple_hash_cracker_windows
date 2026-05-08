<div align="center">

```
 ██████╗██████╗  █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗     
██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝     
██║     ██████╔╝███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗    
██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║    
╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝    
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝    
                                                                    
███████╗████████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗          
██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║          
███████╗   ██║   ███████║   ██║   ██║██║   ██║██╔██╗ ██║          
╚════██║   ██║   ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║          
███████║   ██║   ██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║          
╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝          
```

# 🔐 Cracking Station — Hash Cracker

**© Edison Plaku — EXPLOITCARTEL**

[![Release](https://img.shields.io/badge/Release-v1.0-red?style=for-the-badge&logo=github)](/)
[![Platform](https://img.shields.io/badge/Platform-Windows%2064bit-0078D6?style=for-the-badge&logo=windows)](/)
[![NoInstall](https://img.shields.io/badge/Installation-Not%20Required-22c55e?style=for-the-badge&logo=checkmarx)](/)
[![Python](https://img.shields.io/badge/Built%20with-Python%203-3776AB?style=for-the-badge&logo=python)](/)

<br>

> **Download. Double-click. Crack.**  
> No Python. No pip. No setup.

<br>

---

</div>

## ⚡ Quick Start

```
1. Download cracking_station.exe
2. Double-click
3. Paste hash → Load wordlist → Click RUN
4. Results appear instantly
```

**That's it.** No installation required.

---

## 📦 Download

| File | Platform |
|------|----------|
| `cracking_station.exe` | Windows 10/11 x64 |
| `cracking_station.py` | Any OS with Python 3 |

> ⬇️ **[Download Latest Release](../../releases/latest)**

---

## 🚀 What It Does

```
You provide:  5f4dcc3b5aa765d61d8327deb882cf99
              │
              ├── 🔍  Auto-detects hash type (MD5, SHA-1, SHA-256...)
              ├── 📂  Loads any .txt wordlist
              ├── ✍️   Accepts manual password input
              ├── ⚙️   Case-sensitive / trim / stop-on-first options
              ├── ⚡  Multi-hash cracking in one run
              └── 📊  Live results table with time elapsed
```

---

## ✨ Features (Built-in)

### 🔍 Hash Detection
- Auto-identifies hash type by length
- Confidence score per detection
- Supports MD5, SHA-1, SHA-224, SHA-256, SHA-384, SHA-512

### 💥 Cracking Engine
- Dictionary attack with any `.txt` wordlist
- Manual word input (no file needed)
- Auto mode — tries all algorithms automatically
- Multi-hash support — crack many hashes at once

### ⚙️ Options
- Case-sensitive matching toggle
- Whitespace auto-trim
- Stop on first match (speed mode)

### 📊 Results
- Live table — hash, cracked password, algorithm, time
- Color-coded log output
- Millisecond precision timing

---

## 🖼️ Interface

```
┌─────────────────────────────────────────────────────────────┐
│  🔐  CRACKING STATION  v1.0  © Edison Plaku                 │
├───────────────────────────┬─────────────────────────────────┤
│  Hash Input               │  Rezultatet                     │
│  [___________________]    │  # │ Hash │ Password │ Algo │ ms│
│  [___________________]    │  1 │ 5f4d │ password │ MD5  │ 2 │
│                           │  2 │ ...  │ ...      │ ...  │   │
│  Detected: MD5 • 90%      │                                 │
│  [Identify] [Auto ▼]      │                                 │
│                           │                                 │
│  Wordlist: rockyou.txt    │                                 │
│  [Ngarko .txt]            │                                 │
│                           │                                 │
│  [✓] Trim  [ ] Case       │                                 │
│  [ ] Stop on first        │                                 │
│                           │                                 │
│  [  RUN  ]  [ Clear ]     │                                 │
│  ● Ready                  │                                 │
│  [MATCH] 5f4d → password  │                                 │
└───────────────────────────┴─────────────────────────────────┘
```

---

## 🔐 Supported Algorithms

| Algorithm | Hash Length | Example |
|-----------|-------------|---------|
| MD5 | 32 chars | `5f4dcc3b5aa765d61d8327deb882cf99` |
| SHA-1 | 40 chars | `5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8` |
| SHA-224 | 56 chars | `d9014c4624844aa5bac314773d6b689ad467fa4e1d1a50a1b8a99d5a` |
| SHA-256 | 64 chars | `5e884898da28047151d0e56f8dc629277...` |
| SHA-384 | 96 chars | `a8b64babd0aca91a59bdbb7761b421d4f2bb38280d3a75...` |
| SHA-512 | 128 chars | `b109f3bbbc244eb82441917ed06d618b9008dd09b3befa...` |

---

## 🖥️ Run from Source

```bash
# Clone the repo
git clone https://github.com/exploitcartel/simple_hash_cracker_windows.git
cd simple_hash_cracker_windows

# Run directly — no installs needed
python cracking_station.py
```

> Requires **Python 3.x** only. Zero external dependencies.

---

## ⚠️ Legal Disclaimer

```
EDUCATIONAL USE ONLY

✓ Only test hashes you OWN or have EXPLICIT PERMISSION to test
✗ Unauthorized use against third-party systems is ILLEGAL
✗ Author assumes NO LIABILITY for misuse
```

---

## 🔗 Source Code

> Full source code available in this repository.  
> Executable release included for Windows users — no setup required.

---

<div align="center">

**© Edison Plaku 2026 — EXPLOITCARTEL**

*Security Research & Education*

[![GitHub](https://img.shields.io/badge/GitHub-exploitcartel-181717?style=for-the-badge&logo=github)](https://github.com/exploitcartel)

<br>

*Cracking Station v1.0 — Educational Use Only*

</div>
