def reverse(self, x: int) -> int:
        INT_MAX=(2**31)-1
        INT_MIN=-2**31
        sign=-1 if x<0 else 1
        num=abs(x)
        rev=0
        while num!=0:
            digit=num%10
            num//=10
            rev=rev*10+digit
        if rev>INT_MAX or rev<INT_MIN:
            return 0
        return sign*rev
        