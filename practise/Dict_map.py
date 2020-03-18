# Enter your code here. Read input from STDIN. Print output to STDOUT
"""import sys
n = int(sys.stdin.readline().strip())
phone_book = dict()
for i in range(n):
    entry = sys.stdin.readline().strip().split(" ")
    phone_book[entry[0]] = entry[1]
query = sys.stdin.readline().strip()
while query:
    phone_number = phone_book.get(query)
    if phone_number:
        print(query + "=" + phone_number)
    else:
        print("Not found")
    query = sys.stdin.readline().strip()"""
#Another way implementing the dict and mapping
'''    n = int(input())
d = {}
for i in range(n):
    x = input().split()
    d[x[0]] = x[1]
while True:
    try:
        name = input()
        if name in d:
            print(name, "=", d[name], sep="")
        else : print("Not found")
    except: break     '''
'''listq = ["r","r","g"]
dictionary = {"r":"ravi","t":"teja","g":"geddada"}
print(list(dictionary.values())[2])'''
d = {"model":"car","ravi":1,"build":"bangloo"}
#for i in d:
 #   print(i)
for x, y in d.items():
    print(x, y)