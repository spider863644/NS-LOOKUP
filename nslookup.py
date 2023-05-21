import socket
import os
import time as t
try:
    import colorama
    import pyfiglet
    import update_check
except:
    print("Running requirements.txt...")
    t.sleep(3)
    os.system("pip install -r requirements.txt")
finally:
    print("Requirement installed successfully 😊")
from update_check import isUpToDate, update
from colorama import *
def loop():
    os.system("clear")
    #head = pyfiglet.figlet_format("NS-Lookup")
    print(Fore.YELLOW + """
     _______    _________         .____    ________   ________   ____  __.____ _____________ 
 \      \  /   _____/         |    |   \_____  \  \_____  \ |    |/ _|    |   \______   \
 /   |   \ \_____  \   ______ |    |    /   |   \  /   |   \|      < |    |   /|     ___/
/    |    \/        \ /_____/ |    |___/    |    \/    |    \    |  \|    |  / |    |    
\____|__  /_______  /         |_______ \_______  /\_______  /____|__ \______/  |____|    
        \/        \/                  \/       \/         \/        \/                   """)
    print(Fore.RED + " Version 2.1".center(60))
    print("")
    print(Fore.MAGENTA + "[+] " + Fore.CYAN+ "Created by " + Fore.GREEN +" Spider Anongreyhat " + Fore.MAGENTA + "[+]")
    print(Fore.YELLOW + """
[A] Get Website Ip address
[B] Get Ip Address Hostname""" + Fore.RED + """ [Not avaiable] """ + Fore.YELLOW + """ 
[C] Check Update
[D] Visit my github
[E] Exit Tool
""")
    option = str(input(Fore.GREEN + "$ ")).capitalize()
    if option == "A":
        hostname = input(Fore.CYAN + "Enter url: ")
        if "www" not in hostname:
            print(Fore.RED + "please add www to the url \n")
            t.sleep(3)
            loop()
        lookup = socket.gethostbyname(hostname)
        print(Fore.MAGENTA + "Getting " + hostname + " Ip address\n")
        t.sleep(3)
        print(Fore.YELLOW + "Hostname: " + Fore.GREEN + str(hostname))
        print(Fore.YELLOW + "IP Address:" + Fore.GREEN + str(lookup))
    elif option == "B":
        print(Fore.RED + "This is not available yet due to unknown error")
        t.sleep(2)
        loop()
        ip_address = input(Fore.CYAN + "Enter IP Address: ")
        try:
            lookup = socket.gethostbyaddr(ip_address)
            print(lookup)
        except:
            print(Fore.RED + ip_address + " is an invalid IP address")
            t.sleep(3)
            loop()
    elif option == "C":
        if isUpToDate(__file__,  "https://raw.githubusercontent.com/spider863644/NS-LOOKUP/main/nslookup.py") == True:
            print(Fore.YELLOW + 'NS-LOOKUP is up to date')
            t.sleep(2)
            loop()
        else:
            print(Fore.RED + "NS-LOOKUP is outdated, would you like to update it?")
            update = input("").capitalize()
            if update == "YES":
                update("nslookup.py",  "https://raw.githubusercontent.com/spider863644/NS-LOOKUP/main/nslookup.py")
                print(Fore.GREEN + "Updated\n\nRun script again")
                t.sleep(2)
                exit()
    elif option == "D":
        os.system("xdg-open https://github.com/spider863644")
        loop()
    elif option == "E":
        exit()
    else:
        print(Fore.RED + """Invalid option, kindly wear glasses and Input a valid alphabet from the list of options""")
        t.sleep(2)
        loop()
loop()