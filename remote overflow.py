import random
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.1",53))
d = []
for i in range(100):
	b =random.choice(str("AaBbCcDdEeFf123456789"))
	c =random.choice(str("AaBbCcDdEeFf123456789"))
	b = (str("0x")+str(b)+str(c)+",")
	print("done") 
	d.append(b) 
print(d)
print("sending")
s.sendall(d)
print("sent")

print(d)
s.close()

