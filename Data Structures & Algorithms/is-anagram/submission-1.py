class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}

        for char in s:
            my_dict[char] = my_dict.get(char, 0) + 1

        for char in t:
            my_dict[char] = my_dict.get(char, 0) - 1

        for count in my_dict.values():
            if count != 0:
                return False

        return True

        
        