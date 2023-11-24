import os
import sys
import time
import base64
import marshal
import zlib
import binascii
import py_compile

R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
B = "\033[1;34m"
C = "\033[1;36m"
W = "\033[1;37m"
P = "\033[1;97m"
def slowprint(s):
	try:
		for c in s + "\n":
        	    sys.stdout.write(c)
	            sys.stdout.flush()
	            time.sleep(0.001)
	except (KeyboardInterrupt,EOFError):
		run("Nonaktif!!!")
		
def slowprintxx(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0000000.01)
        
logo = """
\033[1;91m      ____        ______          
\033[1;92m     / __ \__  __/ ____/___  _____
\033[1;93m    / /_/ / / / / __/ / __ \/ ___/
\033[1;94m   / ____/ /_/ / /___/ / / / /__  
\033[1;95m  /_/    \__, /_____/_/ /_/\___/  
\033[1;96m        /____/ \033[1;93mBy \033[1;97mAngga Kurniawan                   
"""

anggaxd = """
  \033[1;97m[\033[1;92m 01 \033[1;97m] Encrypt Marshal 
  \033[1;97m[\033[1;92m 02 \033[1;97m] Encrypt Base64  
  \033[1;97m[\033[1;92m 03 \033[1;97m] Encrypt Base32  
  \033[1;97m[\033[1;92m 04 \033[1;97m] Encrypt Base16 
  \033[1;97m[\033[1;92m 05 \033[1;97m] Encrypt Zlib    
  \033[1;97m[\033[1;92m 06 \033[1;97m] Encrypt Py \033[1;96m> \033[1;97mPyc
  \033[1;97m[\033[1;92m 07 \033[1;97m] Encrypt Marshal\033[1;37m,\033[1;33mZlib\033[1;37m,\033[1;33mBase64
  \033[1;97m[\033[1;92m 08 \033[1;97m] Encrypt Marshal\033[1;37m,\033[1;33mZlib\033[1;37m,\033[1;33mBase32
  \033[1;97m[\033[1;92m 09 \033[1;97m] Encrypt Marshal\033[1;37m,\033[1;33mZlib\033[1;37m,\033[1;33mBase16
  \033[1;97m[\033[1;92m 10 \033[1;97m] Encrypt Zlib\033[1;37m,\033[1;33mBase64
"""
os.system("clear")
print logo
slowprint (anggaxd)

mainmenu = raw_input(G + "  \033[1;97m[\033[1;93m ?? \033[1;97m] choose/" + R + "> " + G)

if mainmenu == "1" or mainmenu == "01":
    file = raw_input(P + "  Name of the File to Encrypt" + C + " > " + Y)
    c = raw_input(P + "  Output File Name" + C + " > " + Y)
    slowprint (G + "  Encrypting ...")
    fileopen = open(file).read()
    a = compile(fileopen, "dg", "exec")
    m = marshal.dumps(a)
    s = repr(m)
    b = "#yo ndak tau komk tanya saya\n\nimport marshal\nexec(marshal.loads(" + s + "))"
    d = open(c, "w")
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + "  Encryption Completed...")
    time.sleep(3)
    print P + "  Output File Name : " + Y, c
    print (W)
elif mainmenu == "2" or mainmenu == "02":
    file = raw_input(P + "  Name of the File to Encrypt" + C + " > " + Y)
    c = raw_input(P + "  Output File Name" + C + " > " + Y)
    slowprint (G + "  Encrypting ...")
    fileopen = open(file).read()
    a = base64.b64encode(fileopen)
    b = "#yo ndak tau komk tanya saya\n\nimport base64\nexec(base64.b64decode("" + a + ""))"
    d = open(c, "w")
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + "  Encryption Completed...")
    time.sleep(3)
    print P + "  Output File Name : " + Y, c
    print (W)
elif mainmenu == "3" or mainmenu == "03":
    file = raw_input(P + "  Name of the File to Encrypt" + C + " > " + Y)
    c = raw_input(P + "  Output File Name" + C + " > " + Y)
    slowprint (G + "  Encrypting ...")
    fileopen = open(file).read()
    a = base64.b32encode(fileopen)
    b = "#yo ndak tau komk tanya saya\n\nimport base32\nexec(base64.b32decode("" + a + ""))"
    d = open(c, "w")
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + "  Encryption Completed...")
    time.sleep(3)
    print P + "  Output File Name : " + Y, c
    print (W)
elif mainmenu == "4" or mainmenu == "04":
    file = raw_input(P + "  Name of the File to Encrypt" + C + " > " + Y)
    c = raw_input(P + "  Output File Name" + C + " > " + Y)
    slowprint (G + "  Encrypting ...")
    fileopen = open(file).read()
    a = base64.b16encode(fileopen)
    b = "#yo ndak tau komk tanya saya\n\nimport base16\nexec(base64.b16decode("" + a + ""))"
    d = open(c, "w")
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + "  Encryption Completed...")
    time.sleep(3)
    print P + "  Output File Name : " + Y, c
    print (W)    
elif mainmenu == "5" or mainmenu == "05":
    file = raw_input(P + "  Name of the File to Encrypt" + C + " > " + Y)
    c = raw_input(P + "  Output File Name" + C + " > " + Y)
    slowprint (G + "  Encrypting ...")
    fileopen = open(file).read()
    a = zlib.compress(fileopen)
    b = "#yo ndak tau komk tanya saya\n\nimport zlib\nexec(zlib.compress("" + a + ""))"
    d = open(c, "w")
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + "  Encryption Completed...")
    time.sleep(3)
    print P + "  Output File Name : " + Y, c
    print (W)        
elif mainmenu == "6" or mainmenu == "06":
    file = raw_input(P + "  Name of the File to Encrypt" + C + " > " + Y)
    from py_compile import compile
    compile(file)
    slowprint(G + "  Encryption Completed...")
    time.sleep(3)
    print (W)        
elif mainmenu == "7" or mainmenu == "07":
    file = raw_input(P + "  Name of the File to Encrypt" + C + " > " + Y)
    c = raw_input(P + "  Output File Name" + C + " > " + Y)
    slowprint (P + "  Encrypting...")
    fileopen = open(file).read()
    sa = compile(fileopen, "dg", "exec")
    sb = marshal.dumps(sa)
    sc = zlib.compress(sb)
    sd = base64.b64encode(sc)
    b = "#yo ndak tau komk tanya saya\n\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b64decode("" + str(sd) + ""))))"
    d = open(c, "w")
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + "  Encryption Completed...")
    time.sleep(3)
    print P + "  Output File Name : " + Y, c
    print (W)
elif mainmenu == "8" or mainmenu == "08":
    file = raw_input(P + "  Name of the File to Encrypt" + C + " > " + Y)
    c = raw_input(P + "  Output File Name" + C + " > " + Y)
    slowprint (P + "  Encrypting...")
    fileopen = open(file).read()
    sa = compile(fileopen, "dg", "exec")
    sb = marshal.dumps(sa)
    sc = zlib.compress(sb)
    sd = base64.b32encode(sc)
    b = "#yo ndak tau komk tanya saya\n\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b32decode("" + str(sd) + ""))))"
    d = open(c, "w")
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + "  Encryption Completed...")
    time.sleep(3)
    print P + "  Output File Name : " + Y, c
    print (W)
elif mainmenu == "9" or mainmenu == "09":
    file = raw_input(P + "  Name of the File to Encrypt" + C + " > " + Y)
    c = raw_input(P + "  Output File Name" + C + " > " + Y)
    slowprint (P + "  Encrypting...")
    fileopen = open(file).read()
    sa = compile(fileopen, "dg", "exec")
    sb = marshal.dumps(sa)
    sc = zlib.compress(sb)
    sd = base64.b16encode(sc)
    b = "#yo ndak tau komk tanya saya\n\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b16decode("" + str(sd) + ""))))"
    d = open(c, "w")
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + "  Encryption Completed...")
    time.sleep(3)
    print P + "  Output File Name : " + Y, c
    print (W)    
elif mainmenu == "10":
    file = raw_input(P + "  Name of the File to Encrypt" + C + " > " + Y)
    c = raw_input(P + "  Output File Name" + C + " > " + Y)
    slowprint (P + "  Encrypting...")
    fileopen = open(file).read()
    sa = zlib.compress(fileopen)
    sb = base64.b64encode(sa)
    b = "#yo ndak tau komk tanya saya\n\nimport zlib,base64\nexec(zlib.decompress(base64.b64decode("" + sb + "")))"
    d = open(c, "w")
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + "  Encryption Completed...")
    time.sleep(3)
    print P + "  Output File Name : " + Y, c
    print (W)    
elif mainmenu == "11":
    file = raw_input(P + "  Name of the File to Encrypt" + C + " > " + Y)
    c = raw_input(P + "  Output File Name" + C + " > " + Y)
    slowprint (G + "  Encrypting ...")
    fileopen = open(file).read()
    a = compile(fileopen, "dg", "exec")
    m = marshal.dumps(a)
    s = repr(m)
    from py_compile import compile
    compile(file)
    b = "#yo ndak tau komk tanya saya\n\nimport marshal\nexec(marshal.loads(" + s + "))"
    d = open(c, "w")
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + "  Encryption Completed...")
    time.sleep(3)
    print P + "  Output File Name : " + Y, c
    print (W)    
