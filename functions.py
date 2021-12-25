def is_palindrome(word: str) -> bool:
    return word == word[::-1]
    

def is_prime(number: int) -> bool:
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    return all(number % i != 0 for i in range(3, int(number ** 0.5) + 1, 2))

def is_in_range(number: float, lower: float, upper: float) -> bool:
    return lower <= number <= upper

def factorial(number: int) -> int:
    if number == 0:
        return 1
    return number * factorial(number - 1)

def reverse_string(string: str) -> str:
    return string[::-1]

def sum_of_list(list_: list) -> int:
    s = 0
    for i in list_:
        s += i
    return s


def max3(x, y, z):
    return max(x, max(y, z))