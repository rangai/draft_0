import socket
import json

from blockchain import Block

BUFSIZE=4096

GET_TXS=0
NEW_TX=1
BROADCAST_NODES=2
BROADCASTED_TX=3
GET_CHAIN=4
NEW_BLOCK=5
CHAIN_VALIDATION=6
SHUTDOWN = 9

TEST_HOST='127.0.0.1'

b = Block()

def receive(my_port):
    connected_nodes = set()
    connected_nodes.add(my_port)

    r_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    r_socket.bind((TEST_HOST, my_port))
    
    r_socket.listen()
    while True:
        soc, addr = r_socket.accept()
        data_sum = ''
        while True:
            data = soc.recv(BUFSIZE)
            data_sum = data_sum + data.decode('utf-8')
            if not data:
                break
        
        msg = data_sum
        msg = parse(msg)
        if msg[0] == SHUTDOWN and msg[1] == my_port:
            soc.close()
            break
        connected_nodes = read_msg(my_port, msg, connected_nodes)
        soc.close()
    
    r_socket.close()

def read_msg(my_port, msg, connected_nodes):
    msg_type = msg[0]
    sender = msg[1]
    txs = b.get_txs()
    if sender not in connected_nodes:
        connected_nodes.add(sender)
        connected_nodes_list = list(connected_nodes)
        node_msg_json=json.dumps({'msg_type':BROADCAST_NODES, 'sender':my_port, 'content':connected_nodes_list})
        connected_nodes = broadcast(node_msg_json, my_port, connected_nodes_list)
        print('new node:', sender, '| connected_nodes:', connected_nodes)
    
    if msg_type == GET_TXS:
        print(txs)
    elif msg_type == NEW_TX:
        tx = msg[2]
        if tx not in txs:
            b.add_tx(tx)
            tx_json = json.dumps({'msg_type':BROADCASTED_TX, 'sender': my_port, 'content': tx})
            broadcast(tx_json, my_port, connected_nodes)
            print('Transactions:', txs)
    elif msg_type == BROADCAST_NODES:
        content = msg['content']
        connected_nodes = set(content)
        print('Connected_nodes:', connected_nodes)
    elif msg_type == BROADCASTED_TX:
        content = msg['content']
        for t in content:
            if t not in txs:
                b.add_tx(t)
        print('Transactions:', txs)
    elif msg_type == GET_CHAIN:
        my_block_chain = b.get_chain()
        print(my_block_chain)
    elif msg_type == NEW_BLOCK:
        b.new_block()
        new_block_chain = b.get_chain()
        print(new_block_chain)
    elif msg_type == CHAIN_VALIDATION:
        is_valid = b.is_valid_chain()
        print(is_valid)
        
    return connected_nodes

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

