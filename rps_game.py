rock = '''
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

images = [rock, paper, scissors]
import random

user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors:\n"))
if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose.")
else:
  print(images[user_choice])

  computer_choice = random.randint(0,2)
  print("Computer chose:")
  print(images[computer_choice])


  if computer_choice == user_choice:
    print("It's a draw.")
  elif user_choice == 2 and computer_choice == 0:
    print("You lose.")
  elif computer_choice > user_choice:
    print("You lose.")
  elif computer_choice < user_choice:
    print("You won!")
