# 🔍 File Integrity Checker



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

## Output

<img width="1487" height="980" alt="File integrity" src="https://github.com/user-attachments/assets/d170aa25-b890-409e-8e25-69a145a72640" />
