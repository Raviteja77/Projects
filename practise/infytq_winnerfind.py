# PF-Exer-28
# This method accepts the name of winner of each match of the day
def find_winner_of_the_day(*match_tuple):
    # Remove pass and write the logic here
    list1 = []
    for i in match_tuple:
        list1.append(i)
    if list1.count("Team1") > list1.count("Team2"):
        return ("Team1")
    elif list1.count("Team1") < list1.count("Team2"):
        return ("Team2")
    else:
        return ("Tie")
# Invoke the function with each of the print statements given below
print(find_winner_of_the_day(""))
print(find_winner_of_the_day("Team1", "Team2", "Team1", "Team2"))
