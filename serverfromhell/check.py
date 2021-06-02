import subprocess
import time

IP='10.10.46.54'

f = open('times', 'w')

for j in range(2500,4501):
    start = time.process_time()
    cmd="telnet {} {}".format(IP, j)
    try:
        op = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
    except Exception as e:
        pass
    f.write((str)(time.process_time() - start))
    # print(time.process_time() - start)
    # exit(1)

f.close()