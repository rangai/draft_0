import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
your_host=input('your host:')
your_port=input('your port:')
s.connect((your_host, int(your_port)))
s.sendall('hello'.encode('utf-8'))
s.close()