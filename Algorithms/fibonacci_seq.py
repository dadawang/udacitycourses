"""Implement a function recursivly to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions."""

def get_fib(position):
    first = 0
    second = 1
    if position == 0:
        return first
    elif position == 1:
        return second
    elif position > 1:
        first = get_fib(position - 2)
        second = get_fib(position - 1)
        fib_sum = first + second
        return fib_sum
    else:
        return -1

# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)
