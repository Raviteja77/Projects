# PF-Exer-26

def factorial(number):
    remainder = 1
    if number == 0:
        remainder = 1
    else:
        while number != 0:
            remainder *= number
            number -= 1
    return remainder
def find_strong_numbers(num_list):
    list1 = []
    for i in range(len(num_list)):
        temp = num_list[i]
        sum1 = 0
        for j in range(len(str(num_list[i]))):
            sum1 += factorial(int(num_list[i])%10)
            num_list[i]/=10
        if sum1==temp:
            list1.append(temp)
    return list1
num_list = [145, 375, 100, 2, 10]
strong_num_list = find_strong_numbers(num_list)
print(strong_num_list)
