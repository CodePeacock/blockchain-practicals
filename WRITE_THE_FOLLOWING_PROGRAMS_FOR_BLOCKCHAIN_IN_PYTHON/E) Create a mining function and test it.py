import hashlib


def sha256(message: str):
    return hashlib.sha256(message.encode("ascii")).hexdigest()


def mine(message: str, difficulty=1):
    assert difficulty >= 1
    prefix = "" * difficulty
    for i in range(1000):
        digest = sha256(str(hash(message)) + str(i))
        if digest.startswith(prefix):
            print(f"After {str(i)} iterations found nonce: {digest}")


mine(message="Hello World!", difficulty=2)
