from a import Client, Dinesh
from b import Ramesh, Transaction

# t = Transaction(Dinesh, Ramesh.identity, 5.0)
# print(f"\n Transaction Recipient:\n{t.recipient}")
# print(f"\n Transaction Value:\n{t.value}")

# signature = t.sign_transaction()
# print(f"\n Signature:\n{signature}")

Seema = Client()
Vijay = Client()

t1 = Transaction(Dinesh, Ramesh.identity, 15.0)
t1.sign_transaction()
transactions = [t1]
t2 = Transaction(Dinesh, Seema.identity, 6.0)
t2.sign_transaction()
transactions.append(t2)
t3 = Transaction(Ramesh, Vijay.identity, 2.0)
t3.sign_transaction()
transactions.append(t3)
t4 = Transaction(Seema, Ramesh.identity, 4.0)
t4.sign_transaction()
transactions.append(t4)

for transaction in transactions:
    Transaction.display_transaction(transaction)
    print("------------")
