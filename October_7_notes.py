# def sum_numbers_rec(n):
#     #X /\ base case: when we get to 1 shut it down
#     if n == 1:
#         return n
    
#     return n + sum_numbers_rec(n-1) #5+4+3+2+1


# print(sum_numbers_rec(100))

# #factorial recursive

# def factorial_rec(n):
#     #X /\ base case: when we get to 1 shut it down
#     if n == 0:
#         return 1
    
#     return n * factorial_rec(n-1) #5+4+3+2+1

# print(factorial_rec(100))

#fibonaci
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fib(n-1) + fib(n-2)

print(fib(10))
