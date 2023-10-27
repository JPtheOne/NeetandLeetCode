#Given a string with spaces, return length of last word
# Time and Space: =O(n)
def lastWord(s):
    ss = s.strip()
    a = ss.split(" ")
    return len(a)