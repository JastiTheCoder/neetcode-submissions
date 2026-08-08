class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        matching = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for brac in s:
            if brac in '[{(':
                stack.append(brac)
            else:
                if not stack or stack[-1] != matching[brac]:
                    return False
                stack.pop()
                    
        return len(stack) == 0
