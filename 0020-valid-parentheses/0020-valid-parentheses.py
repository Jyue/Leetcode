class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2: return False # Rule out odd length string
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for bracket in s:
            # Close brackets
            if bracket in dict: 
                if len(stack) == 0 or dict[bracket] != stack.pop():
                    return False
            # Open brackets (assume all the characters are from the valid types to skip the lookup on the values)
            else:
                stack.append(bracket)
        return len(stack) == 0
                    