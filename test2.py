s='sreerag'
l=len(s)
for row in s:
    n=''
    for ip in range(l):
        if s[ip]!=l:
            n+=s[ip]
    print(n)
    l-=1
        

