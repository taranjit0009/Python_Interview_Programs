
def find_min_and_max_value_in_arr_with_loop():
    arr = [44,22,3,11,55,1,299,4,2]
    min_value=arr[0]
    max_value=arr[0]
    for i in range(len(arr)):
        if arr[i]<min_value:
            min_value=arr[i]
    print(min_value)
    for i in range(len(arr)):
        if arr[i]>max_value:
            max_value=arr[i]
    print(max_value)

find_min_and_max_value_in_arr_with_loop()
def find_min_and_max_value_in_arr():
    arr = [44,22,3,11,55,0,299,4,2]
    arr.sort()
    print(arr)
    print(f"The minimum value of the array is = {arr[0]}")
    print(f"The maximum value of the array is = {arr[-1]} ")
find_min_and_max_value_in_arr()