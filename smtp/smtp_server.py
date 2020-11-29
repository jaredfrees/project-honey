import smtplib
import logging
# Author: Brian Fissel

def prompt(prompt):
    return input(prompt).strip()

logging.basicConfig(filename='./smtp/smtp_dir/smtp.log', level=logging.DEBUG)

fromaddr = prompt("From: ")
toaddr  = prompt("To: ").split()
print("Enter message, end with ^D (Unix) or ^Z (Windows):")


msg = ("From: %s\r\nTo: %s\r\n\r\n"
       % (fromaddr, ", ".join(toaddr)))
while True:
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    msg = msg + line

server = smtplib.SMTP('127.0.0.1', 25)
print("Email Sent!")

