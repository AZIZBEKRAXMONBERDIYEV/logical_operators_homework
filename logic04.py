def main(a,b):
    """
    Given two integers a, b,  check the following statement "Each of the numbers 'a' and 'b' is even".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """

    n=a%2==0
    s=b%2==0 
    c=n and s
    return c
print(main(3,8))