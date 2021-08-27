import socket
import json

BUFSIZE=4096

MSG_CONTENT=0
BROADCAST_NODES=1
SHUTDOWN = 9

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
        msg_type, sender, content = parse(msg)
        if msg_type == MSG_CONTENT:
            if sender not in connected_nodes:
                connected_nodes.add(sender)
                node_msg_json=json.dumps({'msg_type':1, 'sender':my_port, 'content':list(connected_nodes)})
                connected_nodes = broadcast(node_msg_json)
                print('new node:', sender, '| connected_nodes:', connected_nodes)
            print(sender, '->', my_port, '| Content:', content)
        elif msg_type == BROADCAST_NODES:
            connected_nodes = set(content)
            print('connected_nodes:', connected_nodes)
        elif msg_type == SHUTDOWN and sender == my_port:
            break

        soc.close()
    
    r_socket.close()

def send(to_port, msg):
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.connect((TEST_HOST, to_port))
    s_socket.sendall(msg.encode('utf-8'))

def parse(msg):
    msg_dict = json.loads(msg)
    msg_type=msg_dict['msg_type']
    sender=int(msg_dict['sender'])
    content=msg_dict['content']
    return (msg_type, sender, content)

def broadcast(msg):
    msg_type, sender, nodes = parse(msg)
    current_nodes=[]
    for n in nodes:
        try:
            send(n, msg)
            current_nodes.append(n)
        except:
            pass
    return set(current_nodes)

