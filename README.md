# Project Honey

* To run the program you will need to install pyftpdlib which can be done with the command: `pip3 install pyftpdlib`<br/>
* Run program: `python .\main_menu.py`<br/>
* After running you can then select which type of server you would like to run.<br/>
* After selecting the server is now running and you can interact with it.<br/>
* The TCP connection is on port 25565, the SSH is on port 2222, the FTP is port 21, and the HTTP is on port 80.<br/>
* Each server has how you can test it at the top of the file, some are command line inputs or other actions such as opening your browser to test these servers.<br/>
* You can end the program by using ctrl c to exit the program.

<br/><br/>
Team members:
Jared Frees,
Zach Cusick,
Brian Fissel

### Motivation
We want to focus on making a honeypot because we want to set some up on our own networks to see if any hackers are trying to get information about our networks or break in somehow. I think it would be interesting to detect internet bots scraping the web and see where they come from based on IP.

### Problem Statement
We are going to design a honeypot to detect malicious actors spying on a network. The challenges we face are protecting a network from hackers looking for vulnerabilities. 

### The Plan
We will create a honeypot most likely in Python that will mimic real network services. Some services we will probably recreate are HTTP, FTP, SSH, and SMTP.

