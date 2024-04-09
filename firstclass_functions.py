def square(x):
    """
    This functions finds the square of an integer

    Args:
        x: an integer

    Return:
        A square value
    """
    return x * x

def my_map(func, arg_list):
    """
    The function does operations on a list using another function
    
    Args:
        func: A function that acts on the list
        arg_list: The list being used as input

    Return:
        A list
    """
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1,2,3,4,5])

print(squares)