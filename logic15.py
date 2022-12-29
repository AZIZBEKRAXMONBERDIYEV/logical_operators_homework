def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    s=a//100
    d=a%100//10
    c=a%10
    n=(s+d+c)%2==1
    return n
print(main(233))