# Author:Zach Cusick
# You can connect to the server via opening your browser and typing in the ip, ex. 127.0.0.1 for self reference

import socket
import sys
import time
import os
import socketserver
import threading
import http.server


class ThreadedHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        file = open("./http/HomePage.html", "r")
        self.wfile.write(bytes(file.read(), "utf-8"))
        address = self.client_address
        data = "GET request version: " + self.request_version
        log(address, data)
    
    def do_HEAD(self):
      self.send_response(200)
      self.send_header("Content-type", "text/html")
      self.end_headers()

    def do_POST(self):
      self.send_response(200)
      self.send_header('Content-type', 'text/html')
      self.end_headers()
      content_length = int(self.headers['Content-Length'])
      post_data = self.rfile.read(content_length)
      post_data = "Data: " + post_data.decode("utf-8")
      data = "POST request version: " + self.request_version + "\nUser-Agent: " + self.headers['User-Agent'] + "\n"
      file = open("./http/HomePage.html", "r")
      self.wfile.write(bytes(file.read(), "utf-8"))
      address = self.client_address
      log(address, data + post_data)
                      

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
     pass

def log(address, data):
  sep = '-' * 50
  with open('./http/logs/http.log', 'a') as file:
    file.write('Time: {}\nIP: {}\nPort: {}\nRequest: {}\n'.format(time.ctime(), address[0], address[1], data))
    file.write(sep + '\n')


# Opens tcp port and listens for connections
def run_pot():
  print("Starting honeypot...")
  host = ''
  port = 80

  #server = http.server.HTTPServer((host, port), ThreadedHTTPRequestHandler)

  server = ThreadedHTTPServer((host, port), ThreadedHTTPRequestHandler)
  ip, port = server.server_address
  
  #server.serve_forever()

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
