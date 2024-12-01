#Create a function that takes a list of integers and returns the sum of all even numbers.
def cal_sum_of_even_numbers(numbers):
    even_sum = 0
    for num in numbers:
      if num % 2 == 0:
        even_sum += num
    return even_sum 


     
group_of_number = [10,100,30,50,20,40]
result = cal_sum_of_even_numbers(group_of_number)
print(f"The sum of even number for {group_of_number} is {result}")

