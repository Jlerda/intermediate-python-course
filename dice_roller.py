import random
def main():
  first=1
  last=6

  roll=random.randint(first, last)
  print(f'You rolled a {roll}')

if __name__== "__main__":
  main()