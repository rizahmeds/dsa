def selection_sort(arr):
    
    for i in range(len(arr)-1):
        min_value = float('inf')
        min_value_index = -1
        for j in range(i+1, len(arr)):
            if arr[j] < min_value:
                min_value = arr[j]
                min_value_index = j
        arr[i], arr[min_value_index] = arr[min_value_index], arr[i]

if __name__ == "__main__":
    arr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
    sorted = selection_sort(arr)
    print(arr)