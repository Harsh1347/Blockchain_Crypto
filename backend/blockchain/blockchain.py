from backend.blockchain.block import Block


class Blockchain:
    """
    Blockchain: a public ledger of transactions.
    Implemented as a list of blocks - data sets of transaction
    """

    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        self.chain.append(Block.mine_block(self.chain[-1], data))

    def __repr__(self):
        return f"Blockchain:{self.chain}"


def main():
    blockchain = Blockchain()
    blockchain.add_block('1')
    blockchain.add_block('2')
    print(blockchain)


if __name__ == '__main__':
    main()
