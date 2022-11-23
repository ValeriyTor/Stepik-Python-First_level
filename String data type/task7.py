w = int(input())
s = input()
for i in range(len(s)):
    n = ord(s[i]) - w
    if( n < 97 ):
        n = 122 - (96 - n)
    print(chr(n),end="")