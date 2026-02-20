"""
Purpose:
--------
Check if string can be segmented into dictionary words.

Approach:
---------
Dynamic Programming
Time: O(n^2)
Space: O(n)
"""

def word_break(s, wordDict):

    word_set = set(wordDict)
    n = len(s)

    dp = [False] * (n + 1)
    dp[0] = True  # empty string is valid

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]


# Example
print(word_break("leetcode", ["leet", "code"]))