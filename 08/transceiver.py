import socket

BUFSIZE=4096

def receiver(my_host, my_port):
    r_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    r_socket.bind((my_host, my_port))
    
    r_socket.listen()
    while True:
        soc, addr = r_socket.accept()
        msg = soc.recv(BUFSIZE)
        msg = msg.decode('utf-8')
        print('received: ' + msg)
        if msg == 'quit':
            break
    
    r_socket.close()

def sender(to_host, to_port, msg):
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.connect((to_host, to_port))
    s_socket.sendall(msg.encode('utf-8'))
    if msg=='quit':
        s_socket.close()