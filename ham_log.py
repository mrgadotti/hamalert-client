from telnetlib import Telnet
import time
import re

print("Connect telnet")
tn = Telnet("hamalert.org", 7300)
time.sleep(1)
print("Start login")
tn.read_until(b"\n")
time.sleep(0.5)
tn.read_until(b":")
time.sleep(0.5)
tn.write(b"pp5mgt" + b"\n")
time.sleep(1)
tn.read_until(b"\n")
tn.read_until(b":")
tn.write(b"password" + b"\n")
time.sleep(1)
tn.read_until(b"\n")
print(tn.read_until(b"\n").decode("utf-8").rstrip("\n").replace(">", ""))
while True:
    data = tn.read_until(b"\n")
    data = re.sub("\s\s+" , " ", str(data.decode("utf-8")))
    data = data.replace("\r\n", "")
    with open('log.txt', 'a') as file:
        file.write(data + '\r\n')
    print(data)
