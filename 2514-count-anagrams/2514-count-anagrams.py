
class Solution:
    def countAnagrams(self, s):
        MOD = 10**9 + 7
        ans = 1

        for word in s.split():
            fact = 1
            for i in range(2, len(word) + 1):
                fact = fact * i % MOD

            for c in set(word):
                count = word.count(c)
                for i in range(2, count + 1):
                    fact = fact * pow(i, MOD - 2, MOD) % MOD

            ans = ans * fact % MOD

        return ans
