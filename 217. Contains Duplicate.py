# Given an integer list, return true if duplicates exist.

def containsDuplicate(nums):
    uniques = set(nums)
    if len(uniques) != len(nums):
        return True
    else:
        return False

#TIme complexity: O(n)
#Space complexity: O(n)


