class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercase = [chr(i) for i in range(ord('a'), ord('a') + 26)]
        uppercase = [chr(i) for i in range(ord('A'), ord('A') + 26)]
        
        letters = lowercase + uppercase
        numbers = [str(i) for i in range(10)]
        
        characters = letters + numbers

        t_list = []
        for c in s:
            if c not in characters:
                continue
            if c in uppercase:
                i = uppercase.index(c)
                t_list.append(lowercase[i])
            else:
                t_list.append(c)
        
        t = ''.join(t_list)
        
        for i in range(len(t)):
            j = len(t) - 1 - i
            if t[i] != t[j]:
                return False
        return True
