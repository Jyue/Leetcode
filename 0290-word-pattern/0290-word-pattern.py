class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        match_list = {}
        substrings = s.split()
        if len(substrings) != len(pattern):
            return False
        for i in range(len(substrings)):
            if pattern[i] not in match_list.values():
                if (substrings[i] in match_list):
                    return False
                else:
                    match_list[substrings[i]] = pattern[i]
            elif((substrings[i] not in match_list)):
                return False
            elif((match_list[substrings[i]] != pattern[i])):
                return False
        return True
            