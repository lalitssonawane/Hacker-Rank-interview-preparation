#Lena is preparing for an important coding competition that is preceded by a number of sequential preliminary contests. Initially, her luck balance is 0. She believes in "saving luck", and wants to check her theory. Each contest is described by two integers,  and :

# is the amount of luck associated with a contest. If Lena wins the contest, her luck balance will decrease by ; if she loses it, her luck balance will increase by .
 #denotes the contest's importance rating. It's equal to  if the contest is important, and it's equal to  if it's unimportant.

def luckBalance(k, contests):
    important, optional = [], 0
    for x,y in contests:
        if y: 
            important.append(x)
        else: 
            optional+=x
    if k<len(important):
        s = sorted(important)
        i = len(s)-k
        return optional+sum(s[i:])-sum(s[:i])
    return optional+sum(important)

n,k = map(int,input().split())
contests = [list(map(int,input().split())) for _ in range(n)]
print(luckBalance(k, contests))