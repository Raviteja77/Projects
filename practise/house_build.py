t = int(input())
for j in range(t):
    N = int(input())
    M = int(input())
    r = int(input())
    c = int(input())
    s = int(input())
    x = list(map(int, input().split()))[:r]
    y = list(map(int, input().split()))[:c]
    z, index = 0, 0
    if c == 0:
        z += abs(M * (N - r))
    else:
        l = []
        for i in range(len(y)):
            if y[i] > 1:
                z += abs((((len(l[index:y[i]]) - 1) // s) * (N - r)) // s)
                index += y[i]
            elif y[i] == 1 and len(y) == 1:
                z += abs(((len(l[y + 1:M]) // s) * (N - r)) // s)
            elif y[i] == 1 and i < len(y) - 1:
                z += abs(((len(l[index + 1:y[i + 1]]) // s) * (N - r)) // s)
                index += y[i + 1] - 1
print(z)
