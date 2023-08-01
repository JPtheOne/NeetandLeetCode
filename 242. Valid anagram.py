# Given two strings, check if they are anagrams.

def isAnagram(s,t):
    return sorted(s)==sorted(t)
# Time complexity: O(nlogn) using Timsort
# Space complexity: =O(n)

#The following commented code was proposed as solution, but is not an optimized solution
'''
sf = list(s)
tf = list(t)
r1={}
r2={}

for letter in sf:
    r1[letter]=sf.count(letter)

for letter in tf:
    r2[letter]=tf.count(letter)

return r1==r2
'''