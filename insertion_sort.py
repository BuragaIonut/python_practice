

def insertion_sort(list_a):
    indexing_length = range(1,len(list_a))
    for i in indexing_length:
        value_to_sort = list_a[i]

        while list_a[i-1] > value_to_sort and i > 0:
            list_a[i], list_a[i-1] = list_a[i-1],list_a[i]
            i = i-1

    return list_a


print(insertion_sort([4,124,5235,45745,23,346,2,24534,44545,4564,5,4]))


