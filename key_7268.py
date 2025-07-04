def solution(n):
    if n < 5:
        return 0
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    if n >= 2:
        is_prime[2] = True
    for i in range(4, n + 1, 2):
        is_prime[i] = False
    i = 3
    while i * i <= n:
        if is_prime[i]:
            start = i * i
            step = 2 * i
            for j in range(start, n + 1, step):
                is_prime[j] = False
        i += 2
    count1, count3 = 0, 0
    for num in range(3, n + 1, 2):
        if is_prime[num]:
            if num % 4 == 1:
                count1 += 1
            else:
                count3 += 1
    return count1 * count3


print(solution(100))
