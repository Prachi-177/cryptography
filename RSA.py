import math
def gcd(a,h):
    rem=0
    while(1):
        rem= a % b
        if(rem==0):
            return b
        a=b
        b=rem

p=3
q=7
n=p*q
e=2
phi=(p-1)*(q-1)

while(e<phi):
    # e must be co prime to phi and
    # smaller than phi
    if(gcd(e,phi)==1):
        break
    else:
        e=e+1

k=2
d=(1+(k*phi))/e
msg=12.0
c=pow(msg,e)
c=math.fmod(c,n)


        