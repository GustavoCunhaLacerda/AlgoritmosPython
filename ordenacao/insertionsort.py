def insertion_sort(list):

    list_size = len(list)

    for i in range(1, list_size):
        key = list[i]
        j = i - 1
        while j >= 0 and list[j] > key:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key