import socket
import json
import copy

BUFSIZE=4096

BROADCAST_NODES=0
MSG_CONTENT=1

TEST_HOST='127.0.0.1'


def receive(my_port):
    connected_nodes = set()
    connected_nodes.add(my_port)
    r_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    r_socket.bind((TEST_HOST, my_port))
    
    r_socket.listen()
    while True:
        soc, addr = r_socket.accept()
        msg = soc.recv(BUFSIZE)
        msg = msg.decode('utf-8')
        msg_type, sender, content = interpret_msg(msg)
        if msg_type == 0:
            if sender not in connected_nodes:
                print('new node:', sender)
                connected_nodes.add(sender)
                node_msg_dict={'msg_type':1, 'sender':my_port, 'content':list(connected_nodes)}
                node_msg_json=json.dumps(node_msg_dict)
                broadcast(node_msg_json)
            print('connected_nodes:', connected_nodes)
            print('Sender:', sender, '| Content:', content)
            if content == 'quit':
                break
        elif msg_type == 1:
            connected_nodes = set(content)
            print('connected_nodes:', list(connected_nodes))

        soc.close()
    
    r_socket.close()

def send(to_port, msg):
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.connect((TEST_HOST, to_port))
    s_socket.sendall(msg.encode('utf-8'))

def interpret_msg(msg):
    msg_dict = json.loads(msg)
    msg_type=msg_dict['msg_type']
    sender=int(msg_dict['sender'])
    content=msg_dict['content']
    return (msg_type, sender, content)

def broadcast(msg):
    msg_type, sender, nodes = interpret_msg(msg)
    for n in nodes:
        if n != sender:
          send(n, msg)

