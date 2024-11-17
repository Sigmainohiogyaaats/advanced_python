import random 
print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs Paper-> Paper wins \n"
                                + "Rock vs Scissor-> Rock wins \n"
                                +"Paper vs Scissor-> Scissor wins \n") 

while True: 
    print('Enter your choice : \n1. For Rock \n2. For Paper \n3. For Scissors.')
    choice = int(input('What do you want to pick? - ')) 

    while (choice<1) or (choice>3):
        choice = int(input('Invalid input. Kindly pick between 1-3 : '))

    if choice == 1: 
        choice_name = "Rock" 
    elif choice == 2: 
        choice_name = 'Paper'        
    elif choice == 3: 
        choice_name = 'Scissors'        

    print('Users choice is: ', choice_name)
    print('\nNow its the computer\'s turn.....')

    computer_choice = random.randint(1, 3)
    while choice == computer_choice:
        computer_choice = random.randint(1, 3)
        
    if computer_choice == 1: 
        computer_choice_name = 'Rock'
    elif computer_choice == 2: 
        computer_choice_name = 'Paper' 
    elif computer_choice == 3: 
        computer_choice_name = 'Scissors' 
    
    print('Computer\'s choice is: ', computer_choice_name)
    print("\n", choice_name, "v/s", computer_choice_name)

    if (choice == 1 and computer_choice == 2) or (choice == 2 and computer_choice == 1): 
        print("Paper wins => ", end = "")
        result = "Paper"

    elif (choice == 2 and computer_choice == 3) or (choice == 3 and computer_choice == 2): 
        print("Scissor wins => ", end = "")
        result = "Scissor" 
    
    else: 
        print("Rock wins => ", end = "")
        result = "Rock" 

    if result == choice_name: 
        print("<== User Wins ==>")
    else: 
        print("<== Computer Wins ==>") 

    print("Do you want to play again? (Y/N)")
    ans = input()

    if ans == 'n' or ans == 'N':
        break

print("\nThanks for Playing!")