#Write a function to find the factorial of a number using recursion.
def cal_factorial(num):
    if num < 0:
     raise ValueError
    elif num == 0:
        return 1
    else:
        return num * cal_factorial (num - 1) 

num = 160
result = cal_factorial(num)
print (f"The fecturial of {num} is {result}")

  