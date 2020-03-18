word_dict = {"business":"bisiness","word":"word","peace":"pieec","tension":"tanton"}
list1 = [0,0,0]
for key in word_dict:
    ecount = 0
    if len(key)!=len(word_dict[key]):
        list1[2]+=1
    else:
        for i in range(len(key)):
            if word_dict[key][i] in key[i]:
                ecount += 1
        if len(key) == ecount:
            list1[0] += 1
        elif len(key) - ecount <= 2:
            list1[1] += 1
        else:
            list1[2] += 1
print(list1)
'''word_dict = {"business":"bisiness","word":"word","peace":"pieec","tension":"tensio"}
list1=[0,0,0]
for key,value in word_dict.items():
    if key == value:
        list1[0]+=1
    else:
        if len(key)!=len(value):
            list1[2]+=1
            continue
        incorrect=0
        for i in range(min(len(key),len(value))):
            if key[i]!=value[i]:
                incorrect+=1
                if incorrect>2:
                    list1[2]+=1
                    break
        if incorrect<=2:
            list1[1]+=1
print(list1)'''


