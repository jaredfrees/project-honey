# INSTALL: pip3 install pyftpdlib
# Testing command: ftp <ip-address> <port-number>
#                  ftp 127.0.0.1 21

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer
import configparser
import logging

# Get config
config = configparser.ConfigParser()
config.read('config.ini')
section = 'DEFAULT'
FTP_PORT = config[section]['ftp_port']
FTP_USER = config[section]['ftp_user']
FTP_PASSWORD = config[section]['ftp_password']
FTP_DIR = config[section]['ftp_directory']
####################


authorizer = DummyAuthorizer()
authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIR, perm="elradfmw")
authorizer.add_anonymous(FTP_DIR, perm="elr")

handler = FTPHandler
handler.authorizer = authorizer
#handler.log_prefix = 'XXX [%(username)s]@%(remote_ip)s'

handler.banner = "Welcome to the FTP Server :)"

logging.basicConfig(filename='./logs/ftp.log', level=logging.DEBUG)

server = ThreadedFTPServer(('127.0.0.1', FTP_PORT), handler)
server.max_cons = 10
server.max_cons_per_ip = 5

server.serve_forever()

