
def containsDuplicate(nums):
    uniques = set(nums)
    if len(uniques) != len(nums):
        return True
    else:
        return False

print(containsDuplicate([1,2,3,4]))