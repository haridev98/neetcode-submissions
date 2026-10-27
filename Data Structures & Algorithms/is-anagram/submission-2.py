class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        for el in s:
            if el not in dict_s:
                dict_s[el] = 1
            else:
                dict_s[el] += 1


        for el in t:
            if el not in dict_s or dict_s[el] == 0:
                return False
            dict_s[el]-=1
        for val in dict_s.values():
            if val>0:
                return False
        return True
            