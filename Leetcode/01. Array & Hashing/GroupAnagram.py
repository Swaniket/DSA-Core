from collections import defaultdict

def groupAnagrams(strs):
    hMap = defaultdict(list)

    for word in strs:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord("a")] += 1

        hMap[tuple(count)].append(word)

    return hMap.values()

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(groupAnagrams(strs))

