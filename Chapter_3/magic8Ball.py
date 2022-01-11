import random


def get_answer(answer_number):
    if answer_number == 1:
        return 'It is certain'
    elif answer_number == 2:
        return 'It is so'
    elif answer_number == 3:
        return 'Yes'
    elif answer_number == 4:
        return 'reply hazy..try again'
    elif answer_number == 5:
        return 'ask again later'
    elif answer_number == 6:
        return 'concentrate and ask again'
    elif answer_number == 7:
        return 'My reply is no'
    elif answer_number == 8:
        return 'Outlook not so good'
    elif answer_number == 9:
        return 'Very doubtful'


r = random.randint(1, 9)
fortune = get_answer(r)
print(fortune)

print('hello', end=' ')
print('world')

print('cats', 'mice', 'dogs', sep=' & ')
print('boots', 'cats', sep=' & ')
