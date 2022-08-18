from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = dict(sorted(dict(Counter(arr)).items(), key=lambda item: item[1],  reverse=True))
        if len(set(arr)) == 1:
            return 1
        arr_len = len(arr)
        res = arr_len
        count = 0
        for k, v in counter.items():
            if res > (arr_len / 2):
                res -=  v
                count += 1
            else:
                return count
            
            


        