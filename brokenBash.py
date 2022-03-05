#!/bin/python3
print('Hello, what is your name?')

name = input'Name: '

print('Nice to meet you, ' name + '.')

numList = [int(x) for x in input('What are your favorite numbers? (Separate multiple numbers with a space.)').split()]
numList.sort()

print('Here are your favorite numbers:')

for x in numList:
    print(x)
else
    print('Thank you for sharing your favorite numbers!')
