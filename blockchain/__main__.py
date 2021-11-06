# -*- coding: utf-8 -*-
"""
Demo blockchain project.
"""
from blockchain import Blockchain

if __name__ == '__main__':
    bc = Blockchain()

    t1 = bc.new_transaction('Origin', 'Anonymous', 15)
    t2 = bc.new_transaction('Anonymous', 'Jake', 3)
    bc.new_block(541)

    t3 = bc.new_transaction('Origin', 'Jake', 3)
    t4 = bc.new_transaction('Jake', 'Anonymous', 6)
    bc.new_block(111)

    for b in bc.chain:
        print(
            'Index:         {0.index}\n'
            'Timestamp:     {0.timestamp}\n'
            'Proof:         {0.proof}\n'
            'Self hash:     {0.comp_hash}\n'
            'Previous hash: {0.previous_hash}\n'
            'Transactions:  '.format(b)
        )
        if len(trs := b.transactions):
            for tr_ in trs:
                print(f'   {tr_}')
        else:
            print('   None')
        print('')
