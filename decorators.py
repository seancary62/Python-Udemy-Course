from time import time

def performance(fn):
  def wrapper(*args,**kwargs):
    t1 = time()
    fn(*args,**kwargs)
    t2 = time()
    print(f'This took {t2-t1} ms')
  return wrapper
# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
# user1 = {
#     'name': 'Sorna',
#     'valid': True #changing this will either run or not run the message_friends function.
# }

# def authenticated(fn):
#   def wrapper(*args, **kwargs):
#     if kwargs.get('valid'):
#       fn(kwargs)
#     else:
#       print('no no')
#   return  wrapper

 
# @performance
# @authenticated
# def message_friends(user):
#     print('message has been sent')

# message_friends(user1)

user1 = {
    'name': 'Sorna',
    'valid': False
}
user2 = {
    'name': 'Mike',
    'valid': True
}

def authenticated(fn):
  def wrapper(*args, **kwargs):
    for user in args:  
        if user['valid']:
            print(f'\nUser: { user["name"] }')
            fn(user)
  return wrapper
  
@performance
@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1, user2)