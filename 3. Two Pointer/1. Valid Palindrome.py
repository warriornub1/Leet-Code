def isPalindrome(s) -> bool:
    l,  r = 0, len(s) - 1
    while l < r:
        
        if not s[l].isalnum():
            l += 1
            
        if not s[r].isalnum():
            r -= 1
        
        else:
            if(s[l].lower() != s[r].lower()):
                return False
            l += 1
            r -= 1
    return True


print( isPalindrome("A man, a plan, a canal: Panama") )
        
        