
class Solution:
    def countAnagrams(self, s):
        MOD = 10**9 + 7
        n = len(s)
        fact = [1] * (n + 1)

        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv = [1] * (n + 1)
        inv[n] = pow(fact[n], MOD - 2, MOD)

        for i in range(n, 0, -1):
            inv[i - 1] = inv[i] * i % MOD

        ans = 1

        for word in s.split():
            ans = ans * fact[len(word)] % MOD

            count = [0] * 26
            for c in word:
                count[ord(c) - 97] += 1

            for c in count:
                ans = ans * inv[c] % MOD

        return ans
