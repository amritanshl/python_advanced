#Linear serach
def linear_search(arr,target):
    for i in range (len(arr)):
        if arr[i]==target:
            return print(i)
    return -1
# arr =  [10,20,23,40,70,80]
# target="Anjali"
#linear_search(arr,target)


def binary_search(arr, target):
    left, right = 0, len(arr) -1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid -1
arr = [5, 15, 25, 35, 45, 55,65,88,99]


def binary_search_recursive(arr, left, right, target):
    if left>right:
        return -1
    mid = (left + right)//2
    if arr[mid] == target:
        return print(arr[mid])
    elif arr[mid] < target:
        return binary_search_recursive(arr,mid+1, right, target)
    else:
        return binary_search_recursive(arr,left, mid-1, target)
#binary_search_recursive(arr,0,len(arr)-1, 15)
import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

# arr = [10, 20, 30, 40, 50, 55, 60, 70, 80, 90]
# target = 55
# result = jump_search(arr, target)
# print("Index:", result)
def interpolation_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high and target >= arr[low] and target <= arr[high]:
        pos = low + ((target-arr[low])*(high-low)//(arr[high]-arr[low]))
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos+1
        else:
            high = pos-1
    return -1

arr = [10, 20, 30, 40, 50, 60, 70, 80]
target = 60
result = interpolation_search(arr, target)
