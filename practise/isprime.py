import math
for i in range(int(input())):
    number = int(input())
    if (number != 2 and number % 2 == 0 or number == 1):
        print("Not prime")
    elif number == 2:
        print("Prime")
    else:
        c = 0
        for j in range(3, int(math.sqrt(number)) + 1, 2):
            if number % j == 0:
                print("Not prime")
                c += 1
                break
        if c == 0:
            print("Prime")