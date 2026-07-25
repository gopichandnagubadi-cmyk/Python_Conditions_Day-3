account_balance=float(input("Enter the total balance : "))
withdrawal_amount = float(input("Enter the withdrawal amount : "))
if withdrawal_amount >0 and withdrawal_amount%100 == 0 and withdrawal_amount<=account_balance:
    print("Withdrawal successful!")
    account_balance -= withdrawal_amount
    print(f"Remaining balance : {account_balance:.2f}")
else:
    if withdrawal_amount <=0:
        print("Invalid withdrawal amount.")
    elif withdrawal_amount%100!=0:
        print("Withdrawal amount should be multiple of 100")
    elif withdrawal_amount>account_balance:
        print("Insufficient balance")

