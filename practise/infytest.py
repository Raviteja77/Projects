'''class A:
    def __init__(self, bb):
        self.b = bb
class B(A):
    def __init__(self):
        self.a = A(self)
    def __del__(self):
        print("die") #Output:die
def fun():
    b = B()
fun()


def divide(x, y):
    try:
        result = x // y
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
    except:
        print(end='')
    finally:
        print(" finally clause, always raised !! ")
divide(3,"3")
'''






def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i+1:]

        for p in permutation(remLst):
            l.append([m] + p)
    return l
data = list('123')
permutation(data)
#for p in permutation(data):
 #   print (p)





def my_gen():
    n = 1
    print('This is printed first')
    yield n
    n += 1
    print('This is printed second')
    yield n
    n += 1
    print('This is printed at last')
    yield n
for item in my_gen():
    print(item)