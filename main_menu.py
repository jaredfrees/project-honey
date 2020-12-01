#Author: Brian Fissel
#import importlib

import ftp.ftp_server
import httpServer.http_server
import tcp.tcp_honeypot
import ssh.ssh_server
import time

def get_valid_int():
    try:
        choice = input("Please Select an Option by Typing in a Number and Pressing Enter: ")
        choice = int(choice)
    except ValueError:
        choice = 0
    return choice

def main():
    print("Welcome to our Honeypot!")
    print("----------------------------------------------------------------")
    print("1. FTP Honeypot")
    print("2. TCP Honeypot")
    print("3. HTTP Honeypot")
    print("4. SSH Honeypot")
    
    choice = get_valid_int()
    if choice == 1:
        ftp.ftp_server.main()
        #I am getting an error reading the ftp_port, check that, might need to put ftp in a main method.
        print("FTP")
    elif choice == 2:
        tcp.tcp_honeypot.main()
    elif choice == 3:
        httpServer.http_server.main()
    elif choice == 4:
        ssh.ssh_server.main()
    else:
        print("Not a valid selection")
        time.sleep(.5)
        print('')
        main()
        
if __name__ == "__main__":
    main()
