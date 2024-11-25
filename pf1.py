#Task 1 Swap X and Y without Temp
def swap (x, y):
    if isinstance(x,(int,float)) and isinstance(y,(int,float)): #determine if x and y is numeric
        x, y = y, x #swap the value of x and y
        print(f'afterswap: x = {x}, y = {y}') #to print swapped value if x and y is numeric
    else:
        return -1 # Return -1 if either value is not numeric

#Task 2 Swap (Apple,10)

result = swap("Apple",10) #swap value of Apple and 10
if result == -1: #check if results value is returned as -1
    print('afterswap: -1')

#Task 2 Swap 9, 17
result = swap(9,17)