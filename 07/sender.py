import socket

to_host='127.0.0.1'
to_port=50090

while True:
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.connect((to_host, to_port))
    msg = input('msg: ')
    s_socket.sendall(msg.encode('utf-8'))
    if msg=='quit':
        s_socket.close()
        break