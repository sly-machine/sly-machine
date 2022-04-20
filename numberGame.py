from random import randint
import sys

print('Weclcom to Reboot_Mess')
print('You can pick a number from  0 to 1000')
print('For quitting the game you can simply insert \'Q\' ')
print('Are you ready?')

while True : 
    starter = input().lower()
    if starter == '' :
        print('Please type something...')
        continue
    elif starter[0] == 'y':
       print('Let\'s go! :) ')
       break
    elif starter[0] == 'n':
        print('Got it. :( ')
        sys.exit(0)
    elif starter[0] == 'q':
        print('Got it. :( ')
        sys.exit(0)
    else :
        print('Unavailable request')
        print('Answer again...')

# if starter[0] == 'y':
#     print('Let\'s go! :) ')
# elif starter[0] == 'n':
#     print('Got it. :( ')
#     sys.exit(0)
# elif starter[0] == 'q':
#     print('Got it. :( ')
#     sys.exit(0)
# else :
#     print('Unavailable request')
#     while True: 
#         starter_1 = input('Answer again...')
#         if starter_1[0] == 'y':
#             print('Let\'s go! :) ')
#             break
#         elif starter_1[0] == 'n':
#             print('Got it. :( ')
#             sys.exit(0)
#         elif starter_1[0] == 'q':
#             print('Got it. :( ')
#             sys.exit(0)
        


sysScore = 0
userScore = 0

secret_num = range(0, 1000)
secret_score = 5

while sysScore < secret_score and userScore < secret_score : 
    print('  Insert your number from 0 to 1000: ')
    userAct = input()
    sysAct = randint(0 , 1000)
    
    if userAct.strip('-').isdigit():
        userAct = int(userAct)
        if  0 < userAct < 1000 :
            if userAct == sysAct:
                print('That\'s a tie...')
            elif userAct > sysAct :
                print('You won!')
                userScore += 1
            elif userAct < sysAct :
                print('Computer won!')
                sysScore += 1
            print(f'Your number: {userAct} \nComputer number: {sysAct} ')
            print(f'Your victories: {userScore}, Computer victories: {sysScore} ')

        elif userAct < 0 :
            print('Out of defined rang!')
        elif userAct > 1000 :
            print('Out of defined rang!')
    elif userAct == 'q' :
        print('You left the game!')
        sys.exit(0)
    else :
        print('Numbers only! No word.')

print(f'Final scores: \n Your victories: {userScore} \n Computer victories: {sysScore} ')
print('We enjoyed playing with you. \n Have a nice day!')



