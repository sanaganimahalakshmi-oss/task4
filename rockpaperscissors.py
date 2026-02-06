import random
print("Rock Paper Scissors Game:")
print("choices: rock,paper,scissors")
choice_of_user=input("Enter the choice:").lower()
if choice_of_user not in ["rock","paper","scissors"]:
    print("invalid choice")
else:
    choices=["rock","paper","scissors"]
    choice_of_computer=random.choice(choices)
    print("\nyour choice:",choice_of_user)
    print("computer choice:",choice_of_computer)
    if choice_of_user==choice_of_computer:
        print("Result:Tie")
    elif (choice_of_user=="rock" and choice_of_computer=="scissors") or (choice_of_user=="scissors" and choice_of_computer=="paper") or (choice_of_user=="paper" and choice_of_computer=="rock"):
        print("Result:you win")
    else:
        print("Result:computer win")