def solution(n, q, a, queries):
    count = [0] * (n + 2)
    for l, r in queries:
        count[l] += 1
        if r + 1 <= n:
            count[r + 1] -= 1
    for i in range(1, n + 1):
        count[i] += count[i - 1]
    frequencies = count[1:n+1]
    a_sorted = sorted(a, reverse=True)
    frequencies_sorted = sorted(frequencies, reverse=True)
    total = 0
    for ai, freq in zip(a_sorted, frequencies_sorted):
        total += ai * freq
    return total


print(solution(4, 4, [1, 100, 10000, 10101010], [[1, 4], [2, 3], [2, 2], [1, 2]]))