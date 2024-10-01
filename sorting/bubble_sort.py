def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == "__main__":
    arr = [64, 34, 25, 5, 22, 11, 90, 12]
    sorted = bubble_sort(arr)
    print(arr)