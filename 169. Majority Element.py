# Using Moore Algorithm to find most repeated element

#Should remain in O(n) for both space and time
def majority_element(nums):
    candidate, count = nums[0], 1

    # First pass: find a candidate for majority element
    for num in nums[1:]:
        if count == 0:
            candidate = num
            count = 1
        elif candidate == num:
            count += 1
        else:
            count -= 1

    # Second pass: verify if candidate is indeed the majority element
    count = 0
    for num in nums:
        if num == candidate:
            count += 1
    if count > len(nums) // 2:
        return candidate
    else:
        return None  # No majority element

print(majority_element([6,5,5]))
