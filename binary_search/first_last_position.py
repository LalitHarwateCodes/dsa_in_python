def firstPosition(arr,key):
    begin_index = 0
    end_index = len(arr)-1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index-begin_index)//2
        midpoint_value = arr[midpoint]

        if midpoint_value == key:
            ans = midpoint
            end_index = midpoint - 1

        elif key < midpoint_value:
            end_index = midpoint -1
        
        else:
            begin_index = midpoint + 1
    return f"First occurence is at index position {ans}"



def lastPosition(arr,key):
    begin_index = 0
    end_index = len(arr)-1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index-begin_index)//2
        midpoint_value = arr[midpoint]

        if midpoint_value == key:
            ans = midpoint
            begin_index = midpoint + 1
            

        elif key < midpoint_value:
            end_index = midpoint -1
        
        else:
            begin_index = midpoint + 1
    return f"Last occurrence is at index position {ans}"


arr = [1,2,3,4,4,4,5]

print(firstPosition(arr,4))
print(lastPosition(arr,4))