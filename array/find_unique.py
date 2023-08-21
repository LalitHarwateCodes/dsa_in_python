def findUnique(arr):
    dup_elements = {}

    for num in arr:
        if num in dup_elements:
            dup_elements[num] += 1;
        else:
            dup_elements[num] = 1;

    for key,value in dup_elements.items():
        if value == 1:
            return key
   
my_list = [1 ,3, 1, 3, 6, 6, 7, 10, 7]
print(findUnique(my_list))