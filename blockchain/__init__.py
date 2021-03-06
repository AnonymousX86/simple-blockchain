# -*- coding: utf-8 -*-
from time import time

from .block import Block
from .transaction import Transaction


class Blockchain:
    def __init__(self):
        self.chain: list[Block] = []
        self.pending_transactions: list[Transaction] = []

        self.new_block(
            proof=100,
            previous_hash='Genesis block.'
        )

    def new_block(self, proof, previous_hash=None) -> bool:
        block = Block(
            index=len(self.chain),
            proof=proof,
            previous_hash=previous_hash or self.chain[-1].comp_hash,
            transactions=self.pending_transactions,
            timestamp=time()
        )
        self.pending_transactions = []
        if not len(self.chain):
            valid = True
        elif self.validate_block(block, self.last_block):
            valid = True
        elif self.proof_of_work(proof):
            valid = True
        else:
            print('Unable to add block, wrong hash.')
            valid = False
        if valid:
            self.chain.append(block)
        return valid

    def validate_block(self, block: Block, previous_block: Block) -> bool:
        if block.index != previous_block.index + 1:
            return False
        elif block.previous_hash != previous_block.comp_hash:
            return False
        elif block.timestamp <= previous_block.timestamp:
            return False
        return True

    def proof_of_work(self, proof) -> bool:
        return proof == 100

    @property
    def last_block(self) -> Block:
        return self.chain[-1]

    def new_transaction(self, sender, recipient, content: str) -> int:
        transaction = Transaction(
            sender=sender,
            recipient=recipient,
            content=content
        )
        self.pending_transactions.append(transaction)
        return self.last_block.index + 1
