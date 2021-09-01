
class GenesisBlock:
    def __init__(self):
        pass
    
    def genesis_block(self):
        return 'Genesis Block'


class TxPool:
    def __init__(self):
        self.txs=[]

    def add_tx(self, tx):
        self.txs.append(tx)
    
    def clear_txs(self):
        self.txs.clear()
    
    def get_txs(self):
        return self.txs