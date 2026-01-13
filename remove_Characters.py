def removeCharacter(s1,ch):
    if len(s1) == 0 or s1 == '':
        return s1
        
    small_Answer = removeCharacter(s1[1:],ch)
    
    if s1[0] == ch:
        return small_Answer
        
    else:
        return s1[0]+small_Answer

word = "Hello worldzz"
print(removeCharacter(word,'z'))
