'''You will be given two arrays of integers and asked to determine all integers that satisfy
the following two conditions:

The elements of the first array are all factors of the integer being considered
The integer being considered is a factor of all elements of the second array
These numbers are referred to as being between the two arrays. You must determine how many
such numbers exist.
For Example, a=[2,6] and b=[24,36] then 6%2=0,6%6=0 and 24%6,36%6=0 and 12%2,12%6 and 24%12,36%12=0
therefore 2 numbers are possible satisfying the conditions.'''
a = list(map(int,input().split()))
b = list(map(int,input().split()))
nmax = max(a)
nmin = min(b)
count = 0
l = nmin//nmax
for i in range(1,l+1):
    if(sum((i*nmax)%n for n in a)+sum(n%(i*nmax) for n in b)==0):
        count += 1
print(count)
