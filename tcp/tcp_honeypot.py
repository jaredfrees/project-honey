# Author: Jared Frees, Zach Cusick
# Testing: nc 127.0.0.1 25565

import socket
import sys
import time
import os
import socketserver
import threading

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # Get initial connection
        address = self.client_address
        log(address, '')

        # Send response
        cur_thread = threading.current_thread()
        response = "{}: {}".format(cur_thread.name, "Thank you for connecting :)\r\n")
        print("On ", cur_thread.name," connected to: ", address[0], ":", address[1], sep='')
        b = response.encode('utf-8')
        self.request.sendall(b)

        # Look for response
        data = self.request.recv(1024).decode('utf-8').rstrip()
        log(address, data)
        
        
        
               

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def log(address, data):
  sep = '-' * 50
  with open('./tcp/logs/minecraft_tcp.log', 'a') as file:
    if not data:
      file.write('*** Initial connection started ***\nTime: {}\nAddress: {}:{}\n'.format(time.ctime(), address[0], address[1]))  
    else:
      file.write('Time: {}\nAddress: {}:{}\nData: {}\n'.format(time.ctime(), address[0], address[1], data))
    file.write(sep + '\n')


# Opens tcp port and listens for connections
def run_pot():
  host = ''
  port = 25565
  print("Starting Minecraft TCP honeypot on port ", port, "...", sep="")

  server = ThreadedTCPServer((host, port), ThreadedTCPRequestHandler)

  # Start a thread with the server -- that thread will then start one
  # more thread for each request
  print('TCP server started')
  server_thread = threading.Thread(target=server.serve_forever(0.5))
  # Exit the server thread when the main thread terminates
  server_thread.daemon = True
  server_thread.start()
  
def main():
  try:
    run_pot()
  except KeyboardInterrupt:
    print('Closing TCP server...')
    sys.exit(1)

if __name__ == '__main__':
  main()
