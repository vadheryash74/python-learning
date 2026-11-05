import json

student = {
    "name": "Yash",
    "age": 21,
    "course": "BCA"
}

# Python object to JSON string
json_string = json.dumps(student)
print(json_string)

# JSON string to Python object
data = '{"name": "Yash", "age": 21}'
python_object = json.loads(data)
print(python_object)

# Write Python data to JSON file
with open("yash.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)

# Read JSON file
with open("yash.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

print(loaded_data)