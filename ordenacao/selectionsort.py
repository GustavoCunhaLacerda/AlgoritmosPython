def selection_sort(list):
    
    list_size = len(list)

    for j in range(list_size - 1):
        min_index = j
        for i in range(j, list_size):
            if list[i] < list[min_index]:
                min_index = i
        
        if list[j] > list[min_index]:
            list[j], list[min_index] = list[min_index], list[j]
