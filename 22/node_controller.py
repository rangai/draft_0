import sys
import json
from transceiver import *

MY_HOST = '127.0.0.1'
MY_PORT = sys.argv[1]
MY_PORT = int(MY_PORT)

while True:
    cmd = int(input('cmd:'))
    if cmd == GET_TXS:
        get_txs=json.dumps({'msg_type':GET_TXS, 'sender':MY_PORT, 'content':''})
        send(MY_PORT, get_txs)
    elif cmd == NEW_TX:
        sender = input('sender:')
        receiver = int(input('receiver:'))
        value = int(input('value:'))
        tx = {'sender':sender, 'receiver':receiver, 'value':value}
        tx_msg=json.dumps({'msg_type':NEW_TX, 'sender':MY_PORT, 'content':tx})
        send(receiver, tx_msg)
    elif cmd == GET_CHAIN:
        get_chain = json.dumps({'msg_type':GET_CHAIN, 'sender':MY_PORT, 'content':''})
        send(MY_PORT, get_chain)
    elif cmd == NEW_BLOCK:
        new_block = json.dumps({'msg_type':NEW_BLOCK, 'sender':MY_PORT, 'content':''})
        send(MY_PORT, new_block)
    elif cmd == CHAIN_VALIDATION:
        is_valid = json.dumps({'msg_type':CHAIN_VALIDATION, 'sender':MY_PORT, 'content':''})
        send(MY_PORT, is_valid)
    elif cmd == SHUTDOWN:
        shutdown=json.dumps({'msg_type':SHUTDOWN, 'sender':MY_PORT, 'content':''})
        send(MY_PORT, shutdown)
        break