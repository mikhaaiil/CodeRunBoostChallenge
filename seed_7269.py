MOD = 10 ** 9 - 7538


def solution(n):
    memo = {0: 1}

    def dp(x):
        if x in memo:
            return memo[x]
        a_half = dp(x // 2)
        a_third = dp(x // 3)
        a_quarter = dp(x // 4)
        if a_third == 0:
            power = 1
        else:
            power = pow(a_half, a_third, MOD)
        res = (power + 5 * a_quarter + x) % MOD
        memo[x] = res
        return res

    return dp(n)


print(solution(2000000))
