def dailyTemperature(T):
    n = len(T)
    result = [0]*n
    stack = []


    for i,j in enumerate(T):
        # print(i,j)
        while stack and T[n-1] > stack[-1]:
            stack.pop()
            stack.append(j)
        stack.append(j)

    print(stack)


dailyTemperature([73, 74, 75, 71, 69, 72, 76, 73])