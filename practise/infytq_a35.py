#PF-Assgn-35
#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)
def find_more_than_average():
    #Remove pass and write your logic here
    global list_of_marks
    remainder = sum(list_of_marks)/10
    count = 0
    for i in list_of_marks:
        if i > remainder:
            count += 1
    return count*10
def sort_marks():
    #Remove pass and write your logic here
    global list_of_marks
    list1 = []
    for i in list_of_marks:
        list1.append(i)
    list1.sort()
    return list1
def generate_frequency():
    #Remove pass and write your logic here
    global list_of_marks
    list1 = []
    for i in range(26):
        list1.append(list_of_marks.count(i))
    return list1
print(find_more_than_average())
print(generate_frequency())
print(sort_marks())