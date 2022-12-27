## Fibinaci Exercise
def fib(num):
  x = 0
  y = 1

  for i in range(num):
    yield x
    temp = x
    x = y
    y = temp + y

def fib2(num):
  x = 0
  y = 1
  result = []
  for i in range(num):
    result.append(x)
    temp = x
    x = y
    y = temp + y
  return result
    
# for x in fib(20):
#   print(x)

print(fib2(20))

## Example of how range works

# class MyGen():
#   current = 0
#   def __init__(self, first, last):
#       self.first = first
#       self.last = last

#   def __iter__(self):
#     return self

#   def __next__(self):
#     if MyGen.current < self.last:
#       num = MyGen.current
#       MyGen.current +=1
#       return num
#     raise StopIteration
  
# gen = MyGen(0,100)
# for i in gen:
#   print(i)


## second generator example

# def special_for(iterable):
#   iterator = iter(iterable)
#   while True:
#     try:
#       print(iterator)
#       print(next(iterator)*2)
#     except StopIteration:
#       break

# special_for([1,2,3])

## first generator example

# def generator_function(num):
#   for i in range(num):
#      yield i*2

# g = generator_function(100)

# next(g)
# next(g)
# print(next(g))