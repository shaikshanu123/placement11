while True:
    number = int(input("Enter table number: "))
    limit = int(input("Enter the limit: "))

    print("\nMultiplication Table:\n")

    for i in range(1, limit + 1):
        print(number, "*", i, "=", number * i)

    choice = input("\nDo you want to continue? (yes/no): ")

    if choice == "yes":
      continue
    else:
       print("Program ended.")
       break

