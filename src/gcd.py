def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


if __name__ == "__main__":
    assert gcd(6, 4) == 2
    assert gcd(11, 7) == 1
    assert gcd(15, 10) == 5
