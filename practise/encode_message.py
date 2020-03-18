def encode(s):
    count=1
    string=''
    index=0
    while index<=len(s)-1:
        if index==len(s)-1 or s[index]!=s[index+1]:
            string += str(count) + s[index]
            count=1
        else:
            count+=1
        index+=1
    return string

encoded_message=encode('AABBBBCCCCCCCAB')
print(encoded_message)

