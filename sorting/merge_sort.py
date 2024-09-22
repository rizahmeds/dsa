#  Merge Sort

def divide_array(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left_sorted = divide_array(left_arr)
    right_sorted = divide_array(right_arr)
    return merge(left_sorted, right_sorted)
    

def merge(left_arr, right_arr):
    result = []
    i = j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_arr[j])
            j += 1

    while i < len(left_arr):
        result.append(left_arr[i])
        i += 1
    while j < len(right_arr):
        result.append(right_arr[j])
        j += 1
    return result
if __name__ == "__main__":
    arr1 = [6,5,4,3,2,1,7]
    print(arr1)
    # divide_array(arr1)
                    #   i
    left_arr = [4,5,6]
                    #    j
    right_arr = [1,2,3,7]
    # result = [1,2,3,4,5,6]
    # result = merge(left_arr, right_arr)
    result = divide_array(arr1)
    print(result)
    