from block import Block

class Blockchain:

    def __init__(self):
        self.chain = []
        self.all_transations = []
        self.genesis_block()
    
    def genesis_block(self):
        genesis = Block( [] , 0 )
        self.chain.append( genesis)

    def print_blocks(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print("Block {} {}".format(i, current_block))
            current_block.print_block()
    
    def add_block(self, transactions):
        new_block = Block( transactions, self.chain[len(self.chain)-1].hash)
        self.chain.append(new_block)

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]

            if (current.hash != current.generate_hash()):
                return False
        
            if (previous.hash != previous.generate_hash()):
                return False

        return True
    
    def proof_of_work(self,block, difficulty=2):
        proof = block.generate_hash()
        while proof[:difficulty] != '0'*difficulty:
            block.nonce += 1
            proof = block.generate_hash()
        block.nonce = 0
        return proof
