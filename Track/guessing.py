import random
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
guess(int(input('Choose your Number limit: ')))