# ====================================
#     System Login / Register Tool
#     Access your music securely 🎵
# ====================================
import pygame

#LOGIN / REGISTER
users_list = [{
    'oi': 'ooii'
}]
user = {
    'username': 'Ana',
    'password': 'Hello'
}

#Functions

def signin():
    user['username'] = input('Username: ')
    user['password'] = input('Password: ')

    for i in users_list:
        for k, v in i.items():
            if v == user['username']:
                print('Existing user')
                break#TOP HER


def central():
    user['username'] = input('Username: ')
    user['password'] = input('Password: ')


def lines():
    print('-' * 15)

def scanning():
    for i in users_list:
        for _ in i.items():
            if _[1] == user['username']:
                print('Existing user')





#User selection
selection = int(input('''[ 1 ] SIGN IN
[ 2 ] LOG IN
> '''))

#Conditions
if selection == 1:
    lines()
    print('SIGN IN'.center(15))
    lines()
    # users_list.append(user.copy())
    # central()
    # scanning()
    signin()

elif selection == 2:
    lines()
    print('LOG IN'.center(15))
    lines()
    central()
    scanning()



#Corrigir
