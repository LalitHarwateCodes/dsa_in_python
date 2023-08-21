def swapAlternate(lst):
    for i in range(0,len(lst)-1,2):
        temp = lst[i]
        lst[i] = lst[i+1]
        lst[i+1] = temp

my_list = [1,23,4,5,4]

swapAlternate(my_list)

print(my_list)