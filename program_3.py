#Week 4, Program 3 - Average Rainfall
#Caiden Heinrichs
#02/13/26

def main():
    #Set up a variable to count total rainfall
    totalRainfall = 0.0
    #Ask the user for the number of years
    numberOfYears = int(input("How many years did you observe rainfall? "))

    #This will collect data for each year
    for i in range(numberOfYears):
        #Display which year data is being collected for
        print("Year", i+1, ":")

        #Collects data for each month and adds it to the running total
        for i in range(12):
            print("How much rainfall was there in month", i+1, "(inches) ? ")
            rainfall = float(input())
            totalRainfall += rainfall

    #Calculate average rainfall
    averageRainfall = totalRainfall / (numberOfYears * 12)

    #Print the total months, total rainfall, and average rainfall
    print("Total months observed:", round(numberOfYears * 12, 4))
    print("Total rainfall:", round(totalRainfall, 4), "inches")
    print("Average rainfall:", round(averageRainfall, 4), "inches")


if __name__ == '__main__':
    main()
