def findUnique(arr):
    element_count = {}

    for num in arr:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1

        
    if(len(set(element_count.values()))) == len(set(arr)):
        return True
    else:
        return False
    
my_list =[-3,0,1,-3,1,1,1,-3,10,0]
my_list_2 = [1,2]

print(findUnique(my_list))
print(findUnique(my_list_2))