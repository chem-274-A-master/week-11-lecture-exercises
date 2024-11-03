"""
Context manager exercise.

Using a context manager

One context manager in the contextlib library is called redirect_stdout and it allows you to redirect standard output. 
You can learn more about it here (https://docs.python.org/3/library/contextlib.html#contextlib.redirect_stdout)

with contextlib.redirect_stdout(new_target):
  do things

Consider the noisy functions below. 

You should implement the function `suppress_output` that takes a function and its arguments as input and returns the result of 
the original function, but without printing anything to the console.
Use the redirect_stdout context manager to redirect the standard output to a string object so you don't have to see it. 
See the first example in the documentation for how to do this: https://docs.python.org/3/library/contextlib.html#contextlib.redirect_stdout
"""

# you will need to add some imports


def suppress_output(func, *args, **kwargs):
    
    # Create use the redirect_stdout context manager 
    # to redirect the standard output to a string object
    ret = func(*args, **kwargs)

    # This function needs to return the same
    # value as the original function
    return ret

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
    
    # Main for demonstration

    # This will print a lot of stuff
    value = noisy_sum_squared(10)

    # This will suppress the output
    value = suppress_output(noisy_sum_squared, 10)

    # Suppress output of noisy_factorial
    factorial = suppress_output(noisy_factorial, value)

    print(f"Done! The factorial is {factorial}")
