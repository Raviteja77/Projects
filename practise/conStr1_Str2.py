def canAchieve(K,S,T):
    count = 0
    for j in range(len(S)):
        for i in range(K):
            if (ord(S[i]) + (i + 1) > 122):
                if chr(96 + (i + 1)) == T[i]:
                    count += 1
            else:
                if chr(ord(S[i]) + (i + 1)) == T[i]:
                    count += 1

    if count == len(S):
        return True
    return False
s = input()
t = input()
k = int(input())
out_ = canAchieve(k,s,t)
if(out_):
    print("Yes")
else:
    print("No")