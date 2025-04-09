import random

while True:
    try:
        choices = ["Rock","Paper","Scissors"]
        
        computer_choice = random.choice(choices)
        person_choice = input("Choose btn Rock,Paper or Scissors").capitalize()
        
        #print("Person_choice:", person_choice)
        #print("Computer_choice:", computer_choice)
        
        if person_choice == computer_choice:
            print("Person_choice:", person_choice)
            print("Computer_choice:", computer_choice)
            print("Its a tie!⚖️ ")
         
        
        elif person_choice == "Rock":
            if computer_choice == "Paper":
                print("Person_choice:", person_choice)
                print("Computer_choice:", computer_choice)
                print("You lost 😞")
               
        
        
            elif computer_choice == "Scissors":
                print("Person_choice:", person_choice)
                print("Computer_choice:", computer_choice)
                print("You won...hureeee 🏆🎉")
               
        
        
        elif person_choice == "Paper":
            if computer_choice == "Rock":
                print("Person_choice:", person_choice)
                print("Computer_choice:", computer_choice)
                print("You won.....hureeee🏆🎉 ")
              
        
        
            elif computer_choice == "Scissors":
                print("Person_choice:", person_choice)
                print("Computer_choice:", computer_choice)
                print("You lost 😞")
              
        
           
        elif person_choice == "Scissors":
            if computer_choice == "Rock":
                print("Person_choice:", person_choice)
                print("Computer_choice:", computer_choice)
                print("You lost 😞")
              
        
        
            elif computer_choice == "Paper":
                print("Person_choice:", person_choice)
                print("Computer_choice:", computer_choice)
                print("You won...hureeee 🏆🎉")
              
        
        
        else:
            print("Invalid choice.Please choose between Rock,Paper or Scissors")
    
        play_again = input("Do you want to play another round?(yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!🙂")
            break 

    except NameError as e:
        print(e)
        print("Invalid choice.Please choose between Rock,Paper or Scissors")
