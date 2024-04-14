import random

question = input('Enter your question: ')
answer = random.randint(1, 8)

if answer == 1:
    print('Yes - definitely.')
elif answer == 2:
    print('It is decidedly so.')
elif answer == 3:
    print('Without a doubt.')
elif answer == 4:
    print('Reply hazy, try again.')
elif answer == 5:
    print('Ask again later.')
elif answer == 6:
    print('Better not tell you now.')
elif answer == 7:
    print('My sources say no.')
else:
    print('Outlook not so good.')