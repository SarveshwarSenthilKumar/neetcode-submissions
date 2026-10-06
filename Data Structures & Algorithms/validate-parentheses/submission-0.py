class Solution:
    def isValid(self, s: str) -> bool:
        brackets="()[]{}"
        openBrackets=[]
        for bracket in s:
            if (brackets.index(bracket)+1)%2!=0:
                openBrackets.append(bracket)
            else:
                if (brackets[brackets.index(bracket)] == openBrackets[-1]):
                    openBrackets = openBrackets[:-1]
                else:
                    return False