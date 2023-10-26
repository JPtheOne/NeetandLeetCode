nums = [0,1,2,2,3,0,4,2]
val = 2

for idx, num in enumerate(nums):
    if num ==val:
        nums[idx]=None
print(nums)

k = []
for element in nums:
    if element != None:
        k.append(element)
print(len(k))
