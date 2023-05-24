class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for bracket in s:
            # Close brackets
            if bracket in dict: 
                if stack == [] or dict[bracket] != stack.pop():
                    return False
            # Open brackets (assume all the characters are from the valid types to skip the lookup on the values)
            else:
                stack.append(bracket)
        return stack == []
                    