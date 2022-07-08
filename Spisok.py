a=['это строка',
   'http://funny.ru']
for x in a:
    if(x[0:3] == 'wwww','http'):
        print(x)
        #нахождение части текста с помощью фукнции find
s='нужно найти в этой строке емайл, моя почта behzod.rustam@mail.ru'
words=s.split(" ")
for w in words:
    n=w.find('@mail.ru')
    if n!=-1:
        print('В строке присутствует емайл: ' + str(w))'''
from random import randrange
a=randrange(1,101)
while True:
   guess=int(input("Enter your guess!! "))
   if guess==a:
       print("You win")
       break
   elif guess>a:
       print("Too big")
   else:
       print("Too small")
