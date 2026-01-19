def randomSearch(items: list, target) -> int:
    import random

    attempts = 0

    while True:
        attempts += 1
        random_index = random.randint(0, len(items) - 1)

        if items[random_index] == target:
            print(f"Target was found after {attempts} tries")
            return random_index

def linearSearch(items: list, target):
    index = 0
    checks = 0

    while index < len(items):
        checks += 1

        if items[index] == target:
            return index, checks

        index += 1

    return -1, checks


def binarySearch(items: list, target):
    left = 0
    right = len(items) - 1
    checks = 0

    while left <= right:
        checks += 1
        middle = (left + right) // 2

        if items[middle] == target:
            return middle, checks
        elif items[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1, checks
