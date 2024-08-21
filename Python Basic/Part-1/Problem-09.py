# Prompt the user to input an integer and store it in the variable 'a'
a = int(input("Input an integer: "))

# Create new integers 'n1', 'n2', and 'n3' by concatenating 'a' with itself one, two, and three times, respectively
n1 = int(f"{a}")           
n2 = int(f"{a}{a}")        
n3 = int(f"{a}{a}{a}")  

# Calculate the sum of 'n1', 'n2', and 'n3'
result = n1 + n2 + n3

# Print the result
#print("The result of the concatenation and sum is:", result) 
print(f"The result of sum is {result}")

