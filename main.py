#Data 

user_name = input('Enter User Name: ')
password = input('Enter Password: ')

pass_hidden = '*' * len(password)

print(f'{user_name}, your password {pass_hidden} is {len(password)} letter long')
