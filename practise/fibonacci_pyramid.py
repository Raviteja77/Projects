for i in range(int(input())):
    f1 = 0
    f2 = 1
    result = 0
    for j in range(i + 1):
        f1,f2 = f2,result
        print(result,end='')
        result = f1 + f2
    print()


"""
f1 = 0
f2 = 1
result = 0
n = int(input())
print(f1,f2,end = " ")
for i in range(2,n):
    result = f1 + f2
    f1,f2 = f2,result
    print(result,end=" ")

"""