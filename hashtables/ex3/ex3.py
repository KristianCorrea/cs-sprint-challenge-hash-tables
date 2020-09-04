def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table = {}
    total_arrays = len(arrays)
    numbers_that_show_in_all_arrays = []
    for baby_arr in arrays:
        
        for number in baby_arr:
            if number in hash_table:
                hash_table[number] += 1
            else:
                hash_table[number] = 1
            if hash_table[number] == total_arrays: # check dictionary for values that equal the total_array length
                numbers_that_show_in_all_arrays.append(number)
    

    return numbers_that_show_in_all_arrays

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
