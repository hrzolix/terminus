#1. Write a Python program to print the following string in a specific format (see the output).

print(f"Twinkle, twinkle, little star,\n \t How I wonder what you are!\n \t\tUp above the world so high,\n \t \tLike a diamond in the sky.\n Twinkle, twinkle, little star,\n \tHow I wonder what you are")

#2. Write a Python program to get the Python version you are using. Go to the editor
import builtins
from posixpath import join
from random import randint
import sys

print(sys.version)

#3. Write a Python program to display the current date and time.
import datetime

now = datetime.datetime.now()
print(f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

#4. Write a Python program which accepts the radius of a circle from the user and compute the area
import math

pi = math.pi
radius = float(input("How much is the radius: "))**2
print(f"Area is: {pi*radius}")

#5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
first_name = input("Your first name: ")
last_name = input("Your last name: ")

print(first_name[::-1], last_name[::-1])

#6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
numbers = input("Write some numbers: ")
lis = numbers.split()
print(lis, tuple(lis))

#7. Write a Python program to accept a filename from the user and print the extension of that.
filename = input("Your filename: ")
extension = filename.split(".")
print(extension[1])

#8. Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0], color_list[-1])

#9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
print(f"The examination will start from : %i / %i / %i"%exam_st_date)




#10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

n = int(input("Write a number: "))

n1 = int( "%s" % n )
n2 = int( "%s%s" % (n, n) )
n3 = int( "%s%s%s" % (n, n, n) )

print(n1 + n2 + n3)

#11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s). 
abs.__doc__
sum.__doc__
dict.__doc__

#12. Write a Python program to print the calendar of a given month and year.
import calendar

print(calendar.month(2004, 5))

#13. Write a Python program to print the following 'here document'. 
print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")

#14. Write a Python program to calculate number of days between two dates.
from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2015, 7, 11)
delta = l_date - f_date
print(delta.days)

#25. Write a Python program to check whether a specified value is contained in a group of values.
a = [1, 5, 8, 3]

3 in a
7 in a

#28. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

for i in numbers:
    if i != 237:
        print(i)
    else:
        break

#53. Write a python program to access environment variables
import os
print(os.environ["HOME"])

#89. Write a Python program to perform an action if a condition is true. Go to the editor
#Given a variable name, if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal.

def check(val):
    if val==1:
        print("First day of a Month!")

#44. Write a Python program to locate Python site-packages.
import site
s = site.getsitepackages()

#141. Write a python program to convert decimal to hexadecimal.
hex(255)

#72. Write a Python program to get the details of math module.
import math
help(math)

#122. Write a Python program to empty a variable without destroying it.
n=20
d = {"x":200}
print(type(n)())
print(type(d)())

#Modules
#Module random

#1. Write a Python program to generate a random color hex, a random alphabetical string, random value between two integers (inclusive) 
# and a random multiple of 7 between 0 and 70. Use random.randint()
import random
r = lambda: random.randint(0,255)
print('#%02X%02X%02X' % (r(),r(),r()))
import string
print(''.join(random.choice(string.ascii_letters) for _ in range(5)))
print(random.randint(0,255))
print(random.randint(0, 10) * 7)

import pydataset
pydataset.data()
help(pydatasetq)


