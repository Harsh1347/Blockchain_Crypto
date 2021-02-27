import uuid
import time

from backend.wallet.wallet import Wallet


class Transaction:
    """
    Document of an exchange in currency from sender to one or more recipients.
    """

    def __init__(self, sender_wallet, recipient, amount):
        self.id = str(uuid.uuid4())[:8]
        self.output = self.create_output(
            sender_wallet,
            recipient,
            amount
        )
        self.input = self.create_input(sender_wallet, self.output)

    def create_output(self, sender_wallet, recipient, amount):
        """
        Structure the output data for transaction.
        """

        if amount > sender_wallet.balance:
            raise Exception('Amount exceeds balance')

        output = {}
        output[recipient] = amount
        output[sender_wallet.address] = sender_wallet.balance - amount

        return output

    def create_input(self, sender_wallet, output):
        """
        Structure the input data for the transaction.
        Sign the transaction and include  the sender's public key and address.
        """
        return {
            'timestamp': time.time_ns(),
            'amount': sender_wallet.balance,
            'address': sender_wallet.address,
            'public_key': sender_wallet.public_key,
            'signature': sender_wallet.sign(output)
        }


def main():
    transaction = Transaction(Wallet(), 'recipient', 15)
    print(f'transaction.dict: {transaction.__dict__}')


if __name__ == "__main__":
    main()
