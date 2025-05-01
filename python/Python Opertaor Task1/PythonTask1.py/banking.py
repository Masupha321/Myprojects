bank_name = "Phoenix National Bank"

balance= 0.00
transactions=[]
def check_balance(): # function definition
        print(f"Your currrent balance is: M{balance:.2f}")
def deposit_money():
        global balance
        try:
            amount = float(input("\nEnter deposit amount: M"))
            if amount > 0:
                balance += amount
                transactions.append(f"Deposited: M{amount:.2f}")
                print(f"M{amount:.2f} deposited succesfully!")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def withdraw_money():
            global balance
            try:
                amount = float(input("\nEnter withdrawal amount: M"))
                if amount > 0:
                    if amount <= balance:
                        balance -= amount
                        transactions.append(f"Withdrew: M{amount:.2f}")
                        print(f"M{amount:.2f} withdrawn succesfully!")
                    else:
                        print("Insufficient funds.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

def view_transaction_history():
            print("\nTransaction History:")
            if transactions:
                for transaction in transactions:
                    print(transaction)
            else:
                print("No transactions recorded.")
        
def start():
            while True:
                print(f"\nWelcome to Phoenix National Bank!")
                print("1. Check Balance")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. View Transaction History")
                print("5. Exit")

                choice = int(input("\nEnter your choice (1-5): "))

                match choice:
                    case 1:
                        check_balance()
                    case 2:
                        deposit_money()
                    case 3:
                        withdraw_money()
                    case 4:
                        view_transaction_history()
                    case 5:
                        print("Thank you for banking with us!")
                        break
                    case _:
                        print("Invalid choice. Please select a valid option.")
start() # function call



