import json
from time import time
from hashlib import sha256
import binascii

class Block:
    def __init__(self):
        self.txs = []
        genesis = self.genesis_block()
        self.chain = [genesis]

    def get_chain(self):
        return self.chain

    def new_block(self):
        pooled_txs = self.get_txs()
        if len(pooled_txs) == 0:
            pass
        else:
            prev_block_str = json.dumps(self.chain[-1], sort_keys=True)
            prev_hash=binascii.hexlify(sha256(prev_block_str.encode('utf-8')).digest()).decode('ascii')
            d = {
                'timestamp' : time(),
                'transactions': list(map(json.dumps, pooled_txs)),
                'previous_block': prev_hash,
            }
            d['nonce'] = self.block_pow(json.dumps(d),5)
            self.chain.append(d)
            self.clear_txs()

    def genesis_block(self):
        genesis_nonce = self.block_pow('genesis', 5)
        d = {'txs':[],'prev_hash':'GenesisBlock','nonce':genesis_nonce}
        return d
    
    def block_pow(self,msg,difficulty):
        i = 0
        suffix = '0' * difficulty
        while True:
            nonce = str(i)
            digest = binascii.hexlify(sha256((msg + nonce).encode('utf-8')).digest()).decode('ascii')
            if digest.endswith(suffix):
                return nonce
            i += 1

    def add_tx(self, tx):
        self.txs.append(tx)
    
    def clear_txs(self):
        self.txs.clear()
    
    def get_txs(self):
        return self.txs
