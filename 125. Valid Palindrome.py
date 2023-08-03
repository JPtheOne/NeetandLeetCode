#Given a string, return True if its a palindrome
def isPalindrome(self, s: str) -> bool:
    s2 = s.lower()
    normal=[]
    for i in list(s2):
        if i.isalnum():
            normal.append(i)

    reversed = normal[::-1]

    if normal == reversed:
        return True
    
# Time complexity=O(n)
# Space complexity=O(n)