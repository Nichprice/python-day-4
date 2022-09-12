import random

touchrock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


move = [touchrock, paper, scissors]
rando = random.randint(0, 2)

user = int(input("type 0 for rock, 1 for paper, 2 for scissors.\n"))

if user > 2 or user < 0:
    print("invalid number")
else:
    user_move = move[user]
    print(f"You chose {user_move}")
    computer_move = move[rando]
    print(f"Computer chose {computer_move}")

    if user_move == computer_move:
        print("It's a draw!")
    elif user_move == 0 and computer_move == 2:
        print("You win!")
    elif computer_move == 0 and user_move == 2:
        print("You lose!")
    elif user_move == 1 and computer_move == 0:
        print("You win!")
    elif computer_move == 1 and user_move == 0:
        print("You lose!")
    elif user_move == 2 and computer_move == 1:
        print("You win!")
    elif computer_move == 2 and user_move == 1:
        print("You lose!")

