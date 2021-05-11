def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    
    items_greater = []
    items_lower = []


    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


print(quick_sort([12,1223453,46,457,567,2,3535,645,74,57,857,2]))