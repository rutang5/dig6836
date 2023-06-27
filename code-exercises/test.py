import random

print("Hello, World!")

def sayHi():
    print("Hi!")

def sayBye():
    print("Bye!")


def displayRandomQuote():
    quotes = ["Quote 1", "Quote 2", "Quote 3"]
    randomQuote = random.randint(0, len(quotes) - 1)
    print(quotes[randomQuote])

sayHi()
displayRandomQuote()

