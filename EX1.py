def linearSearch(array,n,x):
    for i in range(0,n):
        if (array[i] == x):
            return i
    return -1

array = [7,10,12,14,16,20,29,37]
n = len(array)
result = linearSearch(array,n,14)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ",result)
result = linearSearch(array,n,29)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ",result)