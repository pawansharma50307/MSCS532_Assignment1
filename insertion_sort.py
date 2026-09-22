
def insertion_sort_descending(arr):
    """
    Sort an array in monotonically descending order
    using the Insertion Sort algorithm.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements less than key to the right
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        # Put key in its rightful place
        arr[j + 1] = key

    return arr


def main():
    my_nums = [41, 15, 42, 18, 23, 24, 5, 16]

    print("Original array:", my_nums)

    sorted_my_nums = insertion_sort_descending(my_nums)

    print("Sorted array (decreasing order):", sorted_my_nums)


if __name__ == "__main__":
    main()