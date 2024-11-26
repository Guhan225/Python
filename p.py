def pigeonhole_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    size = max_val - min_val + 1
    pigeonholes = [[] for _ in range(size)]
    for value in arr:
        pigeonholes[value - min_val].append(value)
    sorted_arr = []
    for hole in pigeonholes:
        sorted_arr.extend(hole)
    return sorted_arr
if __name__ == "__main__":
    arr = [8, 3, 2, 7, 4, 6, 5]
    print("Original array:", arr)
    sorted_arr = pigeonhole_sort(arr)
    print("Sorted array:", sorted_arr)
