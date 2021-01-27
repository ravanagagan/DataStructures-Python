# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user
# using input() function

odd_numbers = []
MAX_SIZE = int(input("Enter the MAX_SIZE till you want to print the odd numbers: \n"))
for i in range(1, MAX_SIZE+1):
    if not (i % 2 == 0):
        odd_numbers.append(i)

print(odd_numbers)
