class atm:
    def atm():
        print("HI WELCOME TO THIS ATM !!!")
        jab1=input("write your card number")
        jab2=input("write your pin number")
        Balance =200000
        print("Balance amount = ",Balance)
        withdraw=int(input("money you want to withdraw"))
        if withdraw>Balance:
            print("you cant withdraw money more than your balance")
        else:
            print("money successfully withdrawn")
        balanceleft=(Balance-withdraw)
        print("Balance left = ",balanceleft)
    atm()