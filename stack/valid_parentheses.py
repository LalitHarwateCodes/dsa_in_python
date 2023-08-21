# def isValidParentheses(s: str) -> bool:
#     stack = []
#     mapping = {')': '(', '}': '{', ']': '['}

#     for char in s:
#         if char in mapping:
#             if not stack:
#                 return False
#             top_element = stack.pop()
#             if mapping[char] != top_element:
#                 return False
#         else:
#             stack.append(char)
#     return not stack

# print(isValidParentheses("(})"))


def validParentheses(s:str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            if not stack:
                return False
            top_element = stack.pop()
            if top_element != mapping[char]:
                return False
        else:
            stack.append(char)
    return not stack

print(validParentheses("()"))
