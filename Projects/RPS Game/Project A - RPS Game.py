import random
print ("Rock, Paper, Scissors Game")
print ("Choose between Rock, Paper, and Scissors")
print ("Enter '1' for Rock, '2' for Paper, and '3' for Scissors")
play_again = input("Do you want to play? (yes/no): ")
while play_again == "yes":
    CPU = random.randint(1,3)
    User = int(input("Enter your choice: "))
    if CPU == 1:
        if User == 1:
            print ("CPU chose Rock, it's a tie!")
        elif User == 2:
            print ("CPU chose Rock, you win!")
        elif User == 3:
            print ("CPU chose Rock, you lose!")
    elif CPU == 2:
        if User == 1:
            print ("CPU chose Paper, you lose!")
        elif User == 2:
            print ("CPU chose Paper, it's a tie!")
        elif User == 3:
            print ("CPU chose Paper, you win!")
    elif CPU == 3:
        if User == 1:
            print ("CPU chose Scissors, you win!")
        elif User == 2:
            print ("CPU chose Scissors, you lose!")
        elif User == 3:
            print ("CPU chose Scissors, it's a tie!")
    play_again = input("Do you want to play again? (yes/no): ")