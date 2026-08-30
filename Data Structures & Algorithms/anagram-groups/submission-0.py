class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for word in strs:
            signature = "".join(sorted(word))
            if signature not in anagram_map:
                anagram_map[signature] = []
            anagram_map[signature].append(word)
        return list(anagram_map.values())

        