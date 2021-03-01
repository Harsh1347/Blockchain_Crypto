class TransactionPool:
    def __init__(self):
        self.transaction_map = {}

    def set_transaction(self, transaction):
        """
        Set a transaction in transaction pool.
        """
        self.transaction_map[transaction.id] = transaction

    def existing_transaction(self, address):
        """
        Find a transaction generated  be the address in the transaction pool.
        """
        for transaction in self.transaction_map.values():
            if transaction.input['address'] == address:
                return transaction
