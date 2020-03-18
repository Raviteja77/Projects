def gcd(a,b):
    if(a==0):
        return b
    return gcd(b%a,a)
def lcm(a,b):
    return ((a*b)/gcd(a,b))
def lcm1(a,b):
    if(a<b):
        greater = b
    else:
        greater = a
    while True:
        if((greater%a==0) and (greater%b==0)):
            lcm = greater
            break
        greater +=1
    return lcm
print(gcd(45,9))
print(lcm(24,54))
print(lcm1(24,54))
