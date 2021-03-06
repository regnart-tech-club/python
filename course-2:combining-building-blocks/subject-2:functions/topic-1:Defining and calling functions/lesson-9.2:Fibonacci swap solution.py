# The Fibonacci sequence starts with 0 and 1. Subsequent terms are then gotten by adding the previous two
# such that the first nine terms are: 0, 1, 1, 2, 3, 5, 8, 13, 21.

# Write a function that, given an integer n, returns the nth Fibonacci number.
# For example:
# given n = 0, the function should return 0
# if n = 1, it should return 1
# if n = 2, it should return 1
# if n = 4, it should return 3
# if n = 8, it should return 21
def fibonacci(n):
  # Define two variables to hold interim values and initialize them.
  f0 = 0
  f1 = 1
  
  # Iterate `n` times.
  for i in range(n):
    # Calculate the next value.
    f0 = f0 + f1
  
    # Swap `f0` and `f1` values.
    f0 = f0 ^ f1
    f1 = f1 ^ f0
    f0 = f0 ^ f1
    
  # Return the result.
  return f0

if fibonacci(0) == 0:
  print('Thumbs up.')
else:
  print('Thumbs down.')

if fibonacci(1) == 1:
  print('Thumbs up.')
else:
  print('Thumbs down.')

if fibonacci(2) == 1:
  print('Thumbs up.')
else:
  print('Thumbs down.')

if fibonacci(3) == 2:
  print('Thumbs up.')
else:
  print('Thumbs down.')

if fibonacci(4) == 3:
  print('Thumbs up.')
else:
  print('Thumbs down.')

if fibonacci(5) == 5:
  print('Thumbs up.')
else:
  print('Thumbs down.')

if fibonacci(6) == 8:
  print('Thumbs up.')
else:
  print('Thumbs down.')
