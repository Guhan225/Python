array=[29,10,14,37,13]
n=len(array)
for i in range(n):
    min_index=i
    for j in range(i+1,n):
        if array[j]<array[min_index]:
            min_index=j
    array[i],array[min_index]=array[min_index],array[i]
print("Selection sorted array: ",array)