# Project Honey
<br/>
Team members: Jared Frees, Zach Cusick, Brian Fissel
<br/>

### Documentation
* To run the program you will need to install pyftpdlib which can be done with the command: `pip3 install pyftpdlib`<br/>
* Run program: `python .\main_menu.py`<br/>
* After running you can then select which type of server you would like to run by typing the specified number.<br/>
* After selecting, the server is now running and you can interact with it.<br/>
* The TCP connection is on port 25565, the SSH is on port 2222, the FTP is port 21, and the HTTP is on port 80.<br/>
* For testing each server you can either use the command line, your browser, or use `./porttest.ps1` or `test_client.py` <br/>
* You can end the program with CTRL-C to exit the program.

<br/>

#### Testing the Servers:
* FTP:
    * ftp \<ip-address> \<port-number>
    * ftp 127.0.0.1 21
* TCP:
    * nc \<ip-address> \<port-number>
    * nc 127.0.0.1 25565
* HTTP:
    * Browser: http://127.0.0.1
* SSH:
    * ssh -p \<port> \<ip-address>
    * ssh -p 2222 127.0.0.1
