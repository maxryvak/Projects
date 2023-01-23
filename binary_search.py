
N = int(input("Input number: "))
mas = [3, 5, 74, 47, 8, 3, 7, 85]


def binary_search(mas_sort, item):
    low = 0
    high = len(mas_sort) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = mas_sort[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid-1
        else:
            low = mid+1
    return None


print(sorted(mas))

print(binary_search(sorted(mas), N))