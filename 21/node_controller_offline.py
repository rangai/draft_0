from blockchain import Block

b = Block()

while True:
    cmd = int(input('cmd:'))
    if cmd == 0:
        txs = b.get_txs()
        print(txs)
    elif cmd == 1:
        sender = input('sender:')
        receiver = input('receiver:')
        value = int(input('value:'))
        t = {'sender':sender, 'receiver':receiver, 'value':value}
        b.add_tx(t)
    elif cmd == 2:
        b.clear_txs()
    elif cmd == 3:
        my_block_chain = b.get_chain()
        print(my_block_chain)
    elif cmd == 4:
        b.new_block()
    elif cmd == 5:
        print(b.is_valid_chain())
    elif cmd == 9:
        break