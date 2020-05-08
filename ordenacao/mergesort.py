def merge_sort(list, start=0, end=None):
    if end is None:
        end = len(list)
    if (end - start > 1):
        mid = (start + end) // 2
        merge_sort(list, start, mid)
        merge_sort(list, mid, end)
        merge(list, start, mid, end)

def merge(list, start, mid, end):
    left = list[start:mid]
    right = list[mid:end]

    left_top_index = 0
    right_top_index = 0
    for k in range(start, end):

        if left_top_index >= len(left):
            list[k] = right[right_top_index]
            right_top_index += 1
        elif right_top_index >= len(right):
            list[k] = left[left_top_index]
            left_top_index += 1

        elif left[left_top_index] < right[right_top_index]:
            list[k] = left[left_top_index]
            left_top_index += 1
        else:
            list[k] = right[right_top_index]
            right_top_index += 1