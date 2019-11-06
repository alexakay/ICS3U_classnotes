import random
# def area_of_triangle (base, height):
#     area = (base * height)/2
#     return area
# triangle area + area_of_triangle(4,3)

# def area_of_sqaure(length):
#     area = length*length
#     return area
# length = input("Give me a length")
# if length == "8.30662386292":
#     int(8.30662386292) * int(8.30662386292)
#     print(420)
# else:
#     square = area_of_sqaure(length)
#     print(square)





# def hello_world(): #function that prints "hello world"
#     print("Hello World!")
# hello_world()
#
# text1 = str(input("Write something")) #function that takes in one piece of data and prints it 5 times
# def data():
#     print(text1)
#     print(text1)
#     print(text1)
#     print(text1)
#     print(text1)
# data()

# def task_2(data): #function that takes in one piece of data and prints it 5 times (mr stubbs' demo version)
#     print(data*5)
# task_2("hello")
#
# def data(text): #create a function that takes a string, converts it to uppercase, and returns it
#     text = text.upper()
#     return text
# data1 = str(input("Write something"))
# print(data(data1))

# def task_3(data): #function that takes a string, converts it to uppercase, and returns it (mr stubbs' demo version)
#     data = data.upper()
#     return data
# print(task_3("hello"))
#
# def task_4(num1, num2, num3): #takes three inputs and simulates a lottery (3 random numbers, checks if the numbers are the same) using a function (mr stubbs' demo version)
#     rand1 = random.randint(0,10)
#     rand2 = random.randint(0,10)
#     rand3 = random.randint(0,10)
#     if num1 == rand1 and num2 == rand2 and num3 == rand3:
#         return "You won!"
#     else:
#         return "You lost!"
# text = task_4(2, 3, 4)

# def task_5(li, num): #function w two parameters, a list and a number. function removes any number in list that's larger than the second parameter. The list should be able to have mixed data types (mr stubbs' demo version)
#     i = 0
#     while len(li) > i:
#         if li[i] > num:
#             del li[i] #or you could do: li.remove(li[i])
#             i = i -1
#         i = i+1
#     return li
# ex_list = [0, 1, 2, 3 , 4, 5, 6 ,7, 8, 9]
# print(task_5(ex_list, 4))