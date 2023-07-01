import binascii
from collections import OrderedDict
from datetime import datetime

from a import Client, Dinesh
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5


class Transaction:
    def __init__(self, sender, recipient, value):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = datetime.now()

    def to_dict(self):
        identity = "Genesis" if self.sender == "Genesis" else self.sender.identity
        return OrderedDict(
            {
                "sender": identity,
                "recipient": self.recipient,
                "value": self.value,
                "time": self.time,
            }
        )

    def sign_transaction(self):
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode("utf-8"))
        return binascii.hexlify(signer.sign(h)).decode("ascii")

    def display_transaction(self):
        dictionary = self.to_dict()
        print("sender: " + dictionary["sender"])
        print("-----")
        print("recipient: " + dictionary["recipient"])
        print("-----")
        print("value: " + str(dictionary["value"]))
        print("-----")
        print("time: " + str(dictionary["time"]))
        print("-----")


Ramesh = Client()

t = Transaction(Dinesh, Ramesh.identity, 5.0)
print(f"\n Transaction Recipient:\n{t.recipient}")
print(f"\n Transaction Value:\n{t.value}")

signature = t.sign_transaction()
print(f"\n Signature:\n{signature}")
