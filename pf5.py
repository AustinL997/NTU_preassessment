#Task 1:
def check_divisibility(num, divisor):
    if isinstance(num,(int,float)) and  isinstance(divisor,(int,float)):
        return num % divisor == 0
    else:
        return False

#Task 2
print(check_divisibility(10,2)) #should return true

print(check_divisibility(7,3)) #should return false