class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if stack:
                if (stack[-1] == '(' and c == ')') or \
                   (stack[-1] == '{' and c == '}') or \
                   (stack[-1] == '[' and c == ']'):
                   stack.pop()
                else:
                    stack.append(c)
            else:    
                stack.append(c)
        
        return len(stack) == 0