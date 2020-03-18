# PF-Tryout

def bank_details(transaction_type):
    flag = False
    value = 1000
    if (transaction_type == "Withdraw" or "Deposit" or "Balance Enquiry"):
        for index in range(0, len(account_list)):
            if (account_list[index] == account_number):
                flag = True
                value = index
    transaction_details(balance_list, amount, transaction_type, value, flag)
def transaction_details(balance_list, amount,transaction_type,value,flag):
    if (flag == True and value>=0 and transaction_type=="Withdraw"):
        balance = balance_list[value]
        new_balance = balance - amount
        if (new_balance >= 500):
            balance_list[value] = new_balance
        else:
            print("Insufficient Balance")
    elif (flag == True and value>=0 and transaction_type=="Deposit"):
        balance = balance_list[value]
        new_balance = balance + amount
        balance_list[value] = new_balance
    else:
        print("Invalid Account number")
    print("Balance Amount :", new_balance)
    print("Transaction completed successfully")

def bank(account_list, balance_list, amount, account_number, transaction_type):
    if (transaction_type == "Withdraw"):
        for index in range(0, len(account_list)):
            if (account_list[index] == account_number):
                flag = True
                value = index
        if (flag == True):
            balance = balance_list[value]
            new_balance = balance - amount
            if (new_balance >= 500):
                balance_list[value] = new_balance
                print("Balance Amount :", new_balance)
                print("Transaction completed successfully")

            else:
                print("Insufficient Balance")
        else:
            print("Invalid Account number")

    elif (transaction_type == "Deposit"):
        for index in range(0, len(account_list)):
            if (account_list[index] == account_number):
                flag = True
                value = index
        if (flag == True):
            balance = balance_list[value]
            new_balance = balance + amount
            balance_list[value] = new_balance
            print("Balance Amount :", new_balance)
            print("Transaction completed successfully")
        else:
            print("Invalid Account number")
    elif (transaction_type == "Balance Enquiry"):
        for index in range(0, len(account_list)):
            if (account_list[index] == account_number):
                flag = True
                value = index
        if (flag == True):
            balance = balance_list[value]
            print(balance)
        else:
            print("Invalid Account number")
    else:
        print("Invalid Transaction Type")


account_list = [1001, 1002, 1003, 1004, 1005]
balance_list = [2500, 10000, 7000, 1500, 500]
amount = 1000
account_number = 1003
transaction_type = "Withdraw"
bank(account_list, balance_list, amount, account_number, transaction_type)