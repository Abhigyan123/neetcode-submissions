class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score=[]
        k=-1
        # final_score = 0
        # print(int(operations[0])+int(operations[1]))
        for i in operations:
            if i=="+":
                sum_last_2 =int(score[k])+int(score[k-1])
                score.append(sum_last_2)
                k=k+1
                # print(score)
            
            elif i=="C":
                del score[k]
                k=k-1
                # print(score)
            
            elif i=="D":
                score.append(2*int(score[k]))
                k=k+1
                # print(score)
            
            else:
                score.append(int(i))
                k=k+1
                # print(score)

        return sum(score)

                
        