def get_msb(a):
    """
    :param a: A positive integer
    :return: Most significant bit of a and the integer part of lg(a)
    """
    if not isinstance(a, int) or a <= 0:
        raise ValueError(f'a should be a positive integer, got {str(a)} as {type(a)}')
    mask, cnt = 1, 0
    while mask <= a:
        mask <<= 1
        cnt += 1
    return mask >> 1, cnt-1


if __name__ == "__main__":
    assert get_msb(1) == (1, 0)
    assert get_msb(2) == (1 << 1, 1)
    assert get_msb(3) == (1 << 1, 1)
    assert get_msb(4) == (1 << 2, 2)
    assert get_msb(7) == (1 << 2, 2)
    assert get_msb(2147483647) == (1 << 30, 30)

    try:
        get_msb(0)
        assert False
    except ValueError as e:
        assert str(e) == "a should be a positive integer, got 0 as <class 'int'>"
        pass

    try:
        get_msb(1.39)
        assert False
    except ValueError as e:
        assert str(e) == "a should be a positive integer, got 1.39 as <class 'float'>"
        pass

