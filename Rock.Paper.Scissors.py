import random
def play():

    user = input("Pick rock,paper,scissors:\n").lower()

 
    choices = ['rock','paper','scissors']
    computer_choice = random.choice(choices)

    print(computer_choice)
    print(user)
    computer = computer_choice

	

    if user =='rock':
        if computer =='rock':
            print('Tie')
        elif computer =='paper':
            print('Computer Wins')
        elif computer =='scissors':
            print('User Wins')
    
    if user =='paper':
        if computer =='rock':
            print('User Wins')
        elif computer =='paper':
            print('Tie')
        elif computer =='scissors':
            print('Computer Wins')
    
    if user =='scissors':
        if computer =='rock':
            print('Computer Wins')
        elif computer =='paper':
            print('User Wins')
        elif computer =='scissors':
            print('Tie')
def main():
    play()
    while True:
        choice2=input("Again? y/n:\n").lower()
        if choice2=="y":
            play()
        else:
            break
main()

            



