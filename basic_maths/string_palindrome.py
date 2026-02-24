from re import *
def pal(s):
    s=sub(r'[^a-zA-Z0-9]','',s)
    s=s.lower()
    rev=s[::-1]
    if rev==s:
        return True
    else:
        return False
    
print(pal("A man,a plan,a Canal: Panama"))    