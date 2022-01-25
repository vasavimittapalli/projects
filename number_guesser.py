import random
n=int(input('Enter a number '))
Random_Number=random.randint(0,n)
guess=0
while True:
  user_number=int(input('Make a guess'))
  guess +=1
  if user_number==Random_Number:
      print('Your guess is right')
      break
  else:
      print('your guess is wrong')
print('you make',guess,'guesses')