def binarySearch(data, key):
    start = 0
    end = len(data)-1

    while start <= end:
        middle = (start + end) // 2

        if key == data[middle]:
            return middle
        elif key > data[middle]:
            start = middle +1
        else:
            end = middle -1

    return -1











key = 19
data = [2, 4, 7, 9, 11, 19, 23]
print(binarySearch(data, key))