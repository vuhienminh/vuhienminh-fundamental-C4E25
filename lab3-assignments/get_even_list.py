def remove_odd(l):
    new_list = []
    for i in l:
        if i % 2 == 0:
            new_list.append(i)
    print(new_list)
    return[new_list]
remove_odd([1,2,3,4,5,6,7])

even_list = remove_odd([1, 2, 5, 9, -10, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
