#### once we're on the box

su to paradox user using the same ftp password

now after running linpeas, we find that we can use this to do the exploit
https://book.hacktricks.xyz/linux-unix/privilege-escalation/nfs-no_root_squash-misconfiguration-pe

ssh -L 2049:127.0.0.1:2049 -i /home/srini/.ssh/id_rsa paradox@10.10.36.255

after this ^^ we would be able to mount the nfs on our local drive as root user and transfer/read files