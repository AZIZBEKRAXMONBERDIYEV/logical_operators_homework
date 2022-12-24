def main(a,b):
    """
    Given two integers a, b,  check the following statement "Each of the numbers 'a' and 'b' is negative".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    n=a<0
    s=b<0
    f=n and s
    return f
print(main(-3,-4))
    