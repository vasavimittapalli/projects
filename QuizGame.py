print("Welcome to Quiz Competition")
playing=input('Are you ready to start? ')
score=0
if (playing.lower()!='yes'):
    quit()
else:
   print("OK! Let's play :)  ")
   
   
q1=input('What does CPU stands for? ')
if q1.lower()=='central processing unit':
    print('Correct')
    score +=1
else:
   print('Incorrect')     
q2=input('What does API stands for? ')
if q2.lower()=='application programming interface':
    print('Correct')
    score +=1
else:
   print('Incorrect')    
q3=input('What does AWS stands for? ')
if q3.lower()=='amazon web services':
    print('Correct')
    score +=1
else:
   print('Incorrect')
q4=input('What does CD stands for? ') 
if q4.lower()=='compact disc':
    print('Correct')
    score +=1
else:
    print('Incorrect')
print('Your Score is', score)    
print('Your %is',(score/4)*100)