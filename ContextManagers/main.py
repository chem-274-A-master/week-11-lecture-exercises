"""
Context manager exercise.

Using a context manager

One context manager in the contextlib library is called redirect_stdout and it allows you to redirect standard output. (https://docs.python.org/3/library/contextlib.html#contextlib.redirect_stdout)

with contextlib.redirect_stdout(new_target):
  do things

Consider the noisy functions below. Use the redirect_stdout context manager to redirect the standard output to a string object so you don't have to see it. See the first example in the documentation for how to do this: https://docs.python.org/3/library/contextlib.html#contextlib.redirect_stdout

Leave the print statement starting with "Done"
"""

def noisy_sum_squared(n):

  print(f"I am starting a loop with {n} elements!")
  
  total = 0
  for i in range(n):
    print(f"I am on number {i}")
    i_squared = i ** 2
    print(f"i squared is {i_squared}")
    total += i_squared
    print(f"The total is now {total}")

  print("I am returning the value!")
  print("Here it is:")
  return total

def noisy_factorial(n):
  print(f"n is now {n}")
  if n == 0:
    return 1
  else:
    print("Calling factorial!")
    return n * noisy_factorial(n-1)

if __name__ == '__main__':

  value = noisy_sum_squared(10)

  factorial = noisy_factorial(value)

  print(f"Done! The factorial is {factorial}")

