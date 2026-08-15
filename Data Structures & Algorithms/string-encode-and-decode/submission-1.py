class Solution:

    def encode(self, strs: list[str]) -> str:
        ret=''
        for string in strs:
            ret = ret+str(len(string))+"#"+string
            #print (ret)
        return ret


    def decode(self, s: str) -> list[str]:
        ret_list=[]
        #string=''
        i=0
        while i < len(s):
            j = i
            #print(f"jil:{j}")
            while s[j]!='#':
                j+=1
                #print(f"jeer:{j}")
            
            length = int(s[i:j])
            ret_list.append(s[j+1:j+1+length])
            #print(s[j+1:j+1+length])
            i=j+1+length
        return ret_list