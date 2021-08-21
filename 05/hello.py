import socket

my_host='127.0.0.1'
my_port=50092
the_other_host='127.0.0.1'
the_other_port=50090

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind((my_host, my_port))

my_socket.connect((the_other_host, the_other_port))
my_socket.sendall('hello'.encode('utf-8'))

content=my_socket.recv(4096)
print(content)