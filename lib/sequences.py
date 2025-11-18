#!/usr/bin/env python3

def print_fibonacci(length):

    if not isinstance(length, int) or length < 0:
        print("Error: Length must be a non-negative integer.")
        return
    
    if length == 0:
        fib_list = []
    elif length == 1:
        fib_list = [0]
    else:
        #start with the first two numbers of the sequence
        fib_list = [0, 1]
        while len(fib_list) < length:
            next_num = fib_list[-1] + fib_list[-2]
            fib_list.append(next_num)

    print(fib_list)


    

