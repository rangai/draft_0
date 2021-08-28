import socket
import json

BUFSIZE=4096

MSG_TX=0
BROADCAST_NODES=1
BROADCASTED_TX=2
SHUTDOWN = 9

TEST_HOST='127.0.0.1'


def receive(my_port):
    connected_nodes = set()
    connected_nodes.add(my_port)

    transactions=[]

    r_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    r_socket.bind((TEST_HOST, my_port))
    
    r_socket.listen()
    while True:
        soc, addr = r_socket.accept()
        msg = soc.recv(BUFSIZE)
        msg = msg.decode('utf-8')
        msg = parse(msg)
        if msg[0] == SHUTDOWN and msg[1] == my_port:
            soc.close()
            break
        transactions, connected_nodes = read_msg(my_port, msg, transactions, connected_nodes)
        soc.close()
    
    r_socket.close()

def read_msg(my_port, msg, transactions, connected_nodes):
    msg_type, sender, content = msg
    if msg_type == MSG_TX:
        if sender not in connected_nodes:
            connected_nodes.add(sender)
            connected_nodes_list = list(connected_nodes)
            node_msg_json=json.dumps({'msg_type':BROADCAST_NODES, 'sender':my_port, 'content':connected_nodes_list})
            connected_nodes = broadcast(node_msg_json, my_port, connected_nodes_list)
            print('new node:', sender, '| connected_nodes:', connected_nodes)
        tx = {'from':sender, 'to':my_port, 'content':content}
        if tx not in transactions:
            transactions.append(tx)
            tx_json = json.dumps({'msg_type':BROADCASTED_TX, 'sender': my_port, 'content': transactions})
            broadcast(tx_json, my_port, connected_nodes)
            print('Transactions:', transactions)
    elif msg_type == BROADCAST_NODES:
        connected_nodes = set(content)
        print('Connected_nodes:', connected_nodes)
    elif msg_type == BROADCASTED_TX:
        for t in content:
            if t not in transactions:
                transactions.append(t)
        print('Transactions:', transactions)
        
    return (transactions, connected_nodes)

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

def broadcast(msg, sender, nodes):
    current_nodes=[sender]
    for n in nodes:
        if n != sender:
            try:
                send(n, msg)
                current_nodes.append(n)
            except:
                pass
    return set(current_nodes)

