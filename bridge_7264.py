def solution(n, a):
    pos = sorted(a)
    max_segment = 0
    left = 0
    for right in range(n):
        while pos[right] - pos[left] > n - 1:
            left += 1
        max_segment = max(max_segment, right - left + 1)
    return n - max_segment


n = int(input())
positions = list(map(int, input().split()))
print(solution(n, positions))
