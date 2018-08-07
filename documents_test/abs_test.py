def abs_1(n):
    '''
    Function to get absolute value of number.

    Example:

    >>> abs_1(1)
    1
    >>> abs_1(-1)
    1
    >>> abs_1(0)
    0
    '''
    return n if n>= 0 else (-n)

if __name__ == '__main__':
    import doctest
    doctest.testmod()