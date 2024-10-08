
class ParenthesesValidator:
    def __init__(self,s:str):
        self.s=s
    def is_valid(self) -> bool :
        matching_brackets={')' : '(','}': '{', ']' : '['}
        stack=[]

        for char in self.s:
            if char in matching_brackets:
                top_element=stack.pop() if stack else '#'
                if matching_brackets[char] != top_element:
                    return false
            else:
                stack.append(char)

         return not stack

# example
#print(is_valid_parentheses("()"))







    



  

