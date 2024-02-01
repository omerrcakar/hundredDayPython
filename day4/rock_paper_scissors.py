import random

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


rps_list = [rock, paper, scissors]

my_choice = int(input("Rock(1) - Paper(2) - Scissors(3) Which do you want?\n"))

random_pc = rps_list[random.randint(0,len(rps_list) - 1)]



if my_choice == 1:
    print("My choice: \n")
    print(rps_list[my_choice - 1])

    print(f"Pc choice : \n")
    print(random_pc)

    if random_pc == rock:
        print("Berabere")
    elif random_pc == paper:
        print("Kaybettin")
    elif random_pc == scissors:
        print("Kazandın")
elif my_choice == 2:
    print("My choice: \n")
    print(rps_list[my_choice - 1])

    print(f"Pc choice : \n")
    print(random_pc)

    if random_pc == rock:
        print("Kazandın")
    elif random_pc == paper:
        print("Berabere")
    elif random_pc == scissors:
        print("Kaybettin")
elif my_choice == 3:
    print("My choice: \n")
    print(rps_list[my_choice - 1])

    print(f"Pc choice : \n")
    print(random_pc)

    if random_pc == rock:
        print("Kaybettin")
    elif random_pc == paper:
        print("Kazandın")
    elif random_pc == scissors:
        print("Berabere")
else:
    print("Geçersiz seçim")


