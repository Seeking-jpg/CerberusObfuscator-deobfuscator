import base64
import binascii
import marshal
import zlib
import os
import re
import sys

def cerberus_deobfuscate(payload: str):
    try:
        hex_decoded = binascii.unhexlify(payload)
        b64_decoded = base64.b64decode(hex_decoded)
        decompressed = zlib.decompress(b64_decoded)
        marshaled = marshal.loads(decompressed)

        xor_key = bytes.fromhex("65d5fc5324d4b36eb1e0a9f77ffe14d6caf2b8ec2eb9e7c61728339b188d3afe")
        key_expanded = (xor_key * ((len(marshaled) // len(xor_key)) + 1))[:len(marshaled)]
        decrypted_bytes = bytes([b ^ k for b, k in zip(marshaled, key_expanded)])

        return decrypted_bytes.decode('utf-8')

    except Exception as e:
        return f"[!] Deobfuscation failed: {e}"

def extract_payload_from_file(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    match = re.search(r'payload\s*=\s*["\']([a-fA-F0-9]+)["\']', content)
    if match:
        return match.group(1)
    else:
        print("[!] No payload string found in the file.")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Drag a file onto this script or run: python cerberus_deobfuscator.py <file>")
        return

    input_path = sys.argv[1]
    if not os.path.isfile(input_path):
        print(f"[!] File not found: {input_path}")
        return

    filename = os.path.basename(input_path)
    name_no_ext = os.path.splitext(filename)[0]
    output_file = f"deobfuscated_{name_no_ext}.py"

    payload = extract_payload_from_file(input_path)
    result = cerberus_deobfuscate(payload)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"[+] Deobfuscation complete! Saved to: {output_file}")

if __name__ == "__main__":
    main()
