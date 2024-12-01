#Write a function to count the vowels in a given string.
def count_vowels(s):
    """Count the number of vowels in a given string."""
    vowels = "aeiouAEIOU"  # Define the vowels (both lowercase and uppercase)
    count = 0  # Initialize a counter for vowels


    for char in s:
        if char in vowels:
            count += 1  

    return count  
input_string = "Mian Ahmad Ali"
vowel = count_vowels(input_string)
print(f"The vowel in {input_string} is {vowel}")


