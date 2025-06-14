# CerberusObfuscator-Deobfuscator

A fully automatic deobfuscator for Python scripts obfuscated using [CerberusObfuscator](https://github.com/gvoze32/CerberusObfuscator).

> ✅ Supports multi-layer techniques: hex → base64 → zlib → marshal → XOR decryption.

---

## ⚠️ Legal Disclaimer

This tool is intended **solely for educational and ethical research purposes**.  
Do **not** use it to analyze or reverse-engineer software without **explicit permission** from the rightful owner.

> 🛑 The author does **not condone** the use of this tool for malicious, unauthorized, or illegal activity.  
By using this tool, **you accept full responsibility** for complying with all applicable laws and terms of service.

---

## 🔧 Features

- Detects and extracts embedded Cerberus payloads
- Auto-decrypts: `hex → base64 → zlib → marshal → XOR`
- Outputs clean, readable Python source code
- Drag & drop support

---

## 🚀 How to Use

1. Save the script below as `cerberus_deobfuscator.py`.
2. Drag and drop any `.py` file obfuscated with Cerberus onto the script.
3. The deobfuscated source will be saved as:

