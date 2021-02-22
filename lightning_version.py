def lighning_hash(data):
    return data + '*'


class Block:
    def __init__(self, data, hash, last_hash):
        self.data = data
        self.hash = hash
        self.last_hash = last_hash


class Blockchain:
    def __init__(self):
        genesis = Block('gen_data', 'gen_hash', 'gen_last_hash')
        self.chain = [genesis]

    def add_block(self, data):
        last_hash = self.chain[-1].hash
        hash = lighning_hash(data+last_hash)
        block = Block(data, hash, last_hash)

        self.chain.append(block)


blockchain = Blockchain()
blockchain.add_block('one')
blockchain.add_block('two')
blockchain.add_block('three')

for block in blockchain.chain:
    print(block.__dict__)
