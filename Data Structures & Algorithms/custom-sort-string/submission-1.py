class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        count = {}
        result = []
        for o in s:
            if o in count:
                count[o]+=1
            else:
                count[o]=1
        for i in order:
            if i in count:
                result.append(i*count[i])
                count[i] = 0
        for i in count.keys():
            if count[i] > 0:
                result.append(i*count[i])
            
        return "".join(result)


             

        