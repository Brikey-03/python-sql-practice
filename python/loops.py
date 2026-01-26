# Function to check whether a number is even
def is_even(num):
    return num % 2 == 0
# Loop through numbers from 1 to 10 and classify each number
for i in range(1, 11):
    if is_even(i): 
        print(i, "is even")
    else:
        print(i, "is odd")
