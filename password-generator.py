from random import randrange
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-n', '--number', help='Number of generated passwords')
parser.add_argument('-s', '--size', help='Password max size')
parser.add_argument('-l', '--level', help='Password complexity level')

args = parser.parse_args()

numberOfPasswords = int(args.number) if args.number else 5
passwordSize = int(args.size) if args.size else 8
passwordLevel = int(args.level) if args.level else 3

char = ['a', 'b', 'c', 'ç','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
  'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

caps = ['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
  'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special = ['!', '#', '$', '%', '&', "'", '"', '(', ')', '*', '+', '-', 
  '.', ',', ':', ';', '<', '=', '>', '?', '@',  '[', ']', '^', '`', 
  '|', '{', '}', '~', '/']

for i in range(int(numberOfPasswords)):
  password = ''

  for j in range(int(passwordSize)):
    charChoise = randrange(int(passwordLevel))

    if charChoise == 0:
      charChoise = randrange(len(char))
      password += char[charChoise]

    elif charChoise == 1:
      charChoise = randrange(len(caps))
      password += caps[charChoise]

    elif charChoise == 2:
      charChoise = randrange(len(number))
      password += number[charChoise]

    elif charChoise == 3:
      charChoise = randrange(len(special))
      password += special[charChoise]

  print(password)
  password = ''