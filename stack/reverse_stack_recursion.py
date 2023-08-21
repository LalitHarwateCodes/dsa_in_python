def insert_into_bottom(stack,elem):
    
    if not stack:
        stack.append(elem)
        return
    
    temp_elem = stack.pop()
    # print(temp_elem)
    insert_into_bottom(stack,elem)
    # print("inset",stack)

    stack.append(temp_elem)


def reverse_stack(stack):
    if not stack:
        return
    
    temp_elem = stack.pop()

    reverse_stack(stack)
    print("reverse after")

    insert_into_bottom(stack,temp_elem)
    print("after 3 reverse")


stack = [1,2,3,4]
reverse_stack(stack)
# print(stack)
