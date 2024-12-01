#Create a function that takes a list of numbers and returns the largest number.
def find_largest_number(numbers):
    """Return the largest number from a list of numbers."""
    if not numbers:  # Check if the list is empty
        return None  # Return None if the list is empty

    largest = numbers[0]  

    
    for num in numbers:
        if num > largest:
            largest = num  

    return largest  

# Example usage
number_list = [100, 508, 90, 26, 28, -91]
largest_number = find_largest_number(number_list)
print(f"The largest number in the list is: {largest_number}")