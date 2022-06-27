sample_dict = {
"name": "Kelly",
"age": 25,
"salary": 8000,
"city": "New york"}
# Keys to extract
keys = ["name", "salary"]

a={}
a = {i: sample_dict[i] for i in keys}

print(a)