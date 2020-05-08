def bubble_sort(list):

    list_size = len(list)

    for j in range(list_size-1):
        for i in range(list_size-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
