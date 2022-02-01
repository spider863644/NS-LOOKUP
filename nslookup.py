import os
import time as t
#color
purple = '\033[1;35;40m'
red = '\033[1;31;40m'
green = '\033[1;32;40m'
yellow = '\033[1;33;40m'
white = '\033[0;37;40m'
blue = '\033[1;34;40m'
purpleyellow = '\033[1;33;45m'
redyellow = '\033[1;33;41m'
t.sleep(5)
print(green + "Installing requirement..." + white)
print(yellow)
os.system("""apt update
apt install cowsay
apt install dnsutils
apt install figlet
apt install toilet""")
print(white)
def loop():
    os.system("clear")
    os.system("figlet NS-LOOKUP")
    global header
    header = green + """
    [+] Tool Name:NSLOOKUP
    [+] Creator:Spider Anongreyhat
    [+] Team:TermuxHackz Society
    [+] Github:https://github.com/spider863644
    [+] WhatsApp:+2349052863644
    [+] Facebook:https://facebook.com/SpiderAnongreyhat
    [+] Version:V1.0
    """ + white
    print (header)
    print(red + "==================================" + yellow + "========================================" + blue + "============================" + white)
    print(green + """
    Do you agree to our terms and conditions?
    [1]Yes
    [2]No
    """ + white)
    try:
        tc = int(input(yellow + "$ " + white))
    except ValueError:
        print(red + "Only interger is allowed! " + white)
        t.sleep(3)
        loop()
    if tc == 1:
        print(yellow + "You are now allowed to use this tool" + white)
    elif tc == 2:
        print(red + "I know say you be werey hahaha\nWell you aren\'t allowed to use this" + white)
        t.sleep(5)
        exit()
loop()
t.sleep(2)
def loop2():
    os.system("clear")
    os.system("cowsay NS-LOOKUP")
    print(header)
    print(purpleyellow + "$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Let\'s go $$$$$$$$$$$$$$$$$$$$$$$" + white)
    
    print("")
    print(blue + """
    [1]Scan Website
    [2]Update Script
    [3]Join our whatsapp group
    [4]Exit Tool
    """ + white)
    try:
        c = int(input(redyellow + "Enter a valid option " + purple))
    except ValueError:
        print(red + "Only integers are allowed! " + white)
        t.sleep(2)
        loop2()
    if c == 1:
        os.system("clear")
        os.system("toilet NS-LOOKUP")
        print(header)
        print(red + "Turn on your data connection" + white)
        url = input(redyellow + "Enter the url of the website you wanna scan>> " + green)
        if "www." not in url:
            print(red + url + " is not a valid url" + white)
            t.sleep(4)
            loop2()
        print(blue + "Getting info of  " + url + white)
        t.sleep(3)
        print(yellow)
        lookup = "nslookup " + url
        os.system(lookup)
        print(white)
    elif c == 2:
        os.system("clear")
        print(redyellow + "Updating..." + white)
        t.sleep(4)
        os.system("""
        cd
        rm -f -r NS-LOOKUP
        cd
        git clone https://github.com/spider863644/NS-LOOKUP
        """)
        print(green + """Now type the following command;
        cd $HOME
        cd NS-LOOKUP
        python3 nslookup.py
        """ + white)
        exit()
    elif c == 3:
        os.system("clear")
        print(redyellow + "Redirecting to my Whataspp group..." + white)
        t.sleep(2)
        os.system("xdg-open https://chat.whatsapp.com/BivW6pA9Emu9bDM2rZkaQy")
        t.sleep(3)
        loop2()
    elif c == 4:
        print(green + "Thanks for using my tools\nKindly follow me on github" + white)
        t.sleep(4)
        os.system("xdg-open https://github.com/spider863644")
        t.sleep(1)
        exit()
    cont = input(redyellow + "Do you wanna scan another website [y/n] ")
    if cont == "y" or cont == "Y":
        loop2()
loop2()