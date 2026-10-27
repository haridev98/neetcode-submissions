class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for el in s:
            if el not in dict_s:
                dict_s[el] = 1
            else:
                dict_s[el] += 1
        for el in t:
            if el not in dict_t:
                dict_t[el] = 1
            else:
                dict_t[el] += 1

        if len(dict_t.keys())!=len(dict_s.keys()):
            return False
        else:
            for i in dict_t.keys():
                if i not in dict_s.keys():
                    return False
                elif dict_t[i] != dict_s[i]:
                    return False
        return True