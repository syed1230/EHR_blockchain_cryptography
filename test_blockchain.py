
import hashlib
from blockchain import Blockchain

chain = Blockchain()

# Create a valid block
encrypted_data = "demo_encrypted_record"

data_hash = hashlib.sha256(
    encrypted_data.encode("utf-8")
).hexdigest()

chain.add_block(encrypted_data, data_hash)

print("Valid chain:", chain.verify_chain())

# Simulate tampering
chain.chain[1].encrypted_data = "modified_record"

print("After tampering:", chain.verify_chain())
