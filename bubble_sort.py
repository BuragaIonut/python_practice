import time

def bubble(list_a):
    indexing_length = len(list_a) - 1
    sorted = False


    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if list_a[i] > list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]

    return list_a

start = time.time()
print(bubble([123,14,5,5,2345,43634,3,3,3,45,34563]))
end = time.time() - start
print(end)