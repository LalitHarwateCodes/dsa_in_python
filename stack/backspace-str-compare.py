def apply_backspace(s):
    stack = []

    for char in s:
        if char == "#":
            if stack:
                stack.pop()
        else:
            stack.append(char)
            
    return "".join(stack)

print(apply_backspace("cb#d") == apply_backspace("ac#d"))


# leetcode 844