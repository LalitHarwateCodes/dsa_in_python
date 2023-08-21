def insert_to_last(stack,num):
    if not stack:
        stack.append(num)
        return
    
    temp_num = stack.pop()

    insert_to_last(stack,num)
    print(stack)
    stack.append(temp_num)


stack = [1,2,3]
insert_to_last(stack,9)

print(stack, end= '')
