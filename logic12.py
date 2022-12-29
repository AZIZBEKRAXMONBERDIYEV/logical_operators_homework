def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits of the number are the same".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    s=a//10
    d=a%10
    c=s==d
    return c
print(main(22))