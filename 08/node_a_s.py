from transceiver import sender

MY_HOST= '127.0.0.1'
MY_PORT= 50090

print('MY_HOST:', MY_HOST)
print('MY_PORT:', MY_PORT)

to_host = input('to_host:')
to_port = int(input('to_port:'))

while True:
    to_host = input('to_host:')
    to_port = int(input('to_port:'))
    sender(to_host, to_port, str(MY_PORT))
    my_msg = input('msg: ')
    sender(to_host, to_port, my_msg)
    if my_msg == 'quit':
        break
