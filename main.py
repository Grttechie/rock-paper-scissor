import random
#R - Rock
#P - Paper
#S - Scissor

com_option = ['R','P','S'] #list of computer's options


#A while loop determines the state of the game
while True:
    #your input
    your_input = input("Pick 'R' - for Rock,'P' - for Paper or 'S' - for Scissors:\n")

    #random select the option for the computer's input
    rand_com_option = random.choice(com_option)
    
    if your_input == 'R' or your_input == 'P' or your_input == 'S':
        #Conditions to check for the different states of the game
        if your_input == 'R' and rand_com_option == 'S':
            print("Player" + "(" + your_input + ")" + ":" + "CPU" + "(" + rand_com_option + ")")
            print("You win!")
            
            break #The loop breaks whenever there's a winner

        elif your_input == 'S' and rand_com_option == 'R':
            print("Player" + "(" + your_input + ")" + ":" + "CPU" + "(" + rand_com_option + ")")
            print("Computer wins!")
            break

        elif your_input == 'P' and rand_com_option == 'R':
            print("Player" + "(" + your_input + ")" + ":" + "CPU" + "(" + rand_com_option + ")")
            print ("You win!")
            break

        elif your_input == 'R' and rand_com_option == 'P':
            print("Player" + "(" + your_input + ")" + ":" + "CPU" + "(" + rand_com_option + ")")
            print("Computer wins!")
            break

        elif your_input == "S" and rand_com_option == 'P':
            print("Player" + "(" + your_input + ")" + ":" + "CPU" + "(" + rand_com_option + ")")
            print("You win!")
            break

        elif your_input == "P" and rand_com_option == 'S':
            print("Player" + "(" + your_input + ")" + ":" + "CPU" + "(" + rand_com_option + ")")
            print("Computer wins!")
            break 


    if your_input == rand_com_option:
        print("Player" + "(" + your_input + ")" + ":" + "CPU" + "(" + rand_com_option + ")")
        print("Its a Draw!")
       
        
    #The else block is executed if the user enters a wrong input    
    else:
        print("error")
        