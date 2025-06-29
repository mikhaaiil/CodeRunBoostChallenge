import math


def solution(n, m):
    low = 0
    high = int(math.isqrt(n + m))
    best_k = 0
    while low <= high:
        mid = (low + high) // 2
        half = (mid * mid + 1) // 2
        other_half = (mid * mid) // 2
        if (n >= half and m >= other_half) or (m >= half and n >= other_half):
            best_k = mid
            low = mid + 1
        else:
            high = mid - 1
    return best_k

print(solution(11, 15))