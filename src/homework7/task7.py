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
        Let's find the common factor of all set bits.
        Naturally the only common factor is the rightmost bit:
        26 = 1*2^1 * (1*2^3 + 1*2^2 + 0*2^1 + 1*2^0 + 0*2^(-1))
        Thus  1*2^1 = 2 is the largest factor of 26 that is a power of 2.
        So we need rightmost set bit in our number (11010 -> 10).
        Using binary operations:
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
