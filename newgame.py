import random
import time
import pygame

WIDTH_DISPLAY=500
HEIGHT_DISPLAY=500

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
GRAY_COLOR = (125, 125, 125)
LIGHT_BLUE_COLOR = (64, 128, 255)
GREEN_COLOR = (0, 200, 64)
YELLOW_COLOR = (225, 225, 0)
PINK_COLOR = (230, 50, 230)
PI = 3.14

pygame.init()

screen = pygame.display.set_mode((WIDTH_DISPLAY,HEIGHT_DISPLAY))

pygame.display.set_caption("Draw primitives")

clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True
    
    
    #pygame.draw.line(screen, (255,255,255), [10, 30], [290, 15], 3)
    pygame.draw.line(screen, WHITE_COLOR, [10, 30], [290, 15], 3)
    pygame.draw.line(screen, WHITE_COLOR, [10, 80], [320, 55])
    
    # pygame.draw.aaline(screen, WHITE_COLOR, [10, 70], [290, 55])
   
    pygame.display.update()

pygame.draw.lines(screen, YELLOW_COLOR, True, [[10, 10], [140, 70], [280, 20]], 12)

pygame.draw.polygon(screen, GREEN_COLOR, [[150, 10], [180, 50], [90, 90], [30, 30]],8)

pygame.draw.aalines(screen, GREEN_COLOR, True, [[250, 110], [280, 150], [190, 190], [130, 130]])

pygame.draw.rect(screen, PINK_COLOR, (20, 20, 100, 75))

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
GRAY_COLOR = (125, 125, 125)
LIGHT_BLUE_COLOR = (64, 128, 255)
GREEN_COLOR = (0, 200, 64)
YELLOW_COLOR = (225, 225, 0)
PINK_COLOR = (230, 50, 230)
PI = 3.14

pygame.draw.arc(screen, WHITE_COLOR, (10, 50, 280, 100), 0, PI)

pygame.draw.circle(screen, YELLOW_COLOR, (100, 100), 50,5)

pygame.draw.ellipse(screen, GREEN_COLOR, (10, 50, 280, 100))

pygame.draw.line(screen, (255,255,255), [10, 30], [290, 15], 3)


empty = False
def clear():
  print('\n'*15)
print('What do you wanna do? (Tutorial, Start)')
mode = input()
while mode != 'Start':
  if mode == 'Tutorial':
    print('\n'*3)
    print('You are in a casino to bet your money.')
    print('You start with $100, and your mission is to get $5000 to win.')
    print('You will need to enter your bet amount, then type what you are bet in.')
    print('''Options to bet are:
     - Red or Black: This will double your bet if you win.
     - Number from 1 - 36: This will make your bet worth 20 times if you win.''')
    time.sleep(3)
    print('Press [Enter] to close this tutorial.')
    n = input()
    if n == '':
      clear()
      print('What do you wanna do? (Tutorial, Start)')
      mode = input()
  else:
    print('\n')
    print('Only enter \'Tutorial\' or \'Start\', please.')
    print('What do you wanna do? (Tutorial, Start)')
    mode = input()
money = 100
while money < 5000:
  print('\n' * 3)
  print('You have: $%s' % money)
  if money == 0:
    empty = True
    break
  bet_amount = int(input('Bet: '))
  while bet_amount > money:
    print('\n')
    print('You don\'t have enough money.')
    print('\n')
    bet_amount = int(input('Bet: '))
  money -= bet_amount
  bet = input('Bet on what? Number or Color? ')
  if bet == 'Number':
    print('\n')
    final_bet = int(input('What number do you bet on? '))
    if 1 <= final_bet <= 36:
      print('The roulette is spinning...')
      time.sleep(3)
      k = random.randint(1, 37)
      print('It\'s number %s.' % k)
      if k == final_bet:
        print('Congratulations!You\'ve won 20 times your bet!')
        money += bet_amount * 20
      else:
        print('Oh no, you\'ve lost this time. Good luck next time!')
    else:
      print('Your number you bet on is unavailable. Please bet again!')
      money += bet_amount
  elif bet == 'Color':
    print('\n')
    final_bet = input('What color do you bet on? ')
    if final_bet == 'Black' or final_bet == 'Red':
      print('The roulette is spinning...')
      time.sleep(3)
      k = random.choice(['Red', 'Black'])
      print('The roulette lands on %s.' % k)
      if k == final_bet:
        print('You\'won 2 times your bet! Well done!')
        money += bet_amount * 2
      else:
        print('Unfortunately, you\'ve lost this time. Hope you won next time!')
    else:
      print('At the moment, your bet is unavailable. Please bet again, please.')
      money += bet_amount
  else:
    print('You wasn\'t bet for this turn because you choose something other than Number and Color. Let\'s re-bet!')
    money += bet_amount
if empty == False:
  print('\n')
  print('By being a millionare, you\'ve earn $100 and you retired.')
  print('\n')
  print('Before you retire, you\'ve sent $%s to charity. Good job!' % (money - 4900))
  print('\n')
  print('You have won this roulette game. Take screenshot of this game and you\'ll be one of our champions!')
else:
  print('You have no money left. You have nothing left to eat and then you die. Good luck next time.')

