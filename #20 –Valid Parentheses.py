class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')':'(', '}':'{', ']':'['}
        
        for char in s:
            if char in mapping.values():  
                stack.append(char)
            else:  
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        
        return not stack 
