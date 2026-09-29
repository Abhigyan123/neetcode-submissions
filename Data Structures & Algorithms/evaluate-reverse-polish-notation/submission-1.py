class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+','-','*','/']
        op=0
        eval = []
        eval_len = -1
        for t in range(0,len(tokens)):
            if tokens[t] == '+':
                op = int(eval.pop(len(eval)-2))+int(eval.pop(len(eval)-1))
                eval.append(int(op))
            elif tokens[t] == '-':
                op = int(eval.pop(len(eval)-2))-int(eval.pop(len(eval)-1))
                eval.append(int(op))  
            elif tokens[t] == '*':
                op = int(eval.pop(len(eval)-2))*int(eval.pop(len(eval)-1))
                eval.append(int(op))
               
            elif tokens[t] == '/':
                op = int(eval.pop(len(eval)-2))/int(eval.pop(len(eval)-1))
                eval.append(int(op))
            else:
                eval.append(int(tokens[t]))      
        return (eval[0])