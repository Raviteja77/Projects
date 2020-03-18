number = int(input())
i=0
list1=[]
list2=[]
while(number!=0):
    i=number%2
    number=number//2
    list1.append(i)
print(list1.count(1))
for i in range(len(list1)):
    if list1[i]==1:
        list2.append(i)
print(list2)