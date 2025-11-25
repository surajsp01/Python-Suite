import random as r

random_number = r.randint(1,100)
option = input("Enter your choice for playing the game (y/n): ").lower()

while (option == 'y'):
        choice = int(input("Enter your random number between 1-100: "))
        if choice<0 or choice>100:
            print("Enter choice between range.")
        elif choice > random_number:
            print(f"{choice} is too high. Try again.")
        elif choice < random_number:
            print(f"{choice} is too low. Try again.")
        elif choice == random_number:
            print(f"{choice} is the correct number.")
            break
     
        elif(option == 'n'):
            print("Thank you.")
            break
        else:
            print(f"{choice} is invalid!")
    