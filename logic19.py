def main(x):
    """
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    s=x//100
    c=x%100//10
    d=x%10
    a=(d*100)+(c*10)+(s)==x
    return a
print(main(142))