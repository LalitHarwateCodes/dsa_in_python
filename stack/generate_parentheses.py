# class Solution:


#     def parentheses(self,n):
#         stack = []
#         res= []

#         def backtrack(open,close):
#             if open == close == n:
#                 res.append(' '.join(stack))
#                 return
            

#             if open < n:
#                 stack.append('(')
#                 backtrack(open+1,close)
#                 stack.pop()

#             if close < open:
#                 stack.append(')')
#                 backtrack(open,close+1)
#                 stack.pop()

#         backtrack(0,0)
#         return res
    
# sol = Solution()
# print(sol.parentheses(1))

class Solution:

    def parentheses(self,n):
        res = []
        stack = []

        def backtrack(open,closed):
            if open == closed == n:
                res.append(" ".join(stack))
                return
            
            if open < n:
                stack.append("(")
                backtrack(open+1,closed)
                stack.pop()

            if closed < open:
                stack.append(')')
                backtrack(open,closed+1)
                stack.pop()

        
        backtrack(0,0)
        return res
    
sol = Solution()
print(sol.parentheses(2))   


                