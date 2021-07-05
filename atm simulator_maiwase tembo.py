
# Client inserts card into ATM

# Card prompts ATM account number


while True:
#Insert card and ATM pulls account
    accountNumber = int(input("\nInsert card"))
    pin = 0000


    #ATM requesting pin

    def atmTransaction():
        while True:
            count = 0
            pin = int(input("\nEnter account pin: "))
            count = count +1

#if pin is 0000 print ATM choices
            try:
                pin = int(pin)
                if pin == 0000:
                    print("Welcome to the Bank of Maiwase")
                    print("1-Withdraw")
                    print("2-Balance Enquiry")
                    print("3-Fast Cash")
                    choice = int(input("Please choose transaction: "))

                   #simulating withdraw
                    if choice ==1:
                        withdraw = int(input("Enter withdraw amount: "))
                        balance = 100
                        if withdraw < balance and withdraw % 100 == 0:
                            print("Please take your amount:", withdraw)
                            balance = balance - withdraw
                            print("Remaining Balance:", balance)
                        else:
                            print("Insufficient funds")
                            break
#if pin is not 0000 try 2 more times and if third attempt is incorrect throw an error
                while pin != 0000 and count < 3:
                    print("\nInvalid Id.. Re-enter: ")
                    if count == 3:
                        break
            except ValueError:
                print("\nAmount entered is invalid... Try again")
