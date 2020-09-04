def has_negatives(array):
    """
    YOUR CODE HERE
    """
    # Without Dictionary

    # positive = []
    # output = []
    
    # for number in array:
    #     if (number >= 0):
    #         positive.append(number)
            
    # for number in array:
    #     if (number < 0) and (-number in positive):
    #         output.append(-number)
    
    # return output

    # With Dictionary

    dict = {}
    result = []

    for number in array:
        # absolute value number
        if number not in dict:
            dict[number] = 1
    
    for number in array:
        if -number in dict:
            if number > 0:
                result.append(number)

    return result




if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4,]))
