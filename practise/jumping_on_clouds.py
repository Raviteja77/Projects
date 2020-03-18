def jumpingOnClouds(c):
    jumps,i = 0,0
    while i < len(c) - 1:
        if i+2 < len(c) and c[i+2] == c[i]:
            i += 1
        jumps += 1
        i +=1
    return jumps
n = int(input())
c = list(map(int,input().split()))[:n]
print(jumpingOnClouds(c))
