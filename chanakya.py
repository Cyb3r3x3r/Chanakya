# Copyright Cyb3r3x3r - Indian Cyber Ghosts

from re import search, sub
import requests
import socket
import os
import sys
import whois

w = '\033[1;97m'
g = '\033[1;32m'
r = '\033[1;31m'
y = '\033[1;33m'
e = '\033[1;m'

# This program is free to modify and develop
# Add your own ideas to it....but don't steal it
# atleast mention my name .. Cyb3r3x3r

Version = '0.1.6'

class chanakya:
    def __init__(self):
        self.clscr()
        self.logo()
        self.help()
        print('')
        victim = str(input('{}[?] Enter the target url{} > '.format(y,e)))
        try:
            if victim.startswith('http://'):
                victim = victim.replace('http://','')
            elif victim.startswith('https://'):
                victim = victim.replace('https://','')
        except:
            pass
        print('{} [~] Starting getting informations ...... {}'.format(g,e))
        ip = socket.gethostbyname(victim)
        print('{} [+] IP Address = {}{}'.format(g,ip,e))
        print('')
        print('{} [~] Getting robots.txt.....be patient {}'.format(y,e))
        try:
            self.robots(victim)
        except:
            print('{} [-] looks like robots.txt can\'t be retrieved{}'.format(r,e))
        print('')
        self.honey(ip)
        print('')
        print('{} [~] Scanning port with nmap scanner....{}'.format(y,e))
        self.portscan(ip)
        print('')
        self.whois(victim)
        print('{} [!] Done Getting Info....Exitting....{}'.format(w,e))
    def logo(self):
        print("""{}
  _______   __                              __                    
 |   _   | |  |--. .---.-. .-----. .---.-. |  |--. .--.--. .---.-.
 |.  1___| |     | |  _  | |     | |  _  | |    <  |  |  | |  _  |
 |.  |___  |__|__| |___._| |__|__| |___._| |__|__| |___  | |___._|
 |:  1   |                                         |_____|        
 |::.. . |  Developed By Cyb3r3x3r - ICG                                                      
 `-------'                                                        
                                                                  
{}""".format(y,e))
        
    def clscr(self):
        lin = 'clear'
        win = 'cls'
        os.system([lin,win][os.name == 'nt'])

    def help(self):
        print('{}----------------------------------------{}'.format(y,e))
        print('{}[!]  Usage :    python chanakya.py {}'.format(y,e))

    def robots(self,victim):
        try:
            robot = requests.get('http://' + victim + '/robots.txt').text
            print('{}--------------------------------------{}'.format(y,e))
            if '<title>' in robot:
                print('{} [-] Looks like there is a problem retrieving robots.txt {}'.format(r,e))
            else:
                print('{}  [+] Robots.txt retrieved {}'.format(g,e))
                print('{}{}{}'.format(g,robot,e))
        except:
            pass

    def portscan(self,ip):
        scan = requests.get('http://api.hackertarget.com/nmap/?q=' + ip).text
        result = sub(r'Starting[^<]*\)\.', '', scan)
        result = sub(r'Service[^<]*seconds', '', scan)
        print('{} [+] {}{}'.format(g,result,e))

    def honey(self,ip):
        print('{} [~] Checking Honeypot Probability from online source.........{}'.format(w,e))
        match = {"0.0": 0, "0.1": 10, "0.2": 20, "0.3": 30, "0.4": 40, "0.5": 50, "0.6": 60, "0.7": 70, "0.8": 80, "0.9": 90, "1.0": 10}
        try:
            gethoney = requests.get('https://api.shodan.io/labs/honeyscore/' + str(ip) + '?key=C23OXE0bVMrul2YeqcL7zxb6jZ4pj2by').text
            print('{} [+] HoneyPot Check Result = {}{}'.format(g,gethoney,e))
            print('{} [+] HoneyPot Probability Result = {}{}'.format(g,match[gethoney],e))
            check = float(gethoney)
            if check >= 0.0 and check <= 0.4:
                print('{}  [+] Looks like it is a REAL SYSTEM {}'.format(g,e))
            else:
                print('{}  [-] Oh! It is a HONEYPOT SYSTEM {}'.format(r,e))
        except:
            print('{}[-] It looks like HoneyPot Check can not be completed.{}'.format(r,e))

    def whois(self,url):
        print('{} [~] Doing Whois Lookup.......{}'.format(y,e))
        try:
            info = whois.whois(url)
            print('{}{}{}'.format(g,info,e))
        except Exception:
            print('{} [-] Some Error occurred while getting whois information..{}'.format(r,e))

cyb = chanakya()
cyb
