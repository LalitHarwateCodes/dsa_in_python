def simplifyPath(path: str) -> str:
    # stack = []
    # parts = path.split('/')
    # print(parts)
    # for part in parts:
    #     if part == "..":
    #         if stack:
    #             stack.pop()
    #     elif part and part != '.':
    #         stack.append(part)
    # return '/' + '/'.join(stack)

# print(simplifyPath('/..//home/./user/../'))

    stack = []

    parts = path.split('/')

    for part in parts:
        if part == "..":
            if stack:
                stack.pop()
        elif part and part != '.':
            stack.append(part)
    return '/'+'/'.join(stack)   

print(simplifyPath('/..//home/./user//'))