#Insertion sort
ar = [34, 42, 22, 54, 19, 5]

for i in range(1, len(ar)):
    while ar[i-1] > ar[i] and i > 0:
        ar[i-1], ar[i] = ar[i], ar[i-1]
        i -= 1
print(ar)