
import hashlib
from datetime import datetime

from audit_log import log_security_event


# ============================================================
# BLOCK
# ============================================================

class Block:

    def __init__(
        self,
        index,
        encrypted_data,
        data_hash,
        previous_hash,
        timestamp=None
    ):
        self.index = index

        self.timestamp = (
            timestamp
            if timestamp is not None
            else datetime.now().isoformat()
        )

        self.encrypted_data = encrypted_data
        self.data_hash = data_hash
        self.previous_hash = previous_hash

        # Calculate the block hash
        self.hash = self.calculate_hash()

    # ========================================================
    # CALCULATE BLOCK HASH USING SHA-256
    # ========================================================

    def calculate_hash(self):
        block_data = (
            str(self.index)
            + self.timestamp
            + self.encrypted_data
            + self.data_hash
            + self.previous_hash
        )

        return hashlib.sha256(
            block_data.encode("utf-8")
        ).hexdigest()


# ============================================================
# BLOCKCHAIN
# ============================================================

class Blockchain:

    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    # ========================================================
    # CREATE GENESIS BLOCK
    # ========================================================

    def create_genesis_block(self):
        genesis_data = "Genesis Block"

        genesis_hash = hashlib.sha256(
            genesis_data.encode("utf-8")
        ).hexdigest()

        genesis_block = Block(
            index=0,
            encrypted_data=genesis_data,
            data_hash=genesis_hash,
            previous_hash="0",
            timestamp="GENESIS"
        )

        self.chain.append(genesis_block)

    # ========================================================
    # ADD NEW BLOCK
    # ========================================================

    def add_block(self, encrypted_data, data_hash):
        if not self.verify_chain():
            raise ValueError(
                "Cannot add a block: blockchain integrity check failed."
            )

        previous_block = self.chain[-1]

        new_block = Block(
            index=len(self.chain),
            encrypted_data=encrypted_data,
            data_hash=data_hash,
            previous_hash=previous_block.hash
        )

        self.chain.append(new_block)

        return new_block

    # ========================================================
    # VERIFY BLOCKCHAIN INTEGRITY
    # ========================================================

    def verify_chain(self, username=None, role="Unknown"):
        """
        Verify block data hashes, block hashes, indices,
        genesis block, and previous-block links.

        Returns True if valid, otherwise False.
        Optionally records the result in the security audit log.
        """

        def finish_verification(is_valid):
            if username is not None:
                try:
                    log_security_event(
                        username=username,
                        event="blockchain_integrity_check",
                        success=is_valid,
                        role=role
                    )
                except OSError as error:
                    # Report audit storage errors without changing
                    # the cryptographic verification result.
                    print(
                        "WARNING: Could not write security audit log:",
                        error
                    )

            return is_valid

        # The chain must contain a genesis block.
        if not self.chain:
            return finish_verification(False)

        genesis = self.chain[0]

        # Check genesis block structure.
        expected_genesis_data = "Genesis Block"

        expected_genesis_data_hash = hashlib.sha256(
            expected_genesis_data.encode("utf-8")
        ).hexdigest()

        if (
            genesis.index != 0
            or genesis.timestamp != "GENESIS"
            or genesis.encrypted_data != expected_genesis_data
            or genesis.data_hash != expected_genesis_data_hash
            or genesis.previous_hash != "0"
            or genesis.hash != genesis.calculate_hash()
        ):
            return finish_verification(False)

        # Verify every block.
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # 1. Check block index.
            if current_block.index != i:
                return finish_verification(False)

            # 2. Check data hash.
            calculated_data_hash = hashlib.sha256(
                current_block.encrypted_data.encode("utf-8")
            ).hexdigest()

            if current_block.data_hash != calculated_data_hash:
                return finish_verification(False)

            # 3. Check current block hash.
            if current_block.hash != current_block.calculate_hash():
                return finish_verification(False)

            # 4. Check previous block connection.
            if current_block.previous_hash != previous_block.hash:
                return finish_verification(False)

        return finish_verification(True)

    # ========================================================
    # LOAD EXISTING BLOCK FROM STORED DATA
    # ========================================================

    def add_existing_block(
        self,
        encrypted_data,
        data_hash,
        block_hash,
        previous_hash,
        timestamp
    ):
        """
        Reconstruct a block while preserving its stored hash
        so that integrity verification can detect modifications.
        """

        new_block = Block(
            index=len(self.chain),
            encrypted_data=encrypted_data,
            data_hash=data_hash,
            previous_hash=previous_hash,
            timestamp=timestamp
        )

        # Preserve the hash read from storage.
        new_block.hash = block_hash

        self.chain.append(new_block)

        return new_block
