#Write a function to check weather a string is a palindrome.
def string_palindrome(s):
    normalized_str = ''.join(char.lower() for char in s if char.isalnum())
    return normalized_str == normalized_str [::-1]
   

string = "Ahmad is Ahmad"    
result = string_palindrome(string)
print(f"The {string} is {result} palindrome")
#  example 2
string = "civic"
result = string_palindrome(string)
print(f"The {string} is {result} palindrome")
