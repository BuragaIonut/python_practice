def selection_sort(list_a):
    indexing_length = range(0,len(list_a)-1)

    for i in indexing_length:
        min_value_index = i

        for j in range(i+1, len(list_a)):
            if list_a[j] < list_a[min_value_index]:
                min_value = j

        
        if min_value_index != i:
            list_a[min_value_index], list_a[i] = list_a[i], list_a[min_value_index]
    
    return list_a

print(selection_sort([1,53,234,123123,53,6456,124]))