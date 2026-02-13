#Week 4, Program 5 - Bank Balance
#Caiden Heinrichs
#02/13/26

def main():
    #Set up variables for tracking
    budget = float(input("How much did you budget for this month? $"))
    totalSpending = 0.0

    while True:
        #Get the expense
        expense = float(input("Enter the cost of the expense (0 to exit): $"))

        #Check if the user ends the loop
        if expense == 0:
            break
        else:
            #Update total spending counter
            totalSpending += expense

    #Calculate the amount over/under budget
    difference = budget - totalSpending

    #Print the amount over/under budget
    if difference >= 0:
        print("You are $", round(difference, 2), "under your budget.")
    else:
        print("You are $", round(-difference, 2), "over your budget!")


if __name__ == '__main__':
    main()
