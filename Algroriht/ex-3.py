# students = [
#     {"id": 1, "name": "Alice", "age": 18, "class": "A", "score": 85},
#     {"id": 2, "name": "Bob", "age": 17, "class": "B", "score": 90},
#     {"id": 3, "name": "Charlie", "age": 18, "class": "C", "score": 49},
#     {"id": 4, "name": "Dara", "age": 19, "class": "A", "score": 92},
#     {"id": 5, "name": "Eve", "age": 17, "class": "C", "score": 88}
# ]
# for i in range(len(students)):
#     print(students[i]['name'])



# students = [
#     {"id": 1, "name": "Alice", "age": 18, "class": "A", "score": 85},
#     {"id": 2, "name": "Bob", "age": 17, "class": "B", "score": 90},
#     {"id": 3, "name": "Charlie", "age": 18, "class": "C", "score": 49},
#     {"id": 4, "name": "Dara", "age": 19, "class": "A", "score": 92},
#     {"id": 5, "name": "Eve", "age": 17, "class": "C", "score": 88}
# ]

# total_age=0
# for students in students:
#     total_age+=(students['age'])
# print(total_age/len(students))



# students = [
#     {"id": 1, "name": "Alice", "age": 18, "class": "A", "score": 85},
#     {"id": 2, "name": "Bob", "age": 17, "class": "B", "score": 90},
#     {"id": 3, "name": "Charlie", "age": 18, "class": "C", "score": 49},
#     {"id": 4, "name": "Dara", "age": 19, "class": "A", "score": 92},
#     {"id": 5, "name": "Eve", "age": 17, "class": "C", "score": 88}
# ]
# maxScore=students[0]['score']
# topstudent=''
# for student in students:
#     if student['score']>maxScore:
#         maxScore=student['score']
#         topStudent=student['name']
# print(topStudent)




# students = [
#     {"id": 1, "name": "Alice", "age": 18, "class": "A", "score": 85},
#     {"id": 2, "name": "Bob", "age": 17, "class": "B", "score": 90},
#     {"id": 3, "name": "Charlie", "age": 18, "class": "C", "score": 49},
#     {"id": 4, "name": "Dara", "age": 19, "class": "A", "score": 92},
#     {"id": 5, "name": "Eve", "age": 17, "class": "C", "score": 88}
# ]
# maxScore=students[0]['score']
# topstudent=''
# for student in students:
#     if student['score']< maxScore:
#         maxScore=student['score']
#         topStudent=student['name']
# print(topStudent)




# students = [
#     {"id": 1, "name": "Alice", "age": 18, "class": "A", "score": 85},
#     {"id": 2, "name": "Bob", "age": 17, "class": "B", "score": 90},
#     {"id": 3, "name": "Charlie", "age": 18, "class": "C", "score": 49},
#     {"id": 4, "name": "Dara", "age": 19, "class": "A", "score": 92},
#     {"id": 5, "name": "Eve", "age": 17, "class": "C", "score": 88}
# ]

# total_age=0
# for students in students:
#     total_age+=(students['score'])
# print(total_age/len(students))



# students = [
#     {"id": 1, "name": "Alice", "age": 18, "class": "A", "score": 85},
#     {"id": 2, "name": "Bob", "age": 17, "class": "B", "score": 90},
#     {"id": 3, "name": "Charlie", "age": 18, "class": "C", "score": 49},
#     {"id": 4, "name": "Dara", "age": 19, "class": "A", "score": 92},
#     {"id": 5, "name": "Eve", "age": 17, "class": "C", "score": 88}
# ]

# counter = 0
# for student in students:
#    if (student['class'] == "C"):
#       counter += 1
# print(counter)



# def sumArray(array):
#     sum=0
#     for num in array:
#         sum += num
#     return sum
# arr1 = [2, 4, 5, 6, 7, 9]
# arr2 = [3, 5, 6]
# arr3 = [4, 8, 9, 2, 1]
# print(sumArray(arr1))
# print(sumArray(arr2))
# print(sumArray(arr3))



# def sumArray(array):
#     sum=0
#     for num in array:
#         sum += num
#     return sum
# def averageArray(array):
#     return sumArray(array) / len(array)
# arr1 = [2, 4, 5, 6, 7, 9]
# arr2 = [3, 5, 6]
# arr3 = [4, 8, 9, 2, 1]
# print(averageArray(arr1))
# print(averageArray(arr2))
# print(averageArray(arr3))


# def countOddNumber(array):
#     counter = 0
#     for i in array:
#         if i % 2 != 0:
#             counter+=1
#     return counter
# arr1 = [2, 4, 5, 6, 7, 9]
# arr2 = [3, 5, 6]
# arr3 = [4, 8, 9, 2, 1]
# print(countOddNumber(arr1))
# print(countOddNumber(arr2))
# print(countOddNumber(arr3))




# def findMax(array):
#     max = array[0]
#     for n in array:
#         if n > max:
#             max= n
#     return max


# arr1 = [2, 4, 5, 6, 7, 9]
# arr2 = [3, 5, 6]
# arr3 = [4, 8, 9, 2, 1]
# print(findMax(arr1))
# print(findMax(arr2))
# print(findMax(arr3))




# def replaeValue(array, value):
#     for i in range (len(array)):
#         if array [i] % 2== 0:
#             array[i] = value 
#     return array

# arr1 = [2, 4, 5, 6, 7, 9]
# arr2 = [3, 5, 6]
# arr3 = [4, 8, 9, 2, 1]
# print(replaeValue(arr1,100))
# print(replaeValue(arr2,100))
# print(replaeValue(arr3,100))




# def findMin(array):
#     min= array[0]
#     for n in array:
#          if n < min:
#              max= n
#          return min


# arr1 = [5, 6, 56, 6, 7, 9]
# arr2 = [3, 5, 7, 9, 8]
# arr3 = [4, 8, 3, 2, 1, 7, 3, 9]
# print(findMin(arr1))
# print(findMin(arr2))
# print(findMin(arr3))



# def sumEvenNumber(array):
#     sum =0
#     for value in array:
#         if value % 2==0:
#             sum += value
#     return sum
# arr1 = [5, 6, 56, 6, 7, 9]
# arr2 = [3, 5, 7, 9, 8]
# arr3 = [4, 8, 3, 2, 1, 7, 3, 9]
# print(sumEvenNumber(arr1))
# print(sumEvenNumber(arr2))
# print(sumEvenNumber(arr3))



# def reverseArray(array):
#     lenght = len(array)-1
#     newArray=[]
#     for i in range(len(array)):
#         newArray.append(array[lenght-i])
#     return newArray
# arr1 = [5, 6, 56, 6, 7, 9]
# arr2 = [3, 5, 7, 9, 8]
# arr3 = [4, 8, 3, 2, 1, 7, 3, 9]
# print(reverseArray(arr1))
# print(reverseArray(arr2))
# print(reverseArray(arr3))

    
        
# arr1 = [5, 6, 56, 6, 7, 9]
# arr2 = [3, 5, 7, 9, 8]
# arr3 = [4, 8, 3, 2, 1, 7, 3, 9]
# arr1.append(100)
# arr2.append(100)
# arr3.append(100)
# print(arr1)
# print(arr2)
# print(arr3)



# def indexNumSeven(list):
#     myNewList = []
#     for i in range(len(list)):
#         if array[i] == 7:
#             myNewList.append(i)
#     return myNewList

# array = [1,2,5,6,7,0,2,7,8,9]
# result = indexNumSeven(list)
# print(result)


# myArray = [1,2,5,6,7,0,2,7,8,9]
# isFound = False
# index = 0
# while not isFound:
#     print(index)
#     if myArray[index] == 7:
#         print(index)
#         isFound = True
#     index+=1
#     print(index)



# def indexText(string):
#     myNewText = []
#     for i in range(len(text)):
#         if text[i] == 'n':
#             myNewText.append(i)
#     return myNewText

# text= 'banana'
# result = indexText(list)
# print(result)















