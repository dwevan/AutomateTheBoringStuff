def spam(divby):
    try:
        return 42 / divby
    except ZeroDivisionError:
        print('Error, you wont kill me that easily')


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
