# Author:Zach Cusick

import socket
import sys
import time
import os
import socketserver
import threading
import http.server

file = open("project-honey/HomePage.html", "r")
class ThreadedHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(file.read(), "utf-8"))
        address = self.client_address
        data = "GET request version: " + self.request_version
        log(address, data)
                      

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
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
  port = 80

  server = ThreadedHTTPServer((host, port), ThreadedHTTPRequestHandler)
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
