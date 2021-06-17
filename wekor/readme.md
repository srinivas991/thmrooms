export IP=10.10.127.132

sudo nmap -sS -sV -sC $IP
this gives us a basic idea of what ports are running, while exploring the http server on 80, we can run a full scan for all ports

sudo nmap -sS -p- $IP 

we've modified the /etc/hosts file to have the entry => `10.10.127.132 wekor.thm`

lets do a ffuf on the site
`ffuf -w /usr/share/seclists/Discovery/Web-Content/common.txt -u http://wekor.thm/FUZZ -e .php -t 50`

from the look of it, its an apache server..

and we have a robits.txt we got from the ffuf scan..
```
Disallow: /workshop/
Disallow: /root/
Disallow: /lol/
Disallow: /agent/
Disallow: /feed
Disallow: /crawler
Disallow: /boot
Disallow: /comingreallysoon
Disallow: /interesting
```

cat readme.md| grep isall | awk '{ print $NF }' | sed 's/^/http:\/\/wekor.thm/'

we got a URL from this `http://wekor.thm/it-next/`

ffuf -w "urls.txt:DOMAINS"  -w /usr/share/seclists/Discovery/Web-Content/common.txt -u DOMAINS/FUZZ -e .php -t 100