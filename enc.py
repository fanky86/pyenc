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
        encryptem()
    elif vipper in ["4", "04"]:
        encryptvar()
    elif vipper in ["5", "05"]:
        error()
    elif vipper in ["6", "06"]:
        error()
    elif vipper in ["7", "07"]:
        error()
    elif vipper in ["8", "08"]:
        error()
    elif vipper in ["9", "09"]:
        decryptsh()


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
    open(fileout,"w").write(b)
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

# Encrypting python file into emoji
def encryptem():
    in_file= input("Input File  > " )
    if not os.path.isfile(in_file):
        print(' File not found')
        os.system("sleep 2")
        encryptem()
    out_file= input( "Output File  > ")
    with open(in_file) as in_f, open(out_file, "w", encoding="utf-8") as out_f:
        out_f.write("# Encrypted by Rudal-XD\n# Github- https://github.com/Rudal-XD/Pyenc\n\n")
        out_f.write(encode_string(in_f.read(), alphabet))
        print(f"{out_file} saved in {pwd}")
        mover(out_file)
def encode_string(in_s, alphabet):
    d1 = dict(enumerate(alphabet))
    d2 = {v: k for k, v in d1.items()}
    return (
        'exec("".join(map(chr,[int("".join(str({}[i]) for i in x.split())) for x in\n'
        '"{}"\n.split("  ")])))\n'.format(
            format(d2),
            chunk_string(
                "  ".join(" ".join(d1[int(i)] for i in str(ord(c))) for c in in_s),
                MAX_STR_LEN,
            ),
        )
)

# Emoji unicode list
alphabet = [
    "\U0001f600",
    "\U0001f603",
    "\U0001f604",
    "\U0001f601",
    "\U0001f605",
    "\U0001f923",
    "\U0001f602",
    "\U0001f609",
    "\U0001f60A",
    "\U0001f61b",
]

# Encrypting python file into base64 variable, easily decryptable
def encryptvar():
    var= input("Variable to be used(Must Required)  > ")
    if (var==""):
        print(" No variable")
        os.system("sleep 3")
        encryptvar()
    if (var.find(" ")!= -1):
        print(" Only one word!")
        os.system("sleep 3")
        encryptvar()
    iteration = input("Iteration count for variable  > ")
    try:
        iteration = int(iteration)
    except Exception:
        iteration = 50
    VARIABLE_NAME = var * iteration
    in_file = input("Input file  > ")
    if not os.path.isfile(in_file):
        print(' File not found')
        os.system("sleep 2")
        encryptvar()
    out_file = input("Output file  > ")
    with open(in_file, 'r', encoding='utf-8', errors='ignore') as in_f,open(out_file, 'w') as out_f:
       file_content = in_f.read()
       obfuscated_content = obfuscate(VARIABLE_NAME, file_content)
       out_f.write("# Encrypted by Rudal-XD\n# Github- https://github.com/Rudal-XD/Pyenc\n\n"+obfuscated_content)
    print(f"{out_file} saved in {pwd}")
    mover(out_file)


# Decrypt bash code by "eval"
def decryptsh():
    in_file = input("Input File  > ")
    if not os.path.exists(in_file):
        print(' File not found')
        os.system("sleep 2")
        decryptsh()
    with open(in_file,'r') as in_f, open(".temp1",'w') as temp_f:
        filedata = in_f.read()
        if not (filedata.find("eval") != -1):
            print(" Cannot be decrypted!")
            exit()
        newdata = filedata.replace("eval","echo")
        temp_f.write(newdata)
    out_file = input("Output File  > ")
    os.system("bash .temp1 > .temp2")
    os.remove(".temp1")
    with open(".temp2",'r') as temp_f2, open(out_file,'w') as out_f:
        filedata = temp_f2.read()
        out_f.write("# Decrypted by Rudal-XD\n# Github- https://github.com/Rudal-XD/Pyenc\n\n"+filedata)
    os.remove(".temp2")
    print(f"{out_file} saved in {pwd}")
    mover(out_file)
    
# Custom path chooser
def mover(out_file):
    print('\n')
    move= console.input(f"{H2}• {P2}Move to a custom path? (y/n) ➛ ")
    if move=="y":
        mpath= console.input(f"{H2}• {P2}Enter the path to ➛ ")
        if os.path.exists(mpath):
            os.system(f'''mv -f "{out_file}" "{mpath}" ''')
            console.print(f"{H2}• {P2}{out_file} moved to {mpath} Succes\n")
        else:
            console.print(f"{H2}• {P2}Path do not exist!\n")
    else:
        print("\n")
    exit()
    
if __name__=='__main__':
    menu()
