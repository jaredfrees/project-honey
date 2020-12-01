#Author: Brian Fissel
import importlib

#import ftp.ftp_server
import httpServer.http_server
import tcp.tcp_honeypot
import ssh.ssh_server

def main():
    print("Welcome to our Honeypot!")
    print("----------------------------------------------------------------")
    print("1. FTP Honeypot")
    print("2. TCP Honeypot")
    print("3. HTTP Honeypot")
    print("4. SMTP Honeypot")
    print("5. SSH Honeypot")
    choice = input("Please Select an Option by Typing in a Number and Pressing Enter: ")
    choice = int(choice)
    if choice == 1:
        #ftp.ftp_server
        #I am getting an error reading the ftp_port, check that, might need to put ftp in a main method.
        print("FTP")
    elif choice == 2:
        tcp.tcp_honeypot.main()
    elif choice == 3:
        httpServer.http_server.main()
    elif choice == 4:
        execfile('smtp_server.py') #this file isn't in master yet, still on own branch
        #Just do what I did for other files when it is branched in
    elif choice == 5:
        ssh.ssh_server.main()
    else:
        print("Not a valid Selection")
        main()
        
if __name__ == "__main__":
    main()
