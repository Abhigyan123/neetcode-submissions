class Solution:
    def isValid(self, s: str) -> bool:
        left_par = []
        right_par = []
        c_1=0
        c_2=0
        c_3=0
        str_len = len(s)
        k =-1
        for i in range(0,str_len):
            if s[i]=='(':
                c_1=c_1+1
                left_par.append('(')
                k=k+1
            elif s[i]=='[':
                c_2=c_2+1
                left_par.append('[')
                k=k+1
            elif s[i]=='{':
                c_3=c_3+1
                left_par.append('{')
                k=k+1

            elif s[i]==')':
                c_1=c_1-1
                # FIXED: Check if k == -1 first to prevent crash
                if k == -1 or left_par[k] != '(':
                    return False
                del left_par[k]
                k=k-1

            elif s[i]==']':
                c_2=c_2-1
                # FIXED: Check if k == -1 first to prevent crash
                if k == -1 or left_par[k] != '[':
                    return False
                del left_par[k]
                k=k-1
                
            elif s[i]=='}':
                c_3=c_3-1
                # FIXED: Check if k == -1 first to prevent crash
                if k == -1 or left_par[k] != '{':
                    return False
                del left_par[k]
                k=k-1
                
        # FIXED: Fixed the underscores in the variables
        if c_1 + c_2 + c_3 == 0:
            return True
        else:
            return False
