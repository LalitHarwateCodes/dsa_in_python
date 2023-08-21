def find_duplicate(arr):
    element_count = {}
    duplicate_count = []

    for num in arr:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1

    for key,value in element_count.items():
        if value > 1:
            duplicate_count.append(key)
    
    return duplicate_count

my_list = [3 ,1 ,3 ,4 ,2]
my_list_second = [1,1,1]
print(find_duplicate(my_list))
print(find_duplicate(my_list_second))