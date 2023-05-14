from blockchain import Blockchain

print("Welcome to the Ultimate Mini Blockchain Simulator!")

local_blockchain = Blockchain()

while True:

    str = input("Would you like to append a new block? Y or N: ")

    if str == "Y":
        sender = input("Who is the sender?: ")
        reciever = input("Who is the receiver?: ")
        amount = input("How much money was transferred in the transaction?: ")

        block_to_be_added = {"sender": sender, "reciever": reciever, "amount": amount}

        local_blockchain.add_block(block_to_be_added)

    elif str == "N":
        print("Here is your entire blockchain! \n ")

        local_blockchain.print_blocks()

        break

    else:
        print("Please enter Y or N")

