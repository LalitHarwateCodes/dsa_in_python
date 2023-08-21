def intersectionArray(arr1,arr2):
    intersection_array = set()
    for num in arr2:
        if num in arr1:
            intersection_array.add(num)
    return list(intersection_array)

arr1 =[1,2,2,1]
arr2 = [2,2]

print(intersectionArray(arr1,arr2))