# Given a CORRECT roman number in str, convert it to integer.
def romantoInt(s):
    translation = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
    }

    addends = []
    total=0

    for i in range(len(s)):
        value = translation.get(s[i])
        addends.append(value)

    for i in range(len(addends)-1):  
        if addends[i]>=addends[i+1]:
            total += addends[i]
        else:
            total -= addends[i]
    total += addends[-1]
    return total

# Time complexity=O(n)
# Space complexity=O(n)
