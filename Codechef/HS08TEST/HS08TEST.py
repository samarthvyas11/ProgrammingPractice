#!/usr/bin/python

assumed_withdrawal_money, initial_account_balance = map(float,input().split())
bank_charges = 0.5
withdrawing_money_including_bank_charges = initial_account_balance-assumed_withdrawal_money - bank_charges

if withdrawing_money_including_bank_charges < 0 or assumed_withdrawal_money % 5 !=0:
    print("%.2f" %initial_account_balance)
else:
    print("%.2f" %withdrawing_money_including_bank_charges)
