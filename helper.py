def find_max_index_2d(arr):
    max_value = float('-inf')  # Initialize max_value to negative infinity
    max_i, max_j = -1, -1  # Initialize indices to -1

    # Iterate through the rows
    for i in range(len(arr)):
        # Iterate through the columns
        for j in range(len(arr[i])):
            # Check if the current element is greater than the current max_value
            if arr[i][j] > max_value:
                max_value = arr[i][j]
                max_i, max_j = i, j

    return max_i, max_j


