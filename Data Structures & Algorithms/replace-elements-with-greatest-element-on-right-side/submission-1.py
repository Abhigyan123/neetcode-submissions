class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_seen =arr[len(arr)-1]
        for i in range(len(arr)-2,-1,-1):
            current = arr[i]
            arr[i] = max_seen
            if current>max_seen:
                max_seen = current
            
        arr[len(arr)-1]=-1
        return  arr

