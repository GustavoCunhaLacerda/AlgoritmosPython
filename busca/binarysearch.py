def binary_search(list, el, start=0, end=None):
    if len(list) == 0:
        return None

    start = 0
    end = len(list)-1

    while end >= start:
        pivot = (start+end) // 2 
        if el > list[pivot]:
            start = pivot + 1
        elif el < list[pivot]:
            end = pivot - 1 
        elif el == list[pivot]:
            return pivot

    return None