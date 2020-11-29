# Author: Jared Frees
# Testing: ssh -p 2222 127.0.0.1
"""
SSH server that accepts connections and immediately closes them to
protect against users trying to break in. This program reads the first line
of the SSH connection to get the client SSH version and logs the version.
This is a low interaction, passive honeypot which means it does not give
the attacker any real access to the computer system, it simply allows a connection
and then closes it so the attacker does not think they actually broke into
an SSH system.
"""

import socket
import sys
import time
import os
import threading

def log(address, data):
  sep = '-' * 50
  with open('./ssh/logs/ssh.log', 'a') as file:
    file.write('Time: {}\nIP: {}\nPort: {}\nClient SSH Version: {}\n'.format(time.ctime(), address[0], address[1], data))
    file.write(sep + '\n')

def handle_ssh_connection(client_sock, addr):
  client_version = client_sock.recv(1024).decode('ascii').rstrip()
  print('Client connected with address:', addr)
  log(addr, client_version)
  client_sock.close()
  
  #my_version = 'SSH-2.0-OpenSSH_6.0p1 Debian-4+deb7u2\r\n'.encode('ascii')
  #client_sock.sendall(my_version)
  #enc_algorithms = client_sock.recv(1024)
  #print(enc_algorithms)
  #b = 'rsa-sha2-512\r\n'.encode('ascii')
  #client_sock.sendall(b)
  #password = client_sock.recv(1024)
  #print(password)

   
# Opens tcp port and listens for connections
def run_pot():
  print("Starting ssh honeypot...")
  host = ''
  port = 2222

  try:
    # Bind socket to port and accept connections from 100 clients max
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(100)
    print('Listening for ssh connection on port ', port, '...', sep='')

    while (True):
      try:
        client_sock, client_addr = sock.accept()
        threading.Thread(target=handle_ssh_connection(client_sock, client_addr)).start()

      except Exception as e:
        print('ERROR: Client connection:', e)
        sys.exit(1)

  except Exception as e:
        print('ERROR: Socket failed on port', port, 'with error:', e)
        sys.exit(1)

def main():
  try:
    run_pot()
  except KeyboardInterrupt:
    print('Exiting server...')
    sys.exit(1)

if __name__ == '__main__':
  main()
