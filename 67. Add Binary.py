# Given two binary strings, return sum as binary string
def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]

# Time O(n+m)
# Space O(n+m)
