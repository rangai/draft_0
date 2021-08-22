import json
from transceiver import sender

MY_HOST= '127.0.0.1'
MY_PORT= 50090

print('MY_HOST:', MY_HOST)
print('MY_PORT:', MY_PORT)

while True:
    to_host = input('to_host:')
    to_port = int(input('to_port:'))
    my_msg = input('msg: ')
    msg_dict={'sender':MY_PORT, 'content':my_msg}
    msg_json=json.dumps(msg_dict)
    sender(to_host, to_port, msg_json)
    if my_msg == 'quit':
        break
