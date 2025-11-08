import json
students = [
    {
        "name": "Bob",
        "age": 15,
        "grade": 9,
        "subjects": ["Math", "Informatics", "Physics"],
        "average_score": 11.2
    },
    {
        "name": "Emma",
        "age": 14,
        "grade": 8,
        "subjects": ["Ukrainian", "English", "History"],
        "average_score": 10.5
    },
    {
        "name": "Jack",
        "age": 16,
        "grade": 10,
        "subjects": ["Biology", "Chemistry", "Geography"],
        "average_score": 9.8
    }
]

with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, ensure_ascii=False, indent=4)

new_student = {
    "name": "Mary",
    "age": 15,
    "grade": 9,
    "subjects": ["Math", "English", "Art"],
    "average_score": 11.0
}
students.append(new_student)
with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, ensure_ascii=False, indent=4)
print("----------------------------")
with open("students.json", "r", encoding="utf-8") as file:
    loaded_students = json.load(file)
print(loaded_students)
print("----------------------------")
for student in loaded_students:
    print(student)