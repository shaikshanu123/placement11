balance = 1000

print("1.Deposit  2.Withdraw  3.Check")

choice = input("Enter choice: ")

if choice == "1":
    amount = float(input("Deposit amount: "))
    balance = balance + amount
    print("Balance is:", balance)

elif choice == "2":
    amount = float(input("Withdraw amount: "))
    balance = balance - amount
    print("Balance is:", balance)

elif choice == "3":
    print("Balance is:", balance)

else:
    print("Wrong choice")
