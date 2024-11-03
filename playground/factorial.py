import sys

def bad_factorial(number: int) -> int:
    """Return the factorial of `number` using recursion

    :param int number: number to factorialise
    :return int: factorial of the number
    """
    if not isinstance(number, int):
        raise ValueError("number must be integer")
    
    if number < 1:
        raise ValueError("number must be strictly positive")
    
    if number == 1:
        return number
    
    return number * bad_factorial(number - 1)


def binary_factorial(number: int, _left: int = 1) -> int:
    """Smart factorial, divides problem into two

    :param int number: Number to factorialise
    :param int _left: lower bound of multiplication list, defaults to 1
    :return int: 
    """

    if not isinstance(number, int) or not isinstance(_left, int):
        raise ValueError("number and _left must be integers")

    if number < 0 or _left < 1:
        raise ValueError("number and _left must be strictly positive")

    if number == 0:
        return 1

    if number - _left == 1:
        print(f"This is now included: [{number} x {_left}]")
        return number * _left
    
    if number == _left:
        print(f"This is now included: [{number}]")
        return number
    
    midpoint = (number + _left) // 2
    print(f"Range being multiplied is:\n - Range: {list(range(_left, number+1))}")
    print(f"Midpoint is: {midpoint}")

    return binary_factorial(number=number, _left=midpoint+1) * binary_factorial(number=midpoint, _left=_left)


if __name__ == "__main__":

    number = sys.argv[1]
    try:
        number = int(number)
    except Exception:
        exit(1)
    
    print(binary_factorial(number))