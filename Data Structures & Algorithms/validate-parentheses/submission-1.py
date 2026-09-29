class Solution:
    def isValid(self, s: str) -> bool:
        left_par = []
        
        for i in range(0, len(s)):
            # 1. If it's an opening bracket, just append it to the stack
            if s[i] == '(':
                left_par.append('(')
            elif s[i] == '[':
                left_par.append('[')
            elif s[i] == '{':
                left_par.append('{')

            # 2. If it's a closing bracket, check and pop
            elif s[i] == ')':
                # If stack is empty OR the popped element isn't its match, it's invalid
                if not left_par or left_par.pop() != '(':
                    return False

            elif s[i] == ']':
                if not left_par or left_par.pop() != '[':
                    return False
                
            elif s[i] == '}':
                if not left_par or left_par.pop() != '{':
                    return False
                
        # 3. If the stack is empty, all pairs matched perfectly
        return len(left_par) == 0
