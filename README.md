# 🔍 File Integrity Checker

COMPANY: CODTECH IT SOLUTION

NAME: MOHAMED ABDULLAH R

INTERN ID: CT04DH426

DOMAIN: CYBER SECURITY & ETHICAL HACKING

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

This tool monitors file changes by calculating and comparing SHA-256 hashes.

## 📁 Folder Structure

```
file_integrity_checker/
├── integrity_checker.py
├── hash_database.json (auto-created)
├── files_to_monitor/
```

## 🚀 How to Use

1. Add files to `files_to_monitor/`.
2. Run the script:
   ```bash
   python integrity_checker.py
   ```
3. Select:
   - `1` to save the current file state.
   - `2` to check for changes later.

## ✅ Features

- Detects:
  - 🆕 Added files
  - ✏️ Modified files
  - ❌ Deleted files
- Uses `hashlib` and `json` (no external dependencies)

## ⚠️ Note

This tool is for **local use only**. Do not use on sensitive or remote filesystems.
