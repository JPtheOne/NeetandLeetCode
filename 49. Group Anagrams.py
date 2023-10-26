# Given a list of words, group in tuples by anagram.
def groupAnagrams(strs):
    anagrams = {}

    for word in strs:
        occurences = []
        for letter in word:
            amount = word.count(letter)
            occurence = (letter,amount)
            occurences.append(occurence)

        key = tuple(sorted(occurences))

        if key not in anagrams:
            anagrams[key] = []

        anagrams[key].append(word)

    return anagrams.values()

# Time complexity O(nk^2)
# Space complexity O(nk)
# Where K is the number of letters per word