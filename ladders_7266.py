def solution(n, a):
    result = [0] * (n + 1)
    for i in range(1, len(a)):
        if i == 1:
            a[0] = -abs(a[0])
        if abs(a[i]) < a[i - 1]:
            return result
        if -abs(a[i]) >= a[i - 1]:
            a[i] = -abs(a[i])
        else:
            a[i] = abs(a[i])
    result = [1] + a
    return result


n = int(input())
a = list(map(int, input().split()))
print(*solution(n, a))
