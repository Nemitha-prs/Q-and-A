#Open Your command prompt and type "pip install colorama" beore run the programme

from colorama import Fore, Back, Style # to change the colour of texts

name = input(Fore.BLUE + 'Enter Your Name to Continue :') 
print('')

import os
os.system('cls') #Cleaing the Screen

import time
time.sleep(0.1) #delaying


lines = [Fore.GREEN +'HELLOW, Welcome to the Q&A']
import time
import sys
for line in lines:          #Type writter Text
    for x in line:         
        print(x, end='')    
        sys.stdout.flush()
        time.sleep(0.1)         
    print('',)

time.sleep(0.3)

print('')
print(Fore.BLUE + name,' please press ENTER Key after reading the instructions given below')
time.sleep(3)
print('')
print(Fore.RED + '----------------- INSTRUCTIONS ----------------- ')
print('')

lines = [Fore.WHITE +' - This Q&A is made to check your knowledge',
         ' - you have a time of 15 seconds to answer a question',
         ' - There are 10 questions to answer',
         ' - You can use only capital letters to answer a Question',
         ' - You have 3 chances to answer a question',
         ' - for the first chance you will recieve 10 points',
         ' - 5 points for the 3rd change and 2 points for the 3rd chance']    # INSTRUCTIONS

for line in lines:          #Type writter Text
    for x in line:         
        print(x, end='')    
        sys.stdout.flush()
        time.sleep(0.1)         
    print('',)

print('')


lines = [Fore.LIGHTRED_EX + '       Best of Luck']    # Best of luck 

for line in lines:          #Type writter Text animation 
    for x in line:         
        print(x, end='')    
        sys.stdout.flush()
        time.sleep(0.1)         
    print('',)

enter = input('')
os.system('cls') #Cleaing the Screen


time.sleep(1)

from colorama import Fore, Back, Style  # to change the colour of texts

import os
import time
import sys

marks = 0

# ----------------------question 01----------------------
print(Fore.BLUE + 'Question 01')
time.sleep(0.5)

lines = [Fore.WHITE + 'who is the most wealthy person in the world ?']  # ELON MUSK
import time
import sys

for line in lines:  # Type writter Text
    for x in line:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.1)
    print('', )

from threading import Timer

timeout = 10
t = Timer(timeout, print, ['Sorry, times up!'])
t.start()
answer = input('Answer : ')
t.cancel()

import winsound

winsound.Beep(500, 1000)  # to add a Beep Sound

os.system('cls')  # Clearing the Screen
y = 3

if answer == "ELON MUSK":
    marks = 10

while answer != "ELON MUSK":
    while y > 1:
        lines = [Fore.RED + "Your Answer is Incorrect."]
        if y == 2:
            marks = 5
        elif y == 1:
            marks = 2

        winsound.Beep(300, 500)  # to add a Beep Sound
        for line in lines:
            for x in line:
                print(x, end='')
                sys.stdout.flush()
                time.sleep(0.1)
            print('', )
            y = y - 1
        print(Fore.BLUE + 'You have ', y, ' chanses more')
        timeout = 10
        t = Timer(timeout, print, ['Sorry,times up'])
        t.start()
        answer = input('Answer : ')
        t.cancel()
        if answer == "ELON MUSK":
            y = 0

totmarks = marks

# ----------------------question 02----------------------
print('')
print(Fore.BLUE + 'Question 02')
time.sleep(0.5)

lines = [Fore.WHITE + 'In which year titanic ship sank?']  # 1912
import time
import sys

for line in lines:  # Type writter Text
    for x in line:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.1)
    print('', )

from threading import Timer

timeout = 10
t = Timer(timeout, print, ['Sorry, times up!'])
t.start()
answer = int(input('Answer : '))
t.cancel()

import winsound

winsound.Beep(500, 1000)  # to add a Beep Sound

os.system('cls')  # Clearing the Screen
y = 3

if answer == 1912:
    marks = 10

while answer != 1912:
    while y > 1:
        lines = [Fore.RED + "Your Answer is Incorrect."]
        if y == 2:
            marks = 5
        elif y == 1:
            marks = 2

        winsound.Beep(300, 500)  # to add a Beep Sound
        for line in lines:
            for x in line:
                print(x, end='')
                sys.stdout.flush()
                time.sleep(0.1)
            print('', )
            y = y - 1
        print(Fore.BLUE + 'You have ', y, ' chanses more')
        timeout = 10
        t = Timer(timeout, print, ['Sorry,times up'])
        t.start()
        answer = input('Answer : ')
        t.cancel()
        if answer == 1912:
            y = 0

totmarks = totmarks + marks

# ----------------------question 03----------------------
print('')
print(Fore.BLUE + 'Question 03')
time.sleep(0.5)

lines = [Fore.WHITE + 'Who is the founder of watch?']  # PETER HENLEIN
import time
import sys

for line in lines:  # Type writter Text
    for x in line:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.1)
    print('', )

from threading import Timer

timeout = 10
t = Timer(timeout, print, ['Sorry, times up!'])
t.start()
answer = input('Answer : ')
t.cancel()

import winsound

winsound.Beep(500, 1000)  # to add a Beep Sound

os.system('cls')  # Clearing the Screen
y = 3

if answer == "PETER HENLEIN":
    marks = 10

while answer != "PETER HENLEIN":
    while y > 1:
        lines = [Fore.RED + "Your Answer is Incorrect."]
        if y == 2:
            marks = 5
        elif y == 1:
            marks = 2

        winsound.Beep(300, 500)  # to add a Beep Sound
        for line in lines:
            for x in line:
                print(x, end='')
                sys.stdout.flush()
                time.sleep(0.1)
            print('', )
            y = y - 1
        print(Fore.BLUE + 'You have ', y, ' chanses more')
        timeout = 10
        t = Timer(timeout, print, ['Sorry,times up'])
        t.start()
        answer = input('Answer : ')
        t.cancel()
        if answer == "PETER HENLEIN":
            y = 0
totmarks = totmarks + marks

# ----------------------question 04----------------------
print('')
print(Fore.BLUE + 'Question 04')
time.sleep(0.5)

lines = [Fore.WHITE + 'What is the Smallest country in the world?']  # VATICAN CITY
import time
import sys

for line in lines:  # Type writter Text
    for x in line:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.1)
    print('', )

from threading import Timer

timeout = 10
t = Timer(timeout, print, ['Sorry, times up!'])
t.start()
answer = input('Answer : ')
t.cancel()

import winsound

winsound.Beep(500, 1000)  # to add a Beep Sound

os.system('cls')  # Clearing the Screen
y = 3

if answer == "VATICAN CITY":
    marks = 10

while answer != "VATICAN CITY":
    while y > 1:
        lines = [Fore.RED + "Your Answer is Incorrect."]
        if y == 2:
            marks = 5
        elif y == 1:
            marks = 2

        winsound.Beep(300, 500)  # to add a Beep Sound
        for line in lines:
            for x in line:
                print(x, end='')
                sys.stdout.flush()
                time.sleep(0.1)
            print('', )
            y = y - 1
        print(Fore.BLUE + 'You have ', y, ' chanses more')
        timeout = 10
        t = Timer(timeout, print, ['Sorry,times up'])
        t.start()
        answer = input('Answer : ')
        t.cancel()
        if answer == "VATICAN CITY":
            y = 0
totmarks = totmarks + marks

# ----------------------question 05----------------------
print('')
print(Fore.BLUE + 'Question 05')
time.sleep(0.5)

lines = [Fore.WHITE + 'What does KFC stand for?']  # KENTUCKY FRIED CHICKEN
import time
import sys

for line in lines:  # Type writter Text
    for x in line:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.1)
    print('', )

from threading import Timer

timeout = 10
t = Timer(timeout, print, ['Sorry, times up!'])
t.start()
answer = input('Answer : ')
t.cancel()

import winsound

winsound.Beep(500, 1000)  # to add a Beep Sound

os.system('cls')  # Clearing the Screen
y = 3

if answer == "KENTUCKY FRIED CHICKEN":
    marks = 10

while answer != "KENTUCKY FRIED CHICKEN":
    while y > 1:
        lines = [Fore.RED + "Your Answer is Incorrect."]
        if y == 2:
            marks = 5
        elif y == 1:
            marks = 2

        winsound.Beep(300, 500)  # to add a Beep Sound
        for line in lines:
            for x in line:
                print(x, end='')
                sys.stdout.flush()
                time.sleep(0.1)
            print('', )
            y = y - 1
        print(Fore.BLUE + 'You have ', y, ' chanses more')
        timeout = 10
        t = Timer(timeout, print, ['Sorry,times up'])
        t.start()
        answer = input('Answer : ')
        t.cancel()
        if answer == "KENTUCKY FRIED CHICKEN":
            y = 0
totmarks = totmarks + marks

# ----------------------question 06---------------------
print('')
print(Fore.BLUE + 'Question 06')
time.sleep(0.5)

lines = [Fore.WHITE + 'What is the tallest building in the world?']  # BURJ KHALIFA
import time
import sys

for line in lines:  # Type writter Text
    for x in line:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.1)
    print('', )

from threading import Timer

timeout = 10
t = Timer(timeout, print, ['Sorry, times up!'])
t.start()
answer = input('Answer : ')
t.cancel()

import winsound

winsound.Beep(500, 1000)  # to add a Beep Sound

os.system('cls')  # Clearing the Screen
y = 3

if answer == "BURJ KHALIFA":
    marks = 10

while answer != "BURJ KHALIFA":
    while y > 1:
        lines = [Fore.RED + "Your Answer is Incorrect."]
        if y == 2:
            marks = 5
        elif y == 1:
            marks = 2

        winsound.Beep(300, 500)  # to add a Beep Sound
        for line in lines:
            for x in line:
                print(x, end='')
                sys.stdout.flush()
                time.sleep(0.1)
            print('', )
            y = y - 1
        print(Fore.BLUE + 'You have ', y, ' chanses more')
        timeout = 10
        Ellipsis
        t = Timer(timeout, print, ['Sorry,times up'])
        t.start()
        answer = input('Answer : ')
        t.cancel()
        if answer == "BURJ KHALIFA":
            y = 0
totmarks = totmarks + marks

# ----------------------question 07---------------------
print('')
print(Fore.BLUE + 'Question 07')
time.sleep(0.5)

lines = [Fore.WHITE + 'What is the currency of Denmark?']  # DANISH KRONE
import time
import sys

for line in lines:  # Type writter Text
    for x in line:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.1)
    print('', )

from threading import Timer

timeout = 10
t = Timer(timeout, print, ['Sorry, times up!'])
t.start()
answer = input('Answer : ')
t.cancel()

import winsound

winsound.Beep(500, 1000)  # to add a Beep Sound

os.system('cls')  # Clearing the Screen
y = 3

if answer == "DANISH KRONE":
    marks = 10

while answer != "DANISH KRONE":
    while y > 1:
        lines = [Fore.RED + "Your Answer is Incorrect."]
        if y == 2:
            marks = 5
        elif y == 1:
            marks = 2

        winsound.Beep(300, 500)  # to add a Beep Sound
        for line in lines:
            for x in line:
                print(x, end='')
                sys.stdout.flush()
                time.sleep(0.1)
            print('', )
            y = y - 1
        print(Fore.BLUE + 'You have ', y, ' chanses more')
        timeout = 10
        t = Timer(timeout, print, ['Sorry,times up'])
        t.start()
        answer = input('Answer : ')
        t.cancel()
        if answer == "DANISH KRONE":
            y = 0
totmarks = totmarks + marks

# ----------------------question 08---------------------
print('')
print(Fore.BLUE + 'Question 08')
time.sleep(0.5)

lines = [Fore.WHITE + 'What is the closest planet to the Sun?']  # MERCURY
import time
import sys

for line in lines:  # Type writter Text
    for x in line:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.1)
    print('', )

from threading import Timer

timeout = 10
t = Timer(timeout, print, ['Sorry, times up!'])
t.start()
answer = input('Answer : ')
t.cancel()

import winsound

winsound.Beep(500, 1000)  # to add a Beep Sound

os.system('cls')  # Clearing the Screen
y = 3

if answer == "MERCURY":
    marks = 10

while answer != "MERCURY":
    while y > 1:
        lines = [Fore.RED + "Your Answer is Incorrect."]
        if y == 2:
            marks = 5
        elif y == 1:
            marks = 2

        winsound.Beep(300, 500)  # to add a Beep Sound
        for line in lines:
            for x in line:
                print(x, end='')
                sys.stdout.flush()
                time.sleep(0.1)
            print('', )
            y = y - 1
        print(Fore.BLUE + 'You have ', y, ' chanses more')
        timeout = 10
        t = Timer(timeout, print, ['Sorry,times up'])
        t.start()
        answer = input('Answer : ')
        t.cancel()
        if answer == "MERCURY":
            y = 0
totmarks = totmarks + marks

time.sleep(1)

os.system('cls')

print("Your total marks : ", totmarks)









































    
























