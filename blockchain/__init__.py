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
        if self.validate_block(block):
            self.chain.append(block)
            return True
        else:
            print('Unable to add block, wrong hash.')
            return False

    def validate_block(self, block: Block) -> bool:
        previous_block = self.last_block
        if block.index != previous_block.index + 1:
            return False
        elif block.previous_hash != previous_block.comp_hash:
            return False
        elif block.timestamp < previous_block.timestamp:
            return False
        return True

    def proof_of_work(self, proof):
        pass

    @property
    def last_block(self) -> Block:
        return self.chain[-1]

    def new_transaction(self, sender, recipient, amount: int) -> int:
        transaction = Transaction(
            sender=sender,
            recipient=recipient,
            amount=amount
        )
        self.pending_transactions.append(transaction)
        return self.last_block.index + 1