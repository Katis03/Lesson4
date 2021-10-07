def Palindrome(a):
    if len(a)>1:
        if a[0]==a[-1]:
            Palindrome(a[1:-1])
        else:
            return 0
    if len(a)<1:
        return true
a = 'шалаш'
print(Palindrome(a))

