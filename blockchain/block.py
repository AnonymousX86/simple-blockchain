# -*- coding: utf-8 -*-
from hashlib import sha256
from time import time


class Block:
    def __init__(self, index: int, proof: any, previous_hash: str, transactions: list, timestamp: time = time()):
        self.index = index
        self.proof = proof
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp

    @property
    def comp_hash(self):
        string_block = '{0}{1}{2}{3}{4}'.format(
            self.index,
            self.timestamp,
            list(tr.__repr__() for tr in self.transactions),
            self.proof,
            self.previous_hash
        )
        return sha256(string_block.encode()).hexdigest()
