student = {"name": "Alice", "age": 20, "grade": "A", "subjects": ["Math", "Science", "Literature"]}

print(student)
print(student["name"])
print(student["subjects"][1])
print(student.get("age"))
# Using .get() allows us to specify a default value if the key doesn't exist so with hobby it will return None instead of throwing an error
print(student.get("hobby", "No hobby specified"))
#using the no hobby specified as the default value for the get method when the key "hobby" is not found in the student dictionary.

student.update({"hobby": "painting"})
print(student)

del student["grade"]
age = student.pop("age")
print(len(student))
print(age)
print(student.keys())
print(student.values())
print(student.items())