# Copyright Cyb3r3x3r - Indian Cyber Ghosts
# Version = v0.1.8
import sys
import os
w = '\033[1;97m'
g = '\033[1;32m'
r = '\033[1;31m'
y = '\033[1;33m'
e = '\033[1;m'

if sys.version[0] > '2':
    pass
else:
    print("[{}WARNING{}] You are using Python 2...Install Python 3 to use Chanakya".format(r,r))
    print("[{}INFO{}] A version for Python 2 may be avaiable in future".format(g,g))
    sys.exit()

import re
import time
try:
    import requests
except:
    print('[{}INFO{}]Requests Not found. Please install all module from requirements'.format(y,y))
    sys.exit()
try:
    import socket
except:
    print('[{}INFO{}]Socket not found. Please install all module from requirements'.format(y,y))
    sys.exit()
try:
    import whois
except:
    print('[{}INFO{}]Whois not found. Please install all module from requirements'.format(y,y))
    sys.exit()
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# This program is free to modify and develop
# Add your own ideas to it....but don't try to own in....atleast mention my name .. Cyb3r3x3r
# http://www.sniperhacks.wordpress.com/

Version = 'v0.1.81'

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
        time.sleep(3)
        ip = socket.gethostbyname(victim)
        print('{} [+] IP Address = {}{}'.format(g,ip,e))
        print('')
        self.httpheaders(victim)
        print('')
        self.check_joom(victim)
        print('')
        self.wp_check(victim)
        print('')
        self.check_drup(victim)
        print('')
        print('{} [~] Getting robots.txt.....be patient {}'.format(y,e))
        try:
            self.robots(victim)
        except:
            print('{} [-] looks like robots.txt can\'t be retrieved{}'.format(r,e))
        print('')
        #self.honey(ip)
        #print('')
        #print('{} [~] Scanning port with nmap scanner....{}'.format(y,e))
        #self.portscan(ip)
        print('')
        self.whois(victim)
        print('')
        print('')
        print('{} [~] Sending spider to dump links.....{}'.format(y,e))
        self.spider(victim)
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
            robot = requests.get('https://' + victim + '/robots.txt',timeout=10, verify=False).text
            print('{}--------------------------------------{}'.format(y,e))
            if '<title>' in robot:
                print('{} [-] Looks like robots.txt is not available on this URL {}'.format(r,e))
            else:
                print('{}  [+] Robots.txt retrieved {}'.format(g,e))
                print('{}{}{}'.format(g,robot,e))
        except:
            pass

    def portscan(self,ip):
        try:
            scan = requests.get('http://api.hackertarget.com/nmap/?q=' + ip).text
            result = re.sub(r'Starting[^<]*\)\.', '', scan)
            result = re.sub(r'Service[^<]*seconds', '', scan)
            print('{}[+]{}{}'.format(g,result,e))
        except:
            print('{}[-]Port Scan can not be completed....Skipping...{}'.format(r,e))
            time.sleep(2)

    def honey(self,ip):
        print('{} [~] Checking Honeypot Probability from online source.........{}'.format(w,e))
        match = {"0.0": 0, "0.1": 10, "0.2": 20, "0.3": 30, "0.4": 40, "0.5": 50, "0.6": 60, "0.7": 70, "0.8": 80, "0.9": 90, "1.0": 10}
        try:
            gethoney = requests.get('https://api.shodan.io/labs/honeyscore/' + str(ip) + '?key=C23OXE0bVMrul2YeqcL7zxb6jZ4pj2by',timeout=10, verify=False).text
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
            print('\033[1;32m[+] Domain Name = ',info.domain_name)
            print('[+] Registrar = ',info.registrar)
            print('[+] Whois Server = ',info.whois_server)
            print('[+] Referral Url = ',info.referral_url)
            print('[+] Creation Date = ',info.creation_date)
            print('[+] Expiration Date = ',info.expiration_date)
            print('[+] Name Servers = ',info.name_servers)
            print('[+] Emails = ',info.emails[1])
            print('[+] DNSSEC = ',info.dnssec)
            print('[+] Name = ',info.name)
            print('[+] Organization = ',info.org)
            print('[+] Address = ',info.address)
            print('[+] City = ',info.city)
            print('[+] State = ',info.state)
            print('[+] Zipcode = ',info.zipcode)
            print('[+] Country = \033[1;m',info.country)
        except Exception:
            print('{} [-] Some Error occurred while getting whois information..{}'.format(r,e))

    def check_joom(self,url):
        try:
            print('{} [~] Checking Joomla Installation.......{}'.format(y,e))
            time.sleep(2)
            joom = requests.get('http://' + url,timeout=5).text
            if '/administrator' in joom or '/joomla/' in joom or 'content=\"Joomla!' in joom:
                print('{}[+] Joomla Installation Found...{}'.format(g,e))
            else:
                print('{}[!] No Joomla Installation Found...{}'.format(y,e))
        except Exception:
            print("{}[-] Some error Occurred....Continuing....{}".format(r,e))

    def wp_check(self,url):
        try:
            print('{} [~] Checking Wordpress Installation.......{}'.format(y,e))
            time.sleep(2)
            wp = requests.get('http://' + url,timeout=5).text
            if '/wp-admin' in wp or '/wp-content' in wp:
                print('{}[+] Wordpress Installation Found...{}'.format(g,e))
                print('{}[!] You can scan this website with CybScan WP Scanner.{}'.format(y,e))
                print('{}[!] Check at - https://github.com/cyb3r3x3r/cybscan{}'.format(y,e))
                time.sleep(1)
            else:
                print('{}[!] No Wordpress Installation Found...{}'.format(y,e))
        except Exception:
            print("{}[-] Some error Occurred....Continuing....{}".format(r,e))


    def check_drup(self,url):
        try:
            print('{} [~] Checking Drupal Installation.......{}'.format(y,e))
            time.sleep(2)
            drupal = requests.get('http://' + url,timeout=5).text
            if '/user' in drupal:
                print('{}[+] Drupal Installation Found...{}'.format(g,e))
            else:
                print('{}[!] No Drupal Installation Found...{}'.format(y,e))
        except Exception:
            print("{}[-] Some error Occurred....Continuing....{}".format(r,e))

    def spider(self,url):
        try:
            info = requests.get('http://api.hackertarget.com/pagelinks/?q=https://' + url).text
            print('{} [+] Links retrieved >> {}'.format(y,e))
            print('')
            time.sleep(2)
            print('{}{}{}'.format(g,info,e))
        except:
            print('{} [-]Looks like there is a problem retrieving links..{}'.format(r,e))
            
    def httpheaders(self,url):
        checker = 'https://api.hackertarget.com/httpheaders/?q='+url
        info = requests.get(checker).text
        print('{}[!] HTTP headers retrieved >> {}'.format(y,e))
        print('')
        print('{}[+] {}{}'.format(g,info,e))
cyb = chanakya()
cyb
