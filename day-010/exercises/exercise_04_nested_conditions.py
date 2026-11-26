account_active = True
balance = 500
withdrawal_amount = 200

if account_active:
    print("Account verified")
    
    if balance >= withdrawal_amount:
        print("Sufficient funds")

        if withdrawal_amount > 0:
            print("Withdrawal approved")