import random

print("===== Welcome To John Bank =====")

accounts = {}  # All accounts will be stored here

while True:
    print("\n--- MENU ---")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter Your Choice (1-5): ")

    # 1. CREATE ACCOUNT
    if choice == "1":
        name = input("Enter Your Name: ")
        age = int(input("Enter Your Age: "))
        email = input("Enter Your Email: ")

        # Generate 10 digit random ID
        user_id = random.randint(1000000000, 9999999999)

        accounts[user_id] = {
            "name": name,
            "age": age,
            "email": email,
            "balance": 0
        }

        print("\nAccount Created Successfully!")
        print(f"Your Name: {name}")
        print(f"Your ID: {user_id}")
        print("Please remember your ID, you will need it to login!")

    # 2. DEPOSIT
    elif choice == "2":
        user_id = int(input("Enter Your ID: "))
        if user_id in accounts:
            amount = int(input("Enter Amount To Deposit: "))
            accounts[user_id]["balance"] += amount
            print(f"{amount} Deposited Successfully!")
            print(f"New Balance: {accounts[user_id]['balance']}")
        else:
            print("ID Not Found! Please create an account first.")

    # 3. WITHDRAW
    elif choice == "3":
        user_id = int(input("Enter Your ID: "))
        if user_id in accounts:
            amount = int(input("Enter Amount To Withdraw: "))
            if amount <= accounts[user_id]["balance"]:
                accounts[user_id]["balance"] -= amount
                print(f"{amount} Withdrawn Successfully!")
                print(f"New Balance: {accounts[user_id]['balance']}")
            else:
                print("Insufficient Balance! Please check your balance.")
        else:
            print("ID Not Found!")

    # 4. CHECK BALANCE
    elif choice == "4":
        user_id = int(input("Enter Your ID: "))
        if user_id in accounts:
            acc = accounts[user_id]
            print(f"\nName: {acc['name']}")
            print(f"Balance: {acc['balance']}")
        else:
            print("ID Not Found!")

    # 5. EXIT
    elif choice == "5":
        print("Thanks For Using John Bank! Goodbye!")
        break

    else:
        print("Invalid Choice! Please enter 1 to 5.")
