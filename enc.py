import os
# ------------------[  WARNA  ]-------------------#
M2 = "[#FF0000]"  # MERAH
H2 = "[#00FF00]"  # HIJAU
K2 = "[#FFFF00]"  # KUNING
B2 = "[#00C8FF]"  # BIRU
P2 = "[#FFFFFF]"  # PUTIH
U2 = "[#AF00FF]"  # UNGU
O2 = "[#FF8F00]"  # ORANGE

# ------------------[  MODULE  ]-------------------#
try:
    import rich
except ImportError:
    os.system("pip install rich")
from rich.console import Console

console = Console()
try:
    import rich
except ImportError:
    console.print(f" {H2}• {U2}Sedang Menginstall Modul Rich {H2}•{P2}")
    os.system("pip install rich")
try:
    import stdiomask
except ImportError:
    console.print(f" {H2}• {U2}Sedang Menginstall Modul stdiomask {H2}•{P2}")
    os.system("pip install stdiomask")
try:
    import bs4
except ImportError:
    console.print(f" {H2}• {U2}Sedang Menginstall Modul bs4 {H2}•{P2}")
    os.system("pip install bs4")
try:
    import base64
except ImportError:
    console.print(f" {H2}• {U2}Sedang Menginstall Modul bs4 {H2}•{P2}")
    os.system("pip install base64")

import bs4, sys,time,base64,stdiomask,marshal,zlib,binascii,py_compile
from time import sleep as vip
from rich.panel import Panel as panel
from rich.console import Console
def jalan(keliling):
    for mau in keliling + "\n":
        sys.stdout.write(mau)
        sys.stdout.flush()
        vip(0.03)
def clear():
    os.system("clear")

pwd=os.getcwd()
def error():
    console.print(f"{H2}• {P2}Sedang dalam tahap pengembangan")
def banner():
    console.print(panel(f"""{H2}\t_ __  _   _  ___ _ __   ___ 
\t| '_ \| | | |/ _ \ '_ \ / __|
\t| |_) | |_| |  __/ | | | (__ 
\t| .__/ \__, |\___|_| |_|\___|
\t| |     __/ |                
\t|_|    |___/   {K2}By: Rudal-XD{P2}
""",width=60,style="bold cyan"))
    
def menu():
    clear()
    banner()
    Console().print(panel(f"""\t{P2}[{H2}01{P2}]. {H2}Encrypt Marshal
\t{P2}[{H2}02{P2}]. {H2}Encrypt Bash  
\t{P2}[{H2}03{P2}]. {H2}Encrypt Python into Emoji 
\t{P2}[{H2}04{P2}]. {H2}Encrypt Python Variable 
\t{P2}[{H2}05{P2}]. {H2}Encrypt Base64 
\t{P2}[{H2}06{P2}]. {H2}Encrypt Py {K2}➛  {K2}Pyc
\t{P2}[{H2}07{P2}]. {H2}Encrypt Zlib, {K2}Base64
\t{P2}[{H2}08{P2}]. {H2}Encrypt Marshal, {K2}Zlib, {B2}Base64
\t{P2}[{H2}09{P2}]. {K2}Decrypt Bash""",width=60,style="bold cyan"))
    vipper = console.input(f"{H2}• {P2}pilih menu : ")
    if vipper in [""]:
        console.print(f"{H2}• {P2}[bold red]Masukan Yang Bener Tolol!!! ")
    elif vipper in ["1", "01"]:
        encmarshal()
    elif vipper in ["2", "02"]:
        encbash()
    elif vipper in ["3", "03"]:
        error()
    elif vipper in ["4", "04"]:
        error()
    elif vipper in ["5", "05"]:
        error()
    elif vipper in ["6", "06"]:
        error()
    elif vipper in ["7", "07"]:
        error()
    elif vipper in ["8", "08"]:
        error()


def encmarshal():
    file = console.input(f"{H2}• {P2}nama file untuk di encrypt : ")
    fileout = console.input(f"{H2}• {P2}Output File Name : ")
    jalan("• Sedang Encrypting ...")
    fileopen = open(file).read()
    a = compile(fileopen, "dg", "exec")
    m = marshal.dumps(a)
    s = repr(m)
    b = "#ngapain bang ke sini\n#mau recode hahaha\n#usaha bang, btw follow github gw\n#https://github.com/Rudal-XD\n\n\nimport marshal\nexec(marshal.loads(" + s + "))"
    time.sleep(3)
    jalan("• Encryption Completed...")
    open("{fileout}","w").write(b)
    time.sleep(3)
    console.print(f"{H2}• {P2}Output File Name ➛ {K2} %s"%(fileout))
    mover(fileout)

# Encrypt Bash code by npm package "bash-obfuscate"
def encbash():
    in_file = input("Input Filename  > ")
    if not os.path.exists(in_file):
        print('File not found')
        os.system("sleep 2")
        encbash()
    os.system("bash-obfuscate " + in_file + " -o .temp")
    if not os.path.exists(".temp"):
        try:
            print("Installing Bash-Obfuscate....\n")
            os.system("apt install nodejs -y && npm install -g bash-obfuscate")
            os.system("bash-obfuscate " + in_file + " -o .temp")
        except:
            print(" Bash-Obfuscate not installed! Install it by:\n{H2}[+] \"apt install nodejs -y && npm install -g bash-obfuscate\"")
            exit(1)
    out_file= input("Output Filename  > ")   
    with open(".temp",'r') as temp_f, open(out_file,'w') as out_f:
        filedata = temp_f.read()
        out_f.write("#ngapain bang ke sini\n#mau recode hahaha\n#usaha bang, btw follow github gw\n#https://github.com/Rudal-XD\n\n"+filedata)
    os.remove(".temp")
    print(f"{H2}{out_file} saved in {pwd}")
    mover(out_file)

# Custom path chooser
def mover(out_file):
    move= input("Move to a custom path?(y/n) > ")
    if move=="y":
        mpath=input("Enter the path > ")
        if os.path.exists(mpath):
            os.system(f'''mv -f "{out_file}" "{mpath}" ''')
            print(f"{out_file} moved to {mpath}\n")
        else:
            print("Path do not exist!\n")
    else:
        print("\n")
    exit()
    
if __name__=='__main__':
    menu()
