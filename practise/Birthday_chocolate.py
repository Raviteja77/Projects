'''Consider the chocolate bar as an array of squares,s=[2,2,1,3,2] . She wants to find segments summing to Ron's
birth day,d=4  with a length equalling his birth month,m=2 . In this case, there are two segments meeting
her criteria:  and [2,2],[1,3].'''
def Birthday(s,d,m):
    ans = 0
    for i in range(len(s)):
        count = 0
        n = 0
        while(n<m):
            count += s[i+n]
            n += 1
        if(count==d):
            ans += 1
        if(i+n==len(s)):
            break
    return ans
s = list(map(int,input().split()))
d = int(input())
m = int(input())
print(Birthday(s,d,m))

