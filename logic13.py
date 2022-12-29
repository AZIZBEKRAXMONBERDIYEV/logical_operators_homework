def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is even".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    s=a//10
    d=a%10
    c=(s+d)%2==0
    
    return c
print(main(85))