# fruits = [
#     {"id": 1, "name": "Apple", "quantity": 10, "price": 1.2},
#     {"id": 2, "name": "Banana", "quantity": 25, "price": 0.5},
#     {"id": 3, "name": "Orange", "quantity": 15, "price": 0.8},
#     {"id": 4, "name": "Mango", "quantity": 5, "price": 2.0},
#     {"id": 5, "name": "Grapes", "quantity": 20, "price": 1.5}
# ]
# for i in range (len(fruits)):
#     print(fruits[i]['name'])



fruits = [
    {"id": 1, "name": "Apple", "quantity": 10, "price": 1.2},
    {"id": 2, "name": "Banana", "quantity": 25, "price": 0.5},
    {"id": 3, "name": "Orange", "quantity": 15, "price": 0.8},
    {"id": 4, "name": "Mango", "quantity": 5, "price": 2.0},
    {"id": 5, "name": "Grapes", "quantity": 20, "price": 1.5}
]

for i in range(len(fruits)):
   if fruits[i]['name'] == 'Mango':
      print(fruits[i]['quantity'])