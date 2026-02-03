def rps():
    def computer():
        import random
        game=['rock','paper','scissor']
        choice=random.choice(game)
        return choice
    pc=0 #point to computer
    pu=0 #point to user
    while pc<3 and pu<3:
        com = computer()
        lst = ['rock', 'paper', 'scissor']
        user = input("Enter your choice {Rock,Paper,Scissor} :").lower()
        if user not in lst:
            print("Enter valid input")
        else:
            print(f"Computer choice is : {com}")
            if com == user:
                print("Tie")
                print(f"Score : User={pu}, computer={pc}")
            elif user == "rock" and com == "paper":
                print("Computer got point")
                pc += 1
                print(f"Score : User={pu}, computer={pc}")
            elif com == "rock" and user == "paper":
                print("You got point")
                pu += 1
                print(f"Score : User={pu}, computer={pc}")
            elif user == "rock" and com == "scissor":
                print("You got point")
                pu += 1
                print(f"Score : User={pu}, computer={pc}")
            elif com == "rock" and user == "scissor":
                print("Computer got point")
                pc += 1
                print(f"Score : User={pu}, computer={pc}")
            elif user == "paper" and com == "scissor":
                print("computer got point")
                pc += 1
                print(f"Score : User={pu}, computer={pc}")
            elif com == "paper" and user == "scissor":
                print("You got point")
                pu += 1
                print(f"Score : User={pu}, computer={pc}")
    if pu==3:
            print("You won the Game")
    else:
            print("Computer won the Game")
    play = input("Want to play again? {y/n}").lower()
    if play == 'y':
        rps()

rps()