#write a program for linear search for and binary search
l = [2,5,6,8,3,4,9,7,1,0]
# n=len(l)
item = 8
print("array",l)
# item = int(input("enter element to search in list"))
for i in l:
    if(l[i]==item):
        print("item found at:-",i)
        break
    # else:
    #     print("element not found")
    # print(i)

        # for i in l
# print(id(item))



def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == x:
            return mid   # Element found
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1  # Element not found

# Main program
arr = [2, 4, 6, 8, 10, 12, 14, 16]
print("Array:", arr)

x = int(input("Enter element to search: "))
result = binary_search(arr, x)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")