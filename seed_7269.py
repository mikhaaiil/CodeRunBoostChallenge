CACHE = {0: 1}


def fast_power(val, p):
    


def solution(n: int) -> int:
    return (fast_power(CACHE[n // 2], CACHE[n // 3]) + 5 * CACHE[n // 4] + n) % (10 ** 9 - 7538)


def _solution(n: int) -> int:
    for i in range(1, n + 1):
        CACHE[i] = solution(i)
    return CACHE[n]


print(fast_power(665498719, 352168713))
print(_solution(10))
