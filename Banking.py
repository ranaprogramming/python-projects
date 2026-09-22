print("=" * 50)
print("BANKING SYSTEM")
print("=" * 50)

accounts = []

while True:
    print("1: Create Account")
    print("2: View Account")
    print("3: Deposit Money")
    print("4: Withdraw Money")
    print("5: Check Balance")
    print("6: Exit")

    choice = input("Enter a choice: ")

    if choice == "1":
        Accountuser = input("Enter Account holder Name: ")
        Account_no = int(input("Enter Account Number: "))
        balance = int(input("Enter Amount: "))
        account = {
            "name": Accountuser,
            "account_no": Account_no,
            "balance": balance
            }
        accounts.append(account)
        print("Account Created Successfully!")
    elif choice == "2":
        for index, account in enumerate(accounts, start=1):
            print(index, account["name"],"|", account["account_no"],"|", account["balance"],"|",)
    elif choice == "3":
        account_no = int(input("Enter Account Number: "))

        for account in accounts:
            if account["account_no"] == account_no:
                amount = int(input("Enter amount to deposit: "))
                account["balance"] = account["balance"] + amount
                print("Cash Deposit Successfully")
                break
        else:
            print("Account not found")


    elif choice == "4":
            account_no = int(input("Enter Account Number: "))
    
            for account in accounts:
                if account["account_no"] == account_no:
                    amount = int(input("Enter amount to withdraw: "))
                    if amount > account["balance"]:
                        print("Low Balance")
                    else:
                        account["balance"] = account["balance"] - amount
                        print("Cash withdraw Successfully")
                    break
            else:
                print("Account not found")

    elif choice == "5":
        account_no = int(input("Enter Account Number: "))

        for account in accounts:
            if account["account_no"] == account_no:
                print("Account Holder:", account["name"])
                print("Balance:", account["balance"])
                break
        else:
            print("Account not found")

    elif choice == "6":
        print("Exiting Banking  System...")
        break