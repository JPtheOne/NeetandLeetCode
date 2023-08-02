strs = ["eat","tea","tan","ate","nat","bat"]
letters = []
for i in strs:
    new = tuple(sorted(i))
    letters.append(new)
uniques = set(letters)
print(uniques)