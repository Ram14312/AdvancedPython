def check_Plaindrome_Helper(s1,start,end):
    if (start>=end):
        return True
        
    if (s1[start] != s1[end]):
        return False
        
    return check_Plaindrome_Helper(s1,start+1,end-1)


def check_Palindrome(s1):
    return check_Plaindrome_Helper(s1,0,len(s1)-1)
    
    
word = 'abcda' 
print(check_Palindrome(word))
