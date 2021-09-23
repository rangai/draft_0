class Tx:
    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs
    
    def to_dict(self):
        d = {
            'inputs':list(map(TxInput.to_dict, self.inputs)),
            'outputs':list(map(TxOutput.to_dict, self.outputs))
        }
        return d
    
    def is_enough_input(self, fee):
        total_inputs = sum(i.tx['outputs'][i.output_id]['value'] for i in self.inputs)
        total_outputs = sum(int(o.value) for o in self.outputs) + int(fee)
        delta = total_inputs - total_outputs
        if delta >= 0:
            return True
        else:
            return False

class CoinbaseTx:
    def __init__(self, recipient, value):
        self.inputs = []
        self.outputs = [TxOutput(recipient, value)]
    
    def to_dict(self):
        return super().to_dict()


class TxOutput:
    def __init__(self, recipient, value):
        self.recipient = recipient
        self.value = value

    def to_dict(self):
        d = {
            'recipient':self.recipient,
            'value':self.value
        }
        return d


class TxInput:
    def __init__(self, tx, output_id):
        self.tx = tx
        self.output_id = output_id

    def to_dict(self):
        d = {
            'tx':self.tx,
            'output_id':self.output_id
        }
        return d