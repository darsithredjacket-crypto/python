import random
while True:
    user_action=input("enter a choice (rock, paper, scissors):")
    possible_actions=["rock", "paper", "scissors"]
    computer_action= random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action==computer_action:
        print(f"both players seleceted {user_action}. its a tie")
    elif user_action=="rock":
        if computer_action=="scissors":
            print("rock smashes scissors. you win!")
        else:
            print("paper covers rock. you loose!")
    elif user_action=="scissors":
            if computer_action=="paper":
                print("scissors cut paper. you win!")
            else:
                print("rock smashes scissors. you loose!")
    elif user_action=="paper":
            if computer_action=="rock":
                print("paper covers rock. you win!")
            else:
                print("scissors cut paper. you loose!")
    play_again=input("play again? (Y/N):")
    if play_again != "Y":
         break

   

