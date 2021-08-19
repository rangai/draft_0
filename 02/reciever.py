import socket

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
my_host=s.getsockname()[0]
print(my_host)
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_port=int(input('my port:'))
my_socket.bind((my_host, my_port))
my_socket.listen()
conn, addr = my_socket.accept()
print(conn)
print(addr)