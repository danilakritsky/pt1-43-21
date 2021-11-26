"""Бинарные операции.

Вводится число найти его максимальный делитель, являющийся
степенью двойки. 10(2) 16(16), 12(4).
"""


def greatest_divisor(num: int) -> int:
    """Find the greatest divisor of a given number that is a  power of two.

    Example:
    -------
        greatest_divisor(26)
        26 in binary = 11010 = 1*2^4 + 1*2^3 + 0*2^2 + 1*2^1 + 0*2^0
        The only common factor is the rightmost bit:
        26 = 1*2^1 * (1*2^3 + 1*2^2 + 0*2^1 + 1*2^0 + 0*2^(-1))
        Thus  1*2^1 = 2 is the largest factor of 26 that is a power of 2.
        Let:
            xxx - sequence of bits (1 OR 0)
            111 - sequenct of set bits
            000 - sequence of unset bits
        For any number xxx1000 to find its rightmost set bit we need to:
        1) take the previous number: xxx1000 - 1 = xxx0111
        By doing this we unset the rightmost set bit and set all the unset bits right to it
        2) negate this number: ~(xxx0111) = ~x~x~x1000
        We set the original bit back, and unset all the following bits.
        All the preceding bits are reversed now too.
        3) We use bitwise AND on the original number the transformed one:
        xxx1000 & ~x~x~x1000 = 0001000
        All the preceding bits are unset and we are left with the rightmost
        set bit of the original number.
        The result is the largest factor of of the original number that is a power of 2.
        26 & 25 = 11010 & ~11001 = 11010 & 00110 = 10 (that is 2 in decimal).
    """
    if not isinstance(num, int):
        raise TypeError('Expected an integer.')
    if num < 1:
        raise ValueError('Only positive integers are allowed.')

    if num & (num - 1) == 0:
        divisor = num
    else:
        divisor = (num & ~(num - 1))

    print(f'The greatest divisor of {num} that is power of two:\n{divisor}')
    return divisor
