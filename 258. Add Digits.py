# Sum digits of num until it's a single digit
# O(1) for time and space 
def addDigits(num):
    return (num-1)%9 +1 if num else 0