def minRemoveToMakeValid(self, s: str) -> str:
        res=[]
        open_count=0
        for char in s:
            if char=='(':
                open_count+=1
                res.append(char)
            elif char==')':
                if open_count>0:
                    open_count-=1
                    res.append(char)
            else:
                res.append(char)
        final_res=[]
        for char in reversed(res):
            if char=='(' and open_count>0:
                open_count-=1
            else:
                final_res.append(char)
        return "".join(reversed(final_res))
