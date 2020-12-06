# Author: Jared Frees, Zach Cusick
# Testing: nc 127.0.0.1 25565

import socket
import sys
import time
import os
import socketserver
import threading
from common.common import HoneypotBaseServer

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # Get initial connection
        address = self.client_address
        data = ''
        log(address, data)

        # Send response
        cur_thread = threading.current_thread()
        response = "{}: {}".format(cur_thread.name, "Thank you for connecting :)\r\n")
        print("On ", cur_thread.name," connected to: ", address[0], ":", address[1], sep='')
        b = response.encode('utf-8')
        self.request.sendall(b)

        # Look for response
        try:
          data = self.request.recv(1024).decode('utf-8').rstrip()
        except (socket.error, socket.timeout):
          pass
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

class TcpHoneypot(HoneypotBaseServer):
  def __init__(self, host='', port=25565):
    HoneypotBaseServer.__init__(self, 'TCP Minecraft')
    self.server = None
    self.server_thread = None
    self.host = host
    self.port = port

  # Opens tcp port and listens for connections
  def run_pot(self):
    print("Starting Minecraft TCP honeypot on port ", self.port, "...", sep="")

    self.server = ThreadedTCPServer((self.host, self.port), ThreadedTCPRequestHandler)

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    self.is_running = True
    print('TCP server started')
    self.server_thread = threading.Thread(target=self.server.serve_forever, daemon=True)
    # Exit the server thread when the main thread terminates
    self.server_thread.start()
    
  # TODO: Doesn't work...
  def stop_pot(self):
    print('thread:', self.server_thread)
    #self.server_thread.join()
    #print('join stopped')
    #print('isalive:', self.server_thread.is_alive())

    self.server.shutdown()


def main():
  try:
    server = TcpHoneypot()
    server.run_pot()
  except KeyboardInterrupt:
    print('Closing TCP server...')
    sys.exit(1)

if __name__ == '__main__':
  main()
