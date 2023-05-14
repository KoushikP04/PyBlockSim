from datetime import datetime
from hashlib import sha256

class Block:

    def __init__(self, transaction, previous_hash, nonce = 0):
        self.transaction = transaction
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.timestamp = datetime.now()
        self.hash = self.generate_hash()

    def print_block(self):
        print('Timestamp:', self.timestamp)
        print('Transactions:', self.transaction)
        print('Current Hash:', self.hash)
        print("\n")

    def generate_hash(self):
        block_contents = str(self.timestamp) + str(self.transaction) + str(self.previous_hash) + str(self.nonce)

        block_hash = sha256(block_contents.encode())
        return block_hash.hexdigest()

    
