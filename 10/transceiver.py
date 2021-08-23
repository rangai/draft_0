import socket
import json

BUFSIZE=4096
NODES_BROADCAST=0
MSG_CONTENT=1

def receiver(my_host, my_port):
    connected_nodes=set()
    connected_nodes.add(my_port)
    r_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    r_socket.bind((my_host, my_port))
    
    r_socket.listen()
    while True:
        soc, addr = r_socket.accept()
        msg = soc.recv(BUFSIZE)
        msg = msg.decode('utf-8')
        sender, content = interpret_msg(msg)
        print('Sender:', sender, '| Content:', content)
        connected_nodes.add(sender)
        connected_nodes_list=list(connected_nodes)
        for n in connected_nodes_list:
            if n != my_port:
                print(n)
        
        if content == 'quit':
            break
        soc.close()
    
    r_socket.close()

def sender(to_host, to_port, msg):
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.connect((to_host, to_port))
    print(to_host,to_port, msg)
    s_socket.sendall(msg.encode('utf-8'))

def interpret_msg(msg):
    msg_dict = json.loads(msg)
    msg_type=msg_dict['msg_type']
    if msg_type == 0:
        sender=int(msg_dict['sender'])
        content=msg_dict['content']
        return (sender, content)
