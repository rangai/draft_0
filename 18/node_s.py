import sys
import json
from transceiver import (
    Transceiver,
    MSG_TX,
    SHUTDOWN,
    GENESIS_BLOCK,
)
from blockchain import (
    GenesisBlock,
    TxPool,
)

MY_HOST = '127.0.0.1'
MY_PORT = sys.argv[1]
MY_PORT = int(MY_PORT)

print('MY_HOST:', MY_HOST)
print('MY_PORT:', MY_PORT)

TEST_HOST='127.0.0.1'

s=Transceiver()

while True:
    msg_type = int(input('msg_type:'))
    if msg_type == SHUTDOWN:
        shutdown=json.dumps({'msg_type':SHUTDOWN, 'sender':MY_PORT, 'content':0})
        s.send(MY_PORT, shutdown)
        break
    elif msg_type == MSG_TX:
        to_port = int(input('to_port:'))
        value = int(input('value:'))
        tx_json=json.dumps({'msg_type':msg_type, 'sender':MY_PORT, 'content':value})
        s.send(to_port, tx_json)
    elif msg_type == GENESIS_BLOCK:
        g=GenesisBlock()
        genesis_block = json.dumps({'msg_type':msg_type, 'sender':MY_PORT, 'content':g.genesis_block()})
        s.send(MY_PORT, genesis_block)

