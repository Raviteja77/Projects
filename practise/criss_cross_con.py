def criss_cross(list1,list2):
    list2=list2[::-1]
    string=''
    for i in range(len(list1)):
        if list1[i]=='None':
            list1[i]=''
        if list2[i]=='None':
            list2[i]=''
        string+=list1[i]+list2[i]+' '
    return string

list1=list(input().split())
list2=list(input().split())
print(criss_cross(list1,list2))