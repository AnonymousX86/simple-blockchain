# -*- coding: utf-8 -*-
class Transaction:
    def __init__(self, sender, recipient, content: str):
        self.sender = sender
        self.recipient = recipient
        self.content = content

    def __str__(self):
        return f'{self.sender} -> {self.recipient} ({self.content})'

    def __repr__(self):
        return f'{self.sender}{self.recipient}{self.content}'
