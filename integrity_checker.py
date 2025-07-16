import hashlib
import os
import json

HASH_DB = "hash_database.json"
WATCH_DIR = "files_to_monitor"

def calculate_sha256(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def scan_directory(folder):
    hashes = {}
    for root, _, files in os.walk(folder):
        for filename in files:
            full_path = os.path.join(root, filename)
            relative_path = os.path.relpath(full_path, folder)
            hashes[relative_path] = calculate_sha256(full_path)
    return hashes

def load_hash_database():
    if os.path.exists(HASH_DB):
        with open(HASH_DB, "r") as f:
            return json.load(f)
    return {}

def save_hash_database(hashes):
    with open(HASH_DB, "w") as f:
        json.dump(hashes, f, indent=4)

def check_integrity():
    old_hashes = load_hash_database()
    new_hashes = scan_directory(WATCH_DIR)

    added = []
    modified = []
    deleted = []

    for file in new_hashes:
        if file not in old_hashes:
            added.append(file)
        elif new_hashes[file] != old_hashes[file]:
            modified.append(file)

    for file in old_hashes:
        if file not in new_hashes:
            deleted.append(file)

    print("🔍 File Integrity Report:\n")
    if added:
        print("🆕 Added Files:")
        for f in added:
            print(f"  + {f}")
    if modified:
        print("✏️ Modified Files:")
        for f in modified:
            print(f"  ~ {f}")
    if deleted:
        print("❌ Deleted Files:")
        for f in deleted:
            print(f"  - {f}")
    if not (added or modified or deleted):
        print("✅ No changes detected.")

    save_hash_database(new_hashes)

def main():
    print("=== File Integrity Checker ===")
    print("1. Save Current State")
    print("2. Check File Changes")
    choice = input("Enter option (1 or 2): ")

    if choice == "1":
        hashes = scan_directory(WATCH_DIR)
        save_hash_database(hashes)
        print("✅ File state saved.")
    elif choice == "2":
        check_integrity()
    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
