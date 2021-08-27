import sys
import json
from transceiver import (
    send,
    MSG_CONTENT,
)

MY_HOST = '127.0.0.1'
MY_PORT = sys.argv[1]
MY_PORT = int(MY_PORT)

print('MY_HOST:', MY_HOST)
print('MY_PORT:', MY_PORT)

TEST_HOST='127.0.0.1'

while True:
    msg_type = MSG_CONTENT
    to_port = int(input('to_port:'))
    my_msg = input('msg: ')
    msg_dict={'msg_type':msg_type, 'sender':MY_PORT, 'content':my_msg}
    msg_json=json.dumps(msg_dict)
    send(to_port, msg_json)
    if my_msg == 'quit' and to_port == MY_PORT:
        break
