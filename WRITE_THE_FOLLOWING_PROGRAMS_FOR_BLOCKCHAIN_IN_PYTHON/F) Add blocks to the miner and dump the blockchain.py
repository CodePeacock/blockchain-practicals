import datetime
import hashlib


class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.now(datetime.timezone.utc)
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode("utf-8")
        sha.update(hash_str)
        return sha.hexdigest()


blockchain = [Block("First Block", "0")]

blockchain.append(Block("Second Block", blockchain[0].hash))
blockchain.append(Block("Third Block", blockchain[1].hash))

for block in blockchain:
    print(
        f"Timestamp: {block.timestamp}\nData: {block.data}\nPrevious Hash:{block.previous_hash}\nHash: {block.hash}\n"
    )
