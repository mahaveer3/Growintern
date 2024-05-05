import socket
import os
import sys

def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s= socket.socket()
        s.connect((ip,port))
        banner=  s.recv(1024)
        return banner
    except:
        return
    
def checkVulns(banner,filename):
    f= open(filename , "r")
    for line in f.readlines():
        if line.strip("\n") in banner.decode().strip("\n"):
            print("[+] This Server is Vulnerable " + banner.decode().strip("\n"))


def main():
    if len(sys.argv) != 2:
        print ("[-] Usage :" + str(sys.argv[0]) + " <vuln filename>")
        exit(0)
        
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print("File does not exist")
        exit(0)
    if not os.access(filename, os.R_OK):
        print("[-] Access Denied")
        exit(0)
            
    portlist = [53,143,161,194,69,110,123,139,389,445]
    for x in range(4, 15):
        ip = "8.8.8." +str(x)
        for port in portlist:
            banner = retBanner(ip, port)
            if banner:
                print ("[+] Found Vulnerable Port :" + str(port))
                print ("[+] " + ip + "/" + str(port) + ":" + banner.decode())
                checkVulns(banner, filename)

main()
