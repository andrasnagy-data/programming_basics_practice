def merge_sort(array):
    if len(array) > 1:
        # finding mid element of array
        mid = len(array) // 2
        # splitting array into sub-arrays
        l = array[:mid]
        r = array[mid:]
        # recursive merge_sort call
        merge_sort(l)
        merge_sort(r)

        i = j = k = 0
        # copy data to temporary arrays
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                array[k] = l[i]
                i += 1
            else:
                array[k] = r[j]
                j += 1
            k += 1

        # checking for left elements
        while i < len(l):
            array[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            array[k] = r[j]
            j += 1
            k += 1

def print_list(array):
    for i in range(len(array)):
        print(array[i], end= " ")
    print()


if __name__ == "__main__":
    array = [502, 673, 51, 847, 732, 397, 28, 680, 529, 438, 36, 592, 979, 243, 834, 883, 143]
    merge_sort(array)
    print_list(array)