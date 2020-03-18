def bubbleSort(a):
    n = len(a)
    for i in range(n):
        for j in range(i, n-1):
            if a[i] > a[j+1] :
                a[i], a[j+1] = a[j+1], a[i]

a = [64, 44, 24, 12, 22, 11, 80]
bubbleSort(a)
print ("Sorted array is:")
for i in range(len(a)):
    print ("%d" %a[i])
#Expected output: 11,12,22,24,44,64,80