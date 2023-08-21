def remove_middle(stack,size,count=0):
    #base case

    if count == size//2:
        stack.pop()
        return
    
    temp_num = stack.pop()


    remove_middle(stack,size,count+1)

    stack.append(temp_num)


stack = [1,2,3,4,5]
remove_middle(stack,len(stack)) 

print(stack)
   
