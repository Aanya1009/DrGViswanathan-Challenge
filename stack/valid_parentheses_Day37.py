def isValid(self, s: str) -> bool:
        stack=[]
        bracket_map={")":"(", "]":"[", "}":"{"}
        for bracket in s:
            if bracket in bracket_map:
                top=stack.pop() if stack else "#"
                if bracket_map[bracket]!=top:
                    return False
            else:
                stack.append(bracket)
        return len(stack)==0
