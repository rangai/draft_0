import sys
import json
from transceiver import (
    send,
    MSG_TX,
    SHUTDOWN,
)

MY_HOST = '127.0.0.1'
MY_PORT = sys.argv[1]
MY_PORT = int(MY_PORT)

print('MY_HOST:', MY_HOST)
print('MY_PORT:', MY_PORT)

TEST_HOST='127.0.0.1'

while True:
    msg_type = int(input('msg_type:'))
    if msg_type == SHUTDOWN:
        shutdown=json.dumps({'msg_type':SHUTDOWN, 'sender':MY_PORT, 'content':0})
        send(MY_PORT, shutdown)
        break
    elif msg_type == MSG_TX:
        to_port = int(input('to_port:'))
        value = int(input('value:'))
        tx_json=json.dumps({'msg_type':msg_type, 'sender':MY_PORT, 'content':value})
        send(to_port, tx_json)
