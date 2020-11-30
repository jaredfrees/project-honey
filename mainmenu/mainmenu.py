#Author: Brian Fissel
import importlib

from project-honey.ftp import ftp_server
from project-honey.http import http_server
from project-honey.smtp import smtp_server
from project-honey.tcp import tcp_server
from project-honey.ssh import ssh_server

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
        execfile('ftp_server.py')
    elif choice == 2:
        execfile('tcp_server.py')
    elif choice == 3:
        execfile('http_server.py')
    elif choice == 4:
        execfile('smtp_server.py') #this file isn't in master yet, still on own branch
    elif choice == 5:
        execfile('ssh_server.py')
    else:
        print("Not a valid Selection")
        main()
        
if __name__ == "__main__":
    main()
