# ---4. Convert a decimal number to its binary representation.

n = float(input("Enter a decimal number: "))  
integer_part = int(n)  # Convert only the integer part  
binary_representation = bin(integer_part)[2:]  
print(f'Binary representation of the integer part ({integer_part}) is: {binary_representation}')  

