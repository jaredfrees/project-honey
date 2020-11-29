# Author: Jared Frees
# INSTALL: pip3 install pyftpdlib
# Testing command: ftp <ip-address> <port-number>
#                  ftp 127.0.0.1 21
"""
This is a medium/high interaction FTP honeypot meaning the attacker
will gain "fake" access to the computer system over FTP. We set up
a decoy folder where they can see some test files and make real FTP commands.
Making this a high interaction honeypot allows us to see how a real
attacker would act and what commands would be run when they think they
are inside a real computer system. This allows for more in depth analysis of
an attackers methods.
"""

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer
import configparser
import logging

# Get config
config = configparser.ConfigParser()
config.read('./ftp/config.ini')
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

logging.basicConfig(filename='./ftp/logs/ftp.log', level=logging.DEBUG)

server = ThreadedFTPServer(('127.0.0.1', FTP_PORT), handler)
server.max_cons = 10
server.max_cons_per_ip = 5

server.serve_forever()

