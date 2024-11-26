array=[64,34,25,12,22,11,90]
n=len(array)
for i in range(n):
    swapped=False
    for i in range(0,n-1):
        if array[i]>array[i+1]:
            array[i],array[i+1]=array[i+1],array[i]
            swapped=True
    if not swapped:
        break
print("Bubble sorted array is:",array)