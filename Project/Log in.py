#sistem login / register

#LOGIN / REGISTER
users_list = []



selection = int(input('''[ 1 ] SIGN IN
[ 2 ] LOG IN
> '''))


def lines():
    print('-' * 15)

if selection == 1:
    lines()
    print('SIGN IN'.center(15))
    lines()
    user = {
        'username': input('Username: ' ),
        'password': input('Password: ')
    }
    users_list.append(user)
    if user['username']
elif selection == 2:
    lines()
    print('LOG IN'.center(15))
    lines()
print(users_list)