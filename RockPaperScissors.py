import random

def RockPaperScissors():
    while True:
        p = input('Rock, Paper, or Scissors?')
        if p == 'I quit':
            return False

        c = random.randint(1,3)
        if c == 1:
            print(f'{c}, Computer = Rock')
            c = 'rock'
        elif c == 2:
            print(f'{c}, Computer = Paper')
            c = 'paper'
        else: #c  == 3
            print(f'{c}, Computer = Scissors')
            c = 'scissors'
        
        if p.lower() == 'rock' and c == 'scissors':
            print('You win')
        elif p.lower() == 'rock' and c == 'rock':
            print('Game tied')
        elif p.lower() == 'rock' and c == 'paper':
            print('You lose')
       
        elif p.lower() == 'paper' and c == 'scissors':
            print('You lose')
        elif p.lower() == 'paper' and c == 'rock':
            print('You win')
        elif p.lower() == 'paper' and c =='paper':
            print('Game tied')

        elif p.lower() == 'scissors' and c == 'rock':
            print('You Lose')
        elif p.lower() == 'scissors' and c == 'paper':
            print('You win')
        else: print('Game tied')


RockPaperScissors()
    
