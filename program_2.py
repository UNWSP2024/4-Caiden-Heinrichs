#Week 4, Program 2 - Movie Tix
#Caiden Heinrichs
#02/13/26

def main():
    #Get the number of movies to use for number of iterations
    numberOfMovies = int(input("How many movies would you like to see? "))
    #Use for counting total number of tickets
    ticketTotalCount = 0

    for i in range(numberOfMovies):
        #Get the name of the movies and number of tickets for each
        movieName = input("Enter the movie's name: ")
        numberOfTickets = int(input("How many tickets do you want for " + movieName + "? "))

        #Update the total count of tickets
        ticketTotalCount += numberOfTickets

    #Display the total number of tickets
    print("Your total number of tickets to purchase is", ticketTotalCount)


if __name__ == '__main__':
    main()
