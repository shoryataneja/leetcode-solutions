class Solution(object):
    def totalWaviness(self, num1, num2):

        def solve(x):
            if x < 0:
                return 0

            digits = list(map(int, str(x)))
            n = len(digits)

            memo = {}

            def dp(pos, tight, started, prev1, prev2):

                key = (pos, tight, started, prev1, prev2)

                if not tight and key in memo:
                    return memo[key]

                if pos == n:
                    return (1, 0)

                limit = digits[pos] if tight else 9

                total_count = 0
                total_wave = 0

                for d in range(limit + 1):

                    ntight = tight and (d == limit)

                    if not started and d == 0:

                        cnt, wave = dp(
                            pos + 1,
                            ntight,
                            False,
                            -1,
                            -1
                        )

                    elif not started:

                        cnt, wave = dp(
                            pos + 1,
                            ntight,
                            True,
                            d,
                            -1
                        )

                    else:

                        add = 0

                        if prev2 != -1:
                            if (
                                (prev1 > prev2 and prev1 > d)
                                or
                                (prev1 < prev2 and prev1 < d)
                            ):
                                add = 1

                        cnt, wave = dp(
                            pos + 1,
                            ntight,
                            True,
                            d,
                            prev1
                        )

                        wave += add * cnt

                    total_count += cnt
                    total_wave += wave

                ans = (total_count, total_wave)

                if not tight:
                    memo[key] = ans

                return ans

            return dp(0, True, False, -1, -1)[1]

        return solve(num2) - solve(num1 - 1)