def min(arr):
    min = arr[0]
    min_ind = 0
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
            min_ind = i
    return min_ind


def select_sort(arr):
    res_arr = []
    for i in range(len(arr)):
        min_ind = min(arr)
        res_arr.append(arr.pop(min_ind))
    return res_arr


arr = [35, 37, 37, 13, 6, 84, 4, 7, 7, 6]
print(arr)
print(select_sort(arr))