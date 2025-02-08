# ---7. Find the second largest number in a list.

def second_largest(numbers):
    first, second = float('-inf'), float('-inf')

    for num in numbers:
        if num > first:
            second, first = first, num  
        elif num > second and num != first:
            second = num  

    return second if second != float('-inf') else "No second largest number"

numbers = [10, 20, 4, 45, 90, 99]
print("Second largest number:", second_largest(numbers))
