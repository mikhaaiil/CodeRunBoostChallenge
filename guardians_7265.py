def solution(n, m, swaps):
    result = [0] * m
    guardians = [True] * n + [False] * n
    current_modules = n
    for i in range(0, len(swaps), 2):
        first, second = guardians[min(swaps[i] - 1, swaps[i + 1] - 1)], guardians[max(swaps[i] - 1, swaps[i + 1] - 1)]
        if first != second and max(swaps[i], swaps[i + 1]) > n >= min(swaps[i], swaps[i + 1]):
            if first:
                current_modules -= 1
            else:
                current_modules += 1
        guardians[swaps[i] - 1], guardians[swaps[i + 1] - 1] = guardians[swaps[i + 1] - 1], guardians[swaps[i] - 1]
        result[i // 2] = current_modules
    return result


n = int(input())
m = int(input())
swaps = list(map(int, input().split()))
print(solution(n, m, swaps))
