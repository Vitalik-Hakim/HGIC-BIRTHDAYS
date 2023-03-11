arr = [17, 3, 9, 2, 21, 3, 2]


for j in range(0,len(arr)):
    if arr[j] > arr[j+1]:
        arr[j],arr[j+1] = arr[j+1],arr[j]

print(arr)