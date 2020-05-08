def quick_sort(list, start=0, end=None):
    if end is None:
        end = len(list)-1
    
    if start < end:
        pivot = partition(list, start, end)
        quick_sort(list, start, pivot-1)
        quick_sort(list, pivot+1, end)

def partition(list, start, end):
    pivot = list[end]
    smaller = start
    for bigger in range(start, end):
        if list[bigger] <= pivot:
            list[bigger], list[smaller] = list[smaller], list[bigger]
            smaller += 1

    list[end], list[smaller] = list[smaller], list[end]
    return smaller

