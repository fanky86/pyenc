# -*- coding: utf-8 -*-
import os
import sys
import time
import base64
import marshal
import zlib
from rich.console import Console

# Warna terminal
P2 = '\033[1;92m'
H2 = '\033[1;96m'
K2 = '\033[1;93m'
reset = '\033[0m'

console = Console()

# Fungsi untuk teks dengan animasi
def delay_print(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Membersihkan terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk memilih lokasi output
def choose_output_path(default_path):
    console.print(f"{H2}Default output path: {P2}{default_path}{reset}")
    custom_path = input(f"{H2}Enter custom output path or press Enter to use default: ").strip()
    if not custom_path:
        custom_path = default_path
    try:
        # Memastikan folder output ada
        os.makedirs(os.path.dirname(custom_path), exist_ok=True)
    except Exception as e:
        console.print(f"{H2}Error creating directory: {e}{reset}")
    return custom_path

# Fungsi Enkripsi Base16
def encrypt_base16(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        encrypted = base64.b16encode(content.encode()).decode()
        default_output = f"{os.path.splitext(file_path)[0]}_enc_base16.py"
        output_path = choose_output_path(default_output)
        with open(output_path, 'w') as f:
            f.write(f"import base64\nexec(base64.b16decode('{encrypted}').decode())")
        console.print(f"{H2}• {P2}File encrypted and saved as {K2} {output_path}{reset}")
    except Exception as e:
        console.print(f"{H2}• {P2}Failed to encrypt: {e}{reset}")

# Fungsi Enkripsi Base32
def encrypt_base32(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        encrypted = base64.b32encode(content.encode()).decode()
        default_output = f"{os.path.splitext(file_path)[0]}_enc_base32.py"
        output_path = choose_output_path(default_output)
        with open(output_path, 'w') as f:
            f.write(f"import base64\nexec(base64.b32decode('{encrypted}').decode())")
        console.print(f"{H2}• {P2}File encrypted and saved as {K2} {output_path}{reset}")
    except Exception as e:
        console.print(f"{H2}• {P2}Failed to encrypt: {e}{reset}")

# Fungsi Enkripsi Base64
def encrypt_base64(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        encrypted = base64.b64encode(content.encode()).decode()
        default_output = f"{os.path.splitext(file_path)[0]}_enc_base64.py"
        output_path = choose_output_path(default_output)
        with open(output_path, 'w') as f:
            f.write(f"import base64\nexec(base64.b64decode('{encrypted}').decode())")
        console.print(f"{H2}• {P2}File encrypted and saved as {K2} {output_path}{reset}")
    except Exception as e:
        console.print(f"{H2}• {P2}Failed to encrypt: {e}{reset}")

# Fungsi Enkripsi Zlib
def encrypt_zlib(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        compressed = zlib.compress(content.encode())
        default_output = f"{os.path.splitext(file_path)[0]}_enc_zlib.py"
        output_path = choose_output_path(default_output)
        with open(output_path, 'w') as f:
            f.write(f"import zlib\nexec(zlib.decompress({repr(compressed)}).decode())")
        console.print(f"{H2}• {P2}File encrypted and saved as {K2} {output_path}{reset}")
    except Exception as e:
        console.print(f"{H2}• {P2}Failed to encrypt: {e}{reset}")

# Fungsi Enkripsi Marshal
def encmarshal():
    file = input(f"{H2}• {P2}Nama file untuk di encrypt: ")
    fileout = input(f"{H2}• {P2}Output File Name: ")
    delay_print("• Sedang Encrypting ...")
    
    # Membaca konten file yang akan dienkripsi
    try:
        with open(file, 'r') as f:
            fileopen = f.read()
    except FileNotFoundError:
        console.print(f"{H2}• {P2}File tidak ditemukan! Pastikan path file benar.{reset}")
        return

    # Mengompilasi dan mengenkripsi file dengan marshal
    a = compile(fileopen, "dg", "exec")
    m = marshal.dumps(a)
    s = repr(m)
    
    # Menyusun kode untuk mengeksekusi marshal yang telah dienkripsi
    b = """#ngapain bang ke sini
#mau recode hahaha
#usaha bang, btw follow github gw
#https://github.com/Viper404-XD

import marshal
exec(marshal.loads(""" + s + """))"""
    
    time.sleep(3)
    delay_print("• Encryption Completed...")
    
    # Menulis file yang telah dienkripsi
    with open(fileout, "w") as f_out:
        f_out.write(b)
    
    time.sleep(3)
    console.print(f"{H2}• {P2}Output File Name ➛ {K2} {fileout}{reset}")
    move_file(fileout)

# Fungsi Dekripsi Base16
def decrypt_base16(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read().replace('exec(base64.b16decode("', '').replace('").decode())', '')
        decrypted = base64.b16decode(content).decode()
        default_output = f"{os.path.splitext(file_path)[0]}_dec_base16.py"
        output_path = choose_output_path(default_output)
        with open(output_path, 'w') as f:
            f.write(decrypted)
        console.print(f"{H2}• {P2}File decrypted and saved as {K2} {output_path}{reset}")
        move_file(output_path)
    except Exception as e:
        console.print(f"{H2}• {P2}Failed to decrypt: {e}{reset}")

# Fungsi Dekripsi Base32
def decrypt_base32(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read().replace('exec(base64.b32decode("', '').replace('").decode())', '')
        decrypted = base64.b32decode(content).decode()
        default_output = f"{os.path.splitext(file_path)[0]}_dec_base32.py"
        output_path = choose_output_path(default_output)
        with open(output_path, 'w') as f:
            f.write(decrypted)
        console.print(f"{H2}• {P2}File decrypted and saved as {K2} {output_path}{reset}")
        move_file(output_path)
    except Exception as e:
        console.print(f"{H2}• {P2}Failed to decrypt: {e}{reset}")

# Fungsi Dekripsi Base64
def decrypt_base64(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read().replace('exec(base64.b64decode("', '').replace('").decode())', '')
        decrypted = base64.b64decode(content).decode()
        default_output = f"{os.path.splitext(file_path)[0]}_dec_base64.py"
        output_path = choose_output_path(default_output)
        with open(output_path, 'w') as f:
            f.write(decrypted)
        console.print(f"{H2}• {P2}File decrypted and saved as {K2} {output_path}{reset}")
        move_file(output_path)
    except Exception as e:
        console.print(f"{H2}• {P2}Failed to decrypt: {e}{reset}")

# Fungsi Dekripsi Zlib
def decrypt_zlib(file_path):
    try:
        with open(file_path, 'r') as f:
            content = eval(f.read().replace('exec(', '').replace(')', ''))
        decompressed = zlib.decompress(content).decode()
        default_output = f"{os.path.splitext(file_path)[0]}_dec_zlib.py"
        output_path = choose_output_path(default_output)
        with open(output_path, 'w') as f:
            f.write(decompressed)
        console.print(f"{H2}• {P2}File decrypted and saved as {K2} {output_path}{reset}")
        move_file(output_path)
    except Exception as e:
        console.print(f"{H2}• {P2}Failed to decrypt: {e}{reset}")

# Fungsi Dekripsi Marshal
def decmarshal():
    file = input(f"{H2}• {P2}Nama file untuk di decrypt: ")
    fileout = input(f"{H2}• {P2}Output File Name: ")
    delay_print("• Sedang Decrypting ...")
    try:
        with open(file, 'r') as f:
            content = f.read()
        start = content.find('exec(marshal.loads(')
        end = content.find('))', start) + 2
        encrypted_code = content[start + 18:end - 2]
        decoded_code = marshal.loads(eval(encrypted_code))
        with open(fileout, 'w') as f_out:
            f_out.write(decoded_code.decode())
        console.print(f"{H2}• {P2}File decrypted and saved as {K2} {fileout}{reset}")
        move_file(fileout)
    except Exception as e:
        console.print(f"{H2}• {P2}Failed to decrypt: {e}{reset}")

# Fungsi Dekripsi Marshal + Zlib + Base64
def decrypt_mzb(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        content = content.replace('exec(marshal.loads(zlib.decompress(base64.b64decode("', '').replace('"))))', '')
        decrypted = marshal.loads(zlib.decompress(base64.b64decode(content)))
        default_output = f"{os.path.splitext(file_path)[0]}_dec_mzb.py"
        output_path = choose_output_path(default_output)
        with open(output_path, 'w') as f:
            f.write(decrypted.decode())
        console.print(f"{H2}• {P2}File decrypted and saved as {K2} {output_path}{reset}")
        move_file(output_path)
    except Exception as e:
        console.print(f"{H2}• {P2}Failed to decrypt: {e}{reset}")

# Fungsi menu enkripsi
def encryption_menu():
    clear()
    console.print(f"{H2}Encryptor Menu{reset}")
    print("[1] Encrypt Base16")
    print("[2] Encrypt Base32")
    print("[3] Encrypt Base64")
    print("[4] Encrypt Marshal")
    print("[5] Encrypt Zlib")
    print("[6] Encrypt Marshal + Zlib + Base64")
    print("[0] Back")
    choice = input("Choose an option: ")
    if choice == "1":
        encrypt_base16(input("Enter the file path: "))
    elif choice == "2":
        encrypt_base32(input("Enter the file path: "))
    elif choice == "3":
        encrypt_base64(input("Enter the file path: "))
    elif choice == "4":
        encmarshal()
    elif choice == "5":
        encrypt_zlib(input("Enter the file path: "))
    elif choice == "6":
        encrypt_mzb(input("Enter the file path: "))
    elif choice == "0":
        main_menu()
    else:
        console.print(f"{H2}Invalid choice, try again.{reset}")
        encryption_menu()

# Fungsi menu dekkripsi
def decryption_menu():
    clear()
    console.print(f"{H2}Decryptor Menu{reset}")
    print("[1] Decrypt Base16")
    print("[2] Decrypt Base32")
    print("[3] Decrypt Base64")
    print("[4] Decrypt Zlib")
    print("[5] Decrypt Marshal")
    print("[6] Decrypt Marshal + Zlib + Base64")
    print("[0] Back")
    choice = input("Choose an option: ")
    if choice == "1":
        decrypt_base16(input("Enter the file path: "))
    elif choice == "2":
        decrypt_base32(input("Enter the file path: "))
    elif choice == "3":
        decrypt_base64(input("Enter the file path: "))
    elif choice == "4":
        decrypt_zlib(input("Enter the file path: "))
    elif choice == "5":
        decmarshal()
    elif choice == "6":
        decrypt_mzb(input("Enter the file path: "))
    elif choice == "0":
        main_menu()
    else:
        console.print(f"{H2}Invalid choice, try again.{reset}")
        decryption_menu()

# Fungsi utama
def main_menu():
    clear()
    console.print(f"{H2}Python Encryption/Decryption Tool{reset}")
    print("[1] Encryption Menu")
    print("[2] Decryption Menu")
    print("[0] Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        encryption_menu()
    elif choice == "2":
        decryption_menu()
    elif choice == "0":
        sys.exit()
    else:
        console.print(f"{H2}Invalid choice, try again.{reset}")
        main_menu()

# Eksekusi utama
if __name__ == "__main__":
    main_menu()
