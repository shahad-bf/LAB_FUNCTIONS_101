def print_pattern(n: int):
    
    """ this function that takes 1 parameter of type int , 
    then it prints out the result formatted like the following pattern """
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=' ')
        print()


print(print_pattern.__doc__)


while True:
    num = int(input("Enter a integer number: "))
    if num > 0:
        break 
    print("Please enter a positive number ")

print_pattern(num)