def create_stack():
    stack = []
    return stack

def is_Empty(stack):
    return len(stack) == 0

def push(stack,item):
    stack.append(item)
    print("Item pushed- " + str(item))

def display(stack):
    for i in range(len(stack)):
        print(stack[i], end=" ")

def pop(stack):
    if(is_Empty(stack)):
        return "Stack underflow"
    return stack.pop()


stack = create_stack()
push(stack,1)
push(stack,2)
display(stack)