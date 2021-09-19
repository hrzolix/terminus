import random
import requests
import datetime



def random_trivia():

    q1 = input('Do you wish to write a specific number or get a random trivia? ')
    if q1.isnumeric():
        q1 = int(q1)
        url = f'http://numbersapi.com/{q1}'
        response = requests.get(url)
        print(f'Here is a random fact about {q1}: \n{response.text}')
    else:
        q1 = random.randint(0,10000)
        url = f'http://numbersapi.com/{q1}'
        response = requests.get(url)
        print(f'Here is a random fact about {q1}: \n{response.text}')


def random_math():
    q1 = input('Do you wish to write a specific number or get a random math fact? ')
    if q1.isnumeric():
        q1 = int(q1)
        url = f'http://numbersapi.com/{q1}/math'
        response = requests.get(url)
        print(f'Here is a random fact about {q1}: \n{response.text}')
    else:
        q1 = random.randint(0,10000)
        url = f'http://numbersapi.com/{q1}/math'
        response = requests.get(url)
        print(f'Here is a random fact about {q1}: \n{response.text}')


def random_year():
    q1 = input('Do you wish to write a specific year or a get a random year fact? ')
    if q1.isnumeric():
        q1 = int(q1)
        url = f'http://numbersapi.com/{q1}/year'
        response = requests.get(url)
        print(f'Here is a random fact about {q1}: \n{response.text}')
    else:
        q1 = random.randint(0,2000)
        url = f'http://numbersapi.com/{q1}/year'
        response = requests.get(url)
        print(f'Here is a random fact about {q1}: \n{response.text}')




def random_date_fact():
    q1 = input ('Do you wish to write a specific date or a get a random date fact? ')
    if '/' in q1:
        url = f'http://numbersapi.com/{q1}/date'
        response = requests.get(url)
        print(f'Here is a random fact about {q1}: \n{response.text}')
    else:
        q1 = random.randint(0,2000)
        url = f'http://numbersapi.com/{q1}/year'
        response = requests.get(url)
        print(f'Here is a random fact about todays date {datetime.datetime.today()}: \n{response.text}')

random_trivia()
random_date_fact()
random_math()
