# list1 = [1, 4, 7, 3, 4, 5]
# list2 = [3, 5, 6, 3, 2, 6]
# list3 = [list1, list2]
# print(list3)
#
# a = [1, 2, 3]
# b = [99, 98, 97]
# c = [7, 8 , 9]
# newlist = [a, b, c]
# print(newlist)

row1 = [20,7, 11]
row2 = [34, 67, 1]
row3 = [77, 99, 55]
row_sum = input(print("Which row would you like to find the sum of?"))
if row_sum == row1:
    print(sum(row1))
if row_sum == row2:
    print(row2)
if row_sum == row3:
    print(sum(row3))