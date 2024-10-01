def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == "__main__":
    arr = [64, 34, 25, 5, 22, 11, 90, 12]
    sorted = insertion_sort(arr)
    print(arr)