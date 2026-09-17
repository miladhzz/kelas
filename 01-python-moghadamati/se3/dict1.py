dict1 = {
  "id": 10,
  "numbers": [10,20,30,40],
  "name": "reza"
}
dict1["family"] = "hatami"

print(dict1)
dict1.pop("name")
del dict1["family"]
print(dict1)