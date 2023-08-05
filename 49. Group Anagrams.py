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