import random
def main():
  dice_rolls=2
  dice_sum=0
  first=1
  last=6
  for i in range(0,dice_rolls):
  
    roll=random.randint(first, last)
    dice_sum= dice_sum+roll
    print(f'You rolled a {roll}')
  
  print(f'You have rolled a total of {dice_sum}')
  

if __name__== "__main__":
  main()