import socket

my_host='127.0.0.1'
my_port=50092
the_other_host='127.0.0.1'
the_other_port=50090

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind((my_host, my_port))

content= ''
my_socket.connect((the_other_host, the_other_port))
while True:
    my_msg = input('my new msg:')
    content += my_msg + ' '
    print('now: ' + content)
    my_socket.sendall(my_msg.encode('utf-8'))
    the_others_msg=my_socket.recv(4096)
    content += the_others_msg.decode('utf-8') + ' '
    print('now: '+ content)