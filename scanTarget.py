import argparse
import socket
from threading import *
# From project outlines
semLock = Semaphore(value=1)


def connScan(tgtHost, tgtPort):
    #  connScan will be the function run as a thread and args will be the arguments used by
    #  the function
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create socket
        s.settimeout(0.5)
        s.connect((tgtHost, tgtPort))  # connect
        semLock.acquire()
        print(tgtPort, " /tcp port open")  # print that that port is open
        s.close()  # close the connection
    except:
        semLock.acquire()
        print(tgtPort,  "is filtered or closed")
    finally:
        semLock.release()


def portScan(tgtHost, tgtPorts):  # Code from class
    try:
        tgtIP = socket.gethostbyname(tgtHost)
        print(tgtIP)
    except:
        print("[-] Cannot resolve", tgtHost, ": Unknown Host")
        return

    for tgtPort in tgtPorts:  # Outlined in Project guidelines
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()


def main():  # code from class
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', dest='tgtHost', required=True,
                        help='specify target host')
    parser.add_argument('-p', dest='tgtPorts',
                        default='21, 22, 23, 25, 80, 443', help='specify target port(s)')

    args = parser.parse_args()
    tgtHost = args.tgtHost
    tgtPorts = str(args.tgtPorts).split(', ')

    portScan(tgtHost, tgtPorts)


#   Cyber  _  Ducky
#        >(.)__
#         (___/


if __name__ == "__main__":
    main()
