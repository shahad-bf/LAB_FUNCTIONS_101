def get_pattern(n: int) -> str:
    
    """ Rewrite the previous function so that it returns the pattern as a string,
    then assign the result to a variables and print it  """
    
    pattern = ""
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            pattern += str(j) + " "
        pattern += "\n"
    return pattern


# print Documents
print(get_pattern.__doc__)

while True:
    try:
        num = int(input("Enter a positive integer: "))
        if num > 0:
            break
        else:
            print("Please enter a positive number only!")
    except ValueError: # If the user enters something that's not a number
        print("Please enter a valid number ")

# Calling function
result = get_pattern(num)

# print pattren
print("\nGenerated Pattern:\n")
print(result)