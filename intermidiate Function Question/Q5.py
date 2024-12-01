#Write a Function to calculate the GcD( Greatest Common Divisor) of two numbers.
def gcd(a,b):
    while b != 0:
        a,b = b, a % b
         
    return a

a = 80 
b = 60
result = gcd(a,b)  
print(f"The GCD of {a} and {b} is {result}")


