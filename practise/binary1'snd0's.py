for i in range(int(input())):
    x,y=list(map(int,input().split()))
    xlist=[1]*x
    ylist=[0]*y
    ans,ans1="",[]
    ans1=xlist[:1]+ylist+xlist[1:]
    c,n=len(ans1),0
    if(len(xlist)!=0):
        for i in ans1:
            ans+=str(i)
            n+=i*pow(2,c-1)
            c-=1
        print(int(ans),n)
    else:
        print(0,0)
