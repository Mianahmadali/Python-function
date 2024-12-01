#Write a function to find the nth Fibonacci number using recursion.
def nth_Fibonacci_number(n):
    if n == 0 :
     return 0
    elif n==1:
     return 1
    else:
          a, b = 0, 1
    for _ in range(2, n + 1):
            a, b = b, a + b
    return b
         # Recursive case
        # return nth_Fibonacci_number(n - 1) + nth_Fibonacci_number(n - 2)
n = 70
Fibonacci = nth_Fibonacci_number
print(f"The nth Fibonacci of {n} is {Fibonacci(n)}")





