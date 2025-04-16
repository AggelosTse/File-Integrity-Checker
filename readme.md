# File Integrity Checker 🔐

This Python project allows you to generate and verify the **hash value of a file**, ensuring the file has not been tampered with or corrupted. It's a simple tool to maintain file integrity using cryptographic hash functions like **MD5**, **SHA-256** and more.

## 🚀 Features

- Generate hash value of any file.
- Verify file integrity by comparing the current hash with an original.
- Menu-driven terminal interface.

## 📦 Requirements

- **Python 3.12.3 or higher**
- No external dependencies (uses Python's built-in `hashlib` module)

## 🛠️ How It Works

1. **Generate Hash:**
   - Run the script and choose "Generate Hash" from the menu.
   - Select a file and the hashing algorithm (e.g., MD5, SHA-256).
   - The script displays the hash.

2. **Verify Integrity:**
   - Select "Verify File" from the menu.
   - Provide the file and the original hash value.
   - The script compares both.
     - ✅ If they match: The file is **pure** (unaltered).
     - ❌ If they don't: The file has been **modified or corrupted**.

## 📄 Usage

```bash
# To run the script:
python3 main.py
