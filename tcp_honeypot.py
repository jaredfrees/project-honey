# Author: Jared Frees

import socket
import sys
import time
import os

#TODO for future maybe make multithreaded, on-blocking sockets?


def log(address, data):
  sep = '-' * 50
  with open('./log.txt', 'a') as file:
    file.write('Time: {}\nIP: {}\nPort: {}\nData: {}\n'.format(time.ctime(), address[0], address[1], data))
    file.write(sep + '\n')


# Opens tcp port and listens for connections
def run_pot():
  print("Starting honeypot...")
  host = ''
  port = 25565

  # create socket object
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # tell computer to give me this port
  s.bind((host, port))
  # listen for connections, max 100 connections at a time
  s.listen(100)
  print('Bound to port:', port)
  print('Waiting for connection...')

  #while True:
  (new_conn, address) = s.accept()
  print("Connected to: ", address[0], ":", address[1], sep='')

  try:
    # Send message to connected computer
    new_conn.send(b"Hello world this is a pot\n")

    # Receive data from connected computer
    data = new_conn.recv(1024)
    data = data.decode('utf-8')
    print("Data:", data)
    log(address, data)

    # TODO: try to get info about connected computer?


  except socket.error as e:
    print("Caught exception:", e)
    sys.exit(1)


def main():
  try:
    run_pot()
  except KeyboardInterrupt:
    print('Exiting server')
    sys.exit(1)

if __name__ == '__main__':
  main()
