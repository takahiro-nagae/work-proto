def is_even(num):
    return num % 2 == 0


def is_prime(num):
    if num <= 1:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for i in range(3, num + 1, 2):
        if num % i == 0:
            return i == num

    return True