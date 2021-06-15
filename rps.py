# Write your code here
import random

choices = ['rock', 'paper', 'scissors']

def get_input(choices) -> str:
    #print(choices,'?')
    return input()

print('Enter your name:', end='')
print('Hello, {}'.format(name := input()))

with open('rating.txt', 'r') as ratings:
    score = 0
    for line in ratings:
        if line.split()[0] == name:
            score = int(line.split()[1])

print('Enter the various choices:', end='')
new_choices = input()
if new_choices != '':
    choices = new_choices.split(',')

print("Okay, let's start!")

while (user_choice := get_input(choices)) != '!exit':
    if user_choice == '!rating':
        print('Your rating: {}'.format(score))

    if user_choice not in choices:
        print('Invalid input')
        continue

    computer_choice = random.choice(choices)

    index = choices.index(user_choice)
    sorted_choices = choices[index+1:] + choices[:index]
    beats_user_choice = sorted_choices[:len(sorted_choices)//2]
    loses_to_user_choice = sorted_choices[len(sorted_choices)//2:]

    if user_choice == computer_choice:
        print('There is a draw ({})'.format(user_choice))
        score += 50
    elif computer_choice in beats_user_choice:
        print('Sorry, but the computer chose {}'.format(computer_choice))
    else:
        print('Well done. The computer chose {} and failed'.format(computer_choice))
        score += 100

print('Bye!')
exit()
