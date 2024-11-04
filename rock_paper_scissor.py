import random

while True:
    print("-----Welcome to Rock-Paper-scissors Game-----")

    ties_score = 0
    user_score = 0
    computer_score = 0

    name = input("Enter your name: ")
    print("The winning rules are:\n1.Rock vs Paper is Paper\n2.Paper vs Scissors is Scissors\n3.Scissors vs Rock is Rock")

    while True:
        print("\nThe available choices are\n1.Rock\n2.Paper\n3.Scissors")
        choice_input = int(input("Enter your choice between 1-3 "))

        if choice_input == 1:
            user_choice = "Rock"
        elif choice_input == 2:
            user_choice = "Paper"
        elif choice_input == 3:
            user_choice = "Scissors"
        else:
            print("The choice is invalid")

        print("The user's choice is taken as ",user_choice)
        print("The computer's turn")

        computer_input = random.randint(1, 3)
        if computer_input == 1:
            computer_choice = "Rock"
        elif computer_input == 2:
            computer_choice = "Paper"
        elif computer_input == 3:
            computer_choice = "Scissors"

        print("The computer's choice is ",computer_choice)

        if user_choice == computer_choice:
            ties_score += 1
        elif (user_choice == "Paper" and computer_choice  == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper") or \
             (user_choice == "Rock" and computer_choice == "Scissors"):
            print("The user wins this round")
            user_score += 1
        else:
            print("The computer won this round")
            computer_score += 1
    
        print("After the completion of this round the scores are\n1.No of ties =",ties_score,"\n2.No of user wins =",user_score,"\n3.No of computer wins =",computer_score)

        exit_choice = int(input("Enter 0 to exit and 1 to continue: "))
        if exit_choice == 0:
            break
    
    print("Game Over!")
    if user_score > computer_score:
        print("The winner is ",name," with the total score of ",user_score)
    elif user_score < computer_score:
        print("The winner is computer with the total score of ",computer_score)
    else:
        print("The match has been tied between the player ",name," and computer")

    print("Thank you for playing!")
    break