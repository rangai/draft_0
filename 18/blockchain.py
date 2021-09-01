from hashlib import sha256
import binascii

class GenesisBlock:
    def __init__(self):
        self.nonce = self.pow('genesis',5) 
    
    def genesis_block(self):
        d = {'txs':[],'previous_block_hash':'GenesisBlock','nonce':self.nonce}
        return d
    
    def pow(self,msg,difficulty):
        i = 0
        suffix = '0' * difficulty
        while True:
            nonce = str(i)
            digest = binascii.hexlify(sha256((msg + nonce).encode('utf-8')).digest()).decode('ascii')
            if digest.endswith(suffix):
                return nonce
            i += 1


class TxPool:
    def __init__(self):
        self.txs=[]

    def add_tx(self, tx):
        self.txs.append(tx)
    
    def clear_txs(self):
        self.txs.clear()
    
    def get_txs(self):
        return self.txs