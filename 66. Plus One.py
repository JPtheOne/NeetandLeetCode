#Given an int in list, return int +1 
#Space and Time complexity: O(n)

def plusOne(digits):
    s = [str(integer) for integer in digits]
    a_string = "".join(s)
    res = int(a_string)+1
    answer = [int(i) for i in str(res)]
    return answer

