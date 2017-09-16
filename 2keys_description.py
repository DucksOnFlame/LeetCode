class Solution:

    def minSteps(self, n):
        max_divider = n // 2
        for i in range(max_divider, 2, -1):
            if Solution.is_prime(i) and n % i == 0:
                print("n = " + str(n))
                print("i = " + str(i))
                steps_to_prime = i - 1
                steps_to_n_from_prime = (n / i) - 1

                shortcut = n / i
                if Solution.is_power2(shortcut):
                    steps = 0
                    a = 2
                    while True:
                        steps += 1
                        if shortcut == a:
                            break
                        else:
                            a *= 2

                    steps_to_n_from_prime = steps
                    print("Shortcut steps: " + str(steps))
                elif shortcut % 2 == 0:
                    print()

                return steps_to_prime + steps_to_n_from_prime

        return n - 1

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        if n % 2 == 0:
            return n == 2  # return False
        k = 3
        while k * k <= n:
            if n % k == 0:
                return False
            k += 2
        return True

    @staticmethod
    def is_power2(num):
        num = int(num)
        return num != 0 and ((num & (num - 1)) == 0)

solution = Solution()
print("Min steps: " + str(int(solution.minSteps(50))))
