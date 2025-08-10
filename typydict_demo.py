from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int   
    
new_person: Person = {'name': 'Abhishek', 'age': '21'}

print(new_person)

# -----------------------------------------------------

# from typing import TypedDict

# class PersonDict(TypedDict):
#     name: str
#     age: int
#     is_student: bool

# # ✅ Correct
# person: PersonDict = {
#     "name": "Alice",
#     "age": 25,
#     "is_student": True
# }

# # ❌ Type checker would complain:
# wrong_person: PersonDict = {
#     "name": "Bob",
#     "age": "twenty",  # age should be int
#     "is_student": True
# }

# print(wrong_person)