import hashlib
import json

def sha256d(data):
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()

def reverse_bytes(hex_str):
    return bytes.fromhex(hex_str)[::-1].hex()

def calculate_merkle_root(txids):
    txids = [bytes.fromhex(reverse_bytes(txid)) for txid in txids]  # Reverse bytes for each txid
    while len(txids) > 1:
        if len(txids) % 2 == 1:
            txids.append(txids[-1])  # Duplicate the last element if odd number of txids
        txids = [sha256d(txids[i] + txids[i+1]) for i in range(0, len(txids), 2)]
    return reverse_bytes(txids[0].hex())

with open('input.json', 'r') as file:
    data = json.load(file)

transactions = data.get('tx', [])

txids = [tx['hash'] for tx in transactions]

for i, txid in enumerate(txids):
    print(f"{i}. txid : {txid}")

merkle_root = calculate_merkle_root(txids)
print(f"MerkleRootHash : {merkle_root}")

