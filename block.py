class Block:
    """
    Block: unit of storage.
    Store a transaction in a blockchain that supports a cryptocurrency.
    """

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Block-data:{self.data}"


def main():
    block = Block("test1")
    print(block)


if __name__ == '__main__':
    main()
