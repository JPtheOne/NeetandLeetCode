# Given an array of integers, return the indexes of the two elements that add the target.

def twoSum(nums,target):
    map = {}
    for idx, i in enumerate(nums):
        sub = target - i
        if sub in map:
            return(map[sub],idx)
        map[i]=idx

# Time Complexity: O(n)
# Space Complexity: O(n)

# Notes:
#  numbers are keys and their indexes are values
#  one addend is current number, the other is index of dictionary