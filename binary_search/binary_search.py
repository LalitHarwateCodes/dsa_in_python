def binarySearch(arr,key): 
    begin_index = 0
    end_index = len(arr)-1

    while(begin_index <= end_index):
        midpoint  = begin_index + (end_index-begin_index)//2
        midpoint_value = arr[midpoint]

        if midpoint_value == key:
            return f"Found at index position {midpoint}"
        elif key < midpoint_value:
            end_index = midpoint-1
        else:
            begin_index = midpoint+1
    return None



print(binarySearch([1,2,3,4,5,6],6))