import json
import copy
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
            prev_hash=self.get_hash(prev_block_str)
            d = {
                'timestamp' : time(),
                'txs': list(map(json.dumps, pooled_txs)),
                'prev_hash': prev_hash,
            }
            d['nonce'] = self.block_pow(json.dumps(d),5)
            self.chain.append(d)
            self.clear_txs()

    def genesis_block(self):
        genesis_nonce = self.block_pow('genesis', 5)
        d = {'txs':[],'prev_hash':'GenesisBlock','nonce':genesis_nonce}
        return d
    
    def block_pow(self, msg, difficulty):
        i = 0
        suffix = '0' * difficulty
        while True:
            nonce = str(i)
            digest = self.get_hash(msg+nonce)
            if digest.endswith(suffix):
                return nonce
            i += 1

    def add_tx(self, tx):
        self.txs.append(tx)
    
    def clear_txs(self):
        self.txs.clear()
    
    def get_txs(self):
        return self.txs

    def get_hash(self,msg):
        return binascii.hexlify(sha256(msg.encode('utf-8')).digest()).decode('ascii')
    
    def is_valid_block(self, prev_block_hash, block, difficulty=5):
        suffix = '0' * difficulty
        block_copy = copy.deepcopy(block)
        nonce = str(block_copy['nonce'])
        del block_copy['nonce']
        msg = json.dumps(block_copy)
        if block['prev_hash'] != prev_block_hash:
            return False
        else:
            digest = self.get_hash(msg + nonce)
            if digest.endswith(suffix):
                return True
            else:
                return False

    def is_valid_chain(self):
        chain = self.get_chain()
        check_block = chain[0]
        i = 1
        while i < len(chain):
            block = chain[i]
            if self.is_valid_block(self.get_hash(json.dumps(check_block, sort_keys=True)), block) is not True:
                print(i)
                return False
            check_block = chain[i]
            i += 1

        return True

    def resolve_conflict(self, received_chain):
        if len(received_chain) > len(self.chain):
            if self.is_valid_chain(received_chain):
                self.chain = received_chain
