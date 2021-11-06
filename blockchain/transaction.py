# -*- coding: utf-8 -*-
class Transaction:
    def __init__(self, sender, recipient, amount: any):
        self.sender = sender
        self.recipient = recipient
        self.content = amount

    def __str__(self):
        return f'{self.sender} -> {self.recipient} ({self.content})'

    def __repr__(self):
        return f'{self.sender}{self.recipient}{self.content}'
