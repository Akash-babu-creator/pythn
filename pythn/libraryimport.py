
        # or

'''import math
import random
print(math.log(10))
print(math.sqrt(4))
# for i in range(3):
#     print(random.random())
#     print(random.randint())
#let us create a toss simulation
a=random.random()
if(a<0.5):
    print("head")
else:
    print("tails")
#let us simulate a six faced dice
dice1=random.randrange(1,7)
dice2=random.randrange(1,7)
total=dice1+dice2
print("pair of dice results in",total)'''
#different ways to import library

'''import calendar
print(calendar.calendar(2021))
print(calendar.month(2022,10))'''
         #or
"""from calendar import *          #import entire library
print(calendar(2021))
print(month(2022,10))"""
  
  #importing a function from library
'''from calendar import month
print(month(2023,4))
print(calendar(2023))     #will give an error saying calender is not derined'''

'''from calendar import month, calendar
print(month(2023,4))
print(calendar(2023))     #won't show error'''

# import calendar as c
# print(c.month(2022,4))
# print(c.calendar(2002))


from calendar import month as m
print(m(2002,8))