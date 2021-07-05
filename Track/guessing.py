import random
import sys

def guess(x):
    number = 0
    while number == 0:
     random_number = random.randint(1,x)
     guess = 0
     while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print("Too Low")
        elif guess > random_number:
            print('Too High')

     print(f'JackPot!!!!!\
        The Number {random_number} is right')
#guess(int(input('Choose your Number limit: ')))

def computer_guess(x):
   
    low = 1
    high = x
    feedback = ''
    chance = 3
   
    
    
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H), too low (L) or correct(C): ')
        if feedback == 'h':
            high = guess - 1
            chance = chance - 1
            print(f'{chance} try remaing')
        elif feedback == 'l':
            low = guess + 1
            chance = chance - 1
            print(f'{chance} try remaing')
    
    if chance == 0:
        print('Your chances are exausted')
        sys.exit()    
    print(f'Congratulations!!! , {guess} is correct')
    
    
    
computer_guess(100)