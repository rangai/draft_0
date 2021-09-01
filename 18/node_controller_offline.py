import sys
import json

from blockchain import TxPool

tp = TxPool()

while True:
    cmd = int(input('cmd'))
    if cmd == 0:
        txs = tp.get_txs()
        print(txs)
    elif cmd == 1:
        sender = input('sender')
        receiver = input('receiver')
        value = int(input('value'))
        t = {'sender':sender, 'receiver':receiver, 'value':value}
        tp.add_tx(t)
    elif cmd == 2:
        tp.clear_txs()
    elif cmd == 9:
        break