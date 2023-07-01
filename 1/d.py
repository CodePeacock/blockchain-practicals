from a import Dinesh
from b import Transaction


class Block:
    def __init__(self, client):
        self.verified_transactions = []
        self.previous_block_hash = ""
        self.nonce = ""
        self.client = client


def dump_blockchain(blocks):
    print(f"\nNumber of blocks in the chain: {len(blocks)}")

    for i, block in enumerate(blocks):
        print(f"block # {i}")
        for transaction in block.verified_transactions:
            Transaction.display_transaction(transaction)
            print("---------------")

    print("=========================")


t0 = Transaction("Genesis", Dinesh.identity, 500.0)

block0 = Block(Dinesh)

block0.previous_block_hash = ""
NONCE = None

block0.verified_transactions.append(t0)
digest = hash(block0)
last_block_hash = digest

TPCoins = [block0]
dump_blockchain(TPCoins)
