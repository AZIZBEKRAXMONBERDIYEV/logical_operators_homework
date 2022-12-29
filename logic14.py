def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    s=a//10
    c=a%10
    n=(s+c)%2==1
    return n
print(main(23))