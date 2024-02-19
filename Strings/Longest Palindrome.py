def longestPalindrome(s):
    
    longestStr = ""
    for i in range(len(s)):
        
        L, R = i, i
        while L >= 0 and R < len(s) and s[L] == s[R]:
            if R - L + 1 > len(longestStr):
                longestStr = s[L: R + 1]               
            L -= 1
            R += 1
             
        L, R = i, i + 1
        while L >= 0 and R < len(s) and s[L] == s[R]:
            if R - L + 1 > len(longestStr):
                longestStr = s[L: R + 1]               
            L -= 1
            R += 1
        
    print(longestStr)
    return longestStr

longestPalindrome("babad")