# Simple Polymorphic Ransomware

This project is an example of a simple polymorphic ransomware script written in Python. **Note: This code is for educational and research purposes only.** Using it for any malicious activity is illegal and unethical. Please use this script responsibly to understand polymorphic encryption and study ransomware behavior in a safe environment.

## Overview

This script demonstrates a basic form of polymorphic ransomware using the `cryptography` package for file encryption and decryption. The main functionality involves:
- Encrypting files in the current directory (except specified exceptions).
- Saving the encryption key to a file (`thekey.key`).
- Self-modifying and regenerating its encryption key and token to achieve a polymorphic effect, where the code changes its internal encryption variables upon each execution.

### Important Warning

**These scripts are unstable and can encrypt files on your system, potentially leading to data loss.** It is recommended to run it in a secure, virtual environment where no real data is stored.

## Features

- **File Encryption**: Encrypts all files in the directory, excluding itself and the generated key file.
- **Self-Modification**: The script changes its encryption key and token on each run, demonstrating a basic form of polymorphism.
- **Hash Calculation**: Calculates a SHA-1 hash of the file for integrity verification.

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/eagle-plusplus/simple-polymorphic-ransomware.git
   cd simple-polymorphic-ransomware
    ```
2. **Ensure you have Python 3 installed, then install required packages**:
    ```bash
    pip install cryptography
    ```
