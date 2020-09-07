import random
def main():
  dice_rolls=int(input('How many dice would you like to roll?'))
  dice_sum=0
  first=1
  last=int(input('How many sides are the dice?'))
  for i in range(0,dice_rolls):
  
    roll=random.randint(first, last)
    dice_sum= dice_sum+roll
    if roll==1:
      print(f'You rolled a {roll}! Epic fail!')
    
    elif roll==last:
      print(f'You rolled a {roll}! Amazing success!')

    else:
      print(f'You rolled a {roll}')  
  print(f'You have rolled a total of {dice_sum}')
  

if __name__== "__main__":
  main()