# Author: Jared Frees, Zach Cusick

import socket
import sys
import time
import os
import socketserver
import threading
#TODO for future maybe make multithreaded, on-blocking sockets?

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        address = self.client_address
        cur_thread = threading.current_thread()
        data = data.decode('utf-8')
        response = "{}: {}".format(cur_thread.name, "Hello world this is a pot")
        log(address, data)
        print("On ", cur_thread.name," connected to: ", address[0], ":", address[1], sep='')
        b = response.encode('utf-8')
        self.request.sendall(b)
               

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

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

  server = ThreadedTCPServer((host, port), ThreadedTCPRequestHandler)
  ip, port = server.server_address

  # Start a thread with the server -- that thread will then start one
  # more thread for each request
  server_thread = threading.Thread(target=server.serve_forever(0.5))
  # Exit the server thread when the main thread terminates
  server_thread.daemon = True
  server_thread.start()
  
def main():
  try:
    run_pot()
  except KeyboardInterrupt:
    print('Exiting server')
    sys.exit(1)

if __name__ == '__main__':
  main()
