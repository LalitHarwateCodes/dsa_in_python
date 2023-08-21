def reverseString(s):  # --> appraoch 1
    stack = []

    for char in s[::-1]:
        stack.append(char)

    return ''.join(stack)

print(reverseString("hello"))




def reverseStringwithPop(s):
    stack = []

    for char in s:
        stack.append(char)

    reversed_string = ""

    while stack:
        reversed_string += stack.pop()

    return reversed_string

print(reverseStringwithPop("Hello"))