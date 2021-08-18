import socket

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
my_ip=s.getsockname()
print(my_ip[0])