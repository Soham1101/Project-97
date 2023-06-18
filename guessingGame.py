import random 
chances = int(5)
playerGuess = int(10)
number = (random.randint(1,9))

print ("This is a game where you have to guess the number I am thinking of, I will give hints but you have 5 chances. The number will be from 1-9")
#print (number)
while chances > 0:
    guess = int(input ())


    if (guess > number):
        print ("Too high")


    if (guess < number):
        print ("Too low")


    if (guess == number):
        print ("You Win")
        exit()
        break

    chances = chances - 1 


if chances == 0:
    print ("You lose the number was", number)
    exit()