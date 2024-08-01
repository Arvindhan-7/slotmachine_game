import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1

ROW=3
COL=3

collection=[]

#spin machine to form random elements
def spin_machine(row, col):
    ele_spin=["A","B"]
    for _ in range(row):
        for j in range(col):
            value=random.choice(ele_spin)
            collection.append(value)
    return collection

#show formation of collection
def show(collection):
    #chunked_list=[use[i:i+3] for i in range(0, len(use),3)]
    for i in range(0, len(collection), 3):
        print(collection[i],collection[i+1],collection[i+2])

#check and set wining list
def winning_list(collection,lines):
    #containers
    first_row=collection[0:3]
    second_row = collection[3:6]
    third_row = collection[6:9]
    #check for lines = 1
    if lines==1:
        if first_row[0]==first_row[1]==first_row[2]:
            return True
        else:
            return False
    #check for lines = 2
    elif lines==2:
        if second_row[0] == second_row[1] == second_row[2]:
            return True
        else:
            return False
    #check for lines = 3
    elif lines==3:
        if third_row[0] == third_row[1] == third_row[2]:
            return True
        else:
            return False

def game_continuity(balance,row,col,lines,collection):
    if balance==0:
        opinion=input("You have no balance, Do want to continue. If you want to continue enter ""YES"" else enter ""NO""\n")
        if opinion.upper()=="YES":
            main()
        elif opinion.upper()=="NO":
            print("GAME OVER!")
            quit()
        else:
            print("Enter the right mentioned word ti proceed")
    else:
        chance=input("Do you want to bet again, If yes enter ""YES"" or else enter ""NO""\n")
        if chance.upper()=="YES":
            spin_machine(row,col)
            get_number_of_lines()
            print(show(collection))
            winning_list(collection,lines)
        else:
            print("GAME OVER!")
            quit()

#getting amount from user
def deposit():
    while True:
        amount=input("How much would you like to deposit? / to continue\n$")
        if amount.isdigit():
            amount=int(amount)
            if amount ==0:
                print("Amount must be greater than 0")
            else:
                break
        else:

            if amount=="continue":
                continue
            else:
                print("Enter a valid amount or option")

    return amount

#getting the number of lines on to bet from user
def get_number_of_lines():
    while True:
        lines=input(f"Enter the row you would like to bet on between 1 - {MAX_LINES}\n")
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("enter a valid row to bet on")
        else:
            print("please enter a number")
    return lines

#getting the bet from user
def get_bet():
    while True:
        bet=input("What would you like to bet on each line \n$")
        if bet.isdigit():
            bet=int(bet)
            if MIN_BET<=bet<=MAX_BET:
                break
            else:
                print(f"Enter a valid amount between {MIN_BET}-{MAX_BET}")
        else:
            print("please enter a number")
    return bet

#execution area
def main():
    balance = deposit()
    lines=get_number_of_lines()
    while True:
        bet_amount = get_bet()
        #total_bet=bet_amount*lines
        if bet_amount>balance:
            print(f"you dont have enough money to bet, your balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet_amount} on {lines}. The total bet amount is ${bet_amount}")

    element=spin_machine(ROW,COL)
    print(show(collection))

    #check for winner
    winner=winning_list(collection,lines)
    if winner==True:
        balance=balance+bet_amount
        print(f"Hooray! you won the bet and earned ${bet_amount}, now your balance is ${balance}")
    else:
        balance=balance-bet_amount
        print(f"Oops! you lost the bet and lost ${bet_amount}, now your balance is ${balance}")
    proceed=game_continuity(balance,ROW,COL,lines,collection)
main()