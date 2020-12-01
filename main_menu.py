#Author: Brian Fissel, Jared Frees

import ftp.ftp_server
import httpServer.http_server
import tcp.tcp_honeypot
import ssh.ssh_server
import time
import sys

def get_valid_int():
  try:
    #choice = input("Please Select an Option by Typing in a Number and Pressing Enter: ")
    choice = input()
    choice = int(choice)
    print()
    time.sleep(.25)
  except ValueError:
    choice = 0
  return choice


class MainMenu:
  def __init__(self):
    self.tcp_server = tcp.tcp_honeypot.TcpHoneypot()
    self.ssh_server = ssh.ssh_server.SshServer()
    self.ftp_server = ftp.ftp_server.FtpServer()
    self.http_server = httpServer.http_server.HttpServer()
    self.servers = [self.ftp_server, self.tcp_server, self.http_server, self.ssh_server]

  def print_menu(self):
    print('Please choose a selection:')

    for i, server in enumerate(self.servers, start=1):
      if server.is_running:
        print(i, '. (Active) ', server.name, ' Honeypot', sep='')
      else:
        print(i, '. (Not Active) ', server.name, ' Honeypot', sep='')
  
  def check_valid_selection(self, num):
    if self.servers[num - 1].is_running:
      print(self.servers[num - 1].name, 'server is already running')
      return 0
    else:
      return num

  def main(self):
    print("Welcome to our Honeypot!")
    print("----------------------------------------------------------------")
    
    while True:
      self.print_menu()

      choice = self.check_valid_selection(get_valid_int())
      if choice == 1:
        self.ftp_server.run_pot()
      elif choice == 2:
        self.tcp_server.run_pot()
      elif choice == 3:
        self.http_server.run_pot()
      elif choice == 4:
        self.ssh_server.run_pot()
      else:
        print("Not a valid selection")
      
      time.sleep(.5)
      print('')
      


if __name__ == "__main__":
  try:
    main_menu = MainMenu()
    main_menu.main()
  except KeyboardInterrupt:
    print('Exiting program')
    sys.exit(1)
