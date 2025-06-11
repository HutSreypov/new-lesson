# num=0
# while num!= 7:
#     num=int(input('Enter your number here:'))
#     if num == 7:
#      print(' good bay')



# isFoundSeven = True
# while isFoundSeven:
#     num = int(input("Enter number: "))
#     if num == 7:
#         print("Good bye!")
#         isFoundSeven = False







# num=0
# index=1
# while num !=9 and index != 4:
#     num= int(input('Enter your number me:'))
#     if num !=9 and num != 3:
#         print('Sorry you already try 3 times, please try again later')
#     else:
#         print('Great! you can do it!')
#     index +=1 



# index = 0
# isFoundNine = False
# while index < 3:
#     num = int(input("Enter number: "))
#     if num == 9:
#         print("Great! You do it!")
#         isFoundNine = True
#         break
#     index += 1

# if not isFoundNine:
#     print("Sorry you already try 3 times, please try again later")



# students = [
#     {
#         "name": "Alice",
#         "age": 17,
#         "gender": "Female",
#         "address": {
#             "city": "Phnom Penh",
#             "district": "Chamkarmon"
#         },
#         "subjects": [
#             {"name": "Math", "score": 85},
#             {"name": "Physics", "score": 78},
#             {"name": "Biology", "score": 90}
#         ]
#     },
#     {
#         "name": "Sokha",
#         "age": 16,
#         "gender": "Male",
#         "address": {
#             "city": "Siem Reap",
#             "district": "Svay Dangkum"
#         },
#         "subjects": [
#             {"name": "English", "score": 75},
#             {"name": "Computer", "score": 88},
#             {"name": "Art", "score": 92}
#         ]
#     },
#     {
#         "name": "Dara",
#         "age": 18,
#         "gender": "Male",
#         "address": {
#             "city": "Battambang",
#             "district": "Battambang"
#         },
#         "subjects": [
#             {"name": "History", "score": 60},
#             {"name": "Geography", "score": 70},
#             {"name": "Math", "score": 80}
#         ]
#     }
# ]
# countMale=0
# for student in students:
#     if student['gender'] == 'Male':
#         countMale+= 1
# print(countMale)





students = [
    {
        "name": "Alice",
        "age": 17,
        "gender": "Female",
        "address": {
            "city": "Phnom Penh",
            "district": "Chamkarmon"
        },
        "subjects": [
            {"name": "Math", "score": 85},
            {"name": "Physics", "score": 78},
            {"name": "Biology", "score": 90}
        ]
    },
    {
        "name": "Sokha",
        "age": 16,
        "gender": "Male",
        "address": {
            "city": "Siem Reap",
            "district": "Svay Dangkum"
        },
        "subjects": [
            {"name": "English", "score": 75},
            {"name": "Computer", "score": 88},
            {"name": "Art", "score": 92}
        ]
    },
    {
        "name": "Dara",
        "age": 18,
        "gender": "Male",
        "address": {
            "city": "Battambang",
            "district": "Battambang"
        },
        "subjects": [
            {"name": "History", "score": 60},
            {"name": "Geography", "score": 70},
            {"name": "Math", "score": 80}
        ]
    }
]
