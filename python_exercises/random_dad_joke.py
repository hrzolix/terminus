import requests
import random

def search_for():
    topic = input("Let me tell you a joke. Give me the topic: ")
    return topic

def search_term(term):
    url = "https://icanhazdadjoke.com/search"

    response = requests.get(url,
        headers={"Accept": "application/json"},
        params ={"term": term})

    data = response.json()
    return data

def user_input(data):
    res = data
    if res["total_jokes"]>1:
        random_joke = random.choice(res['results'])
        print(f"I've got {res['total_jokes']} jokes about {res['search_term']}. Here is one: {random_joke['joke']}")
    elif res["total_jokes"] == 1:
        random_joke = random.choice(res['results'])
        print(f"I've got {res['total_jokes']} joke about fruit. Here is one: {random_joke['joke']}")
    else:
        print(f"Sorry, I have no jokes on term {res['search_term']}")


top = search_for()
data = search_term(top)
user_input(data)