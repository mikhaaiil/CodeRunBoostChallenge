def solution(n, t, a, b):
    events_F = [0] * (t + 2)
    events_G = [0] * (t + 2)
    total_A = 0
    total_B = 0

    for i in range(n):
        total_A += a[i]
        if b[i] > 0:
            total_B += b[i]
            if a[i] == 0:
                j_i = 0
            else:
                j_i = (a[i] + b[i] - 1) // b[i]
            if j_i <= t:
                events_F[j_i] += a[i]
                events_G[j_i] += b[i]

    res = [0] * (t + 1)
    res[0] = total_A

    F = events_F[0]
    H = events_G[0]
    for j in range(1, t + 1):
        F += events_F[j]
        H += events_G[j]
        G_j = total_B - H
        S_j = j * G_j + F
        res[j] = total_A - S_j

    return res