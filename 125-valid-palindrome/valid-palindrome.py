class Solution:
    def isPalindrome(self, s):
        a=""
        for i in s:
            if i.isalnum():
                a=a+i.lower()
        return a==a[::-1]      