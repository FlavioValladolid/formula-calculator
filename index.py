
import json


# Opening JSON file
f = open(r'C:\Users\Flavio\Documents\SMK Python Projects\Formula calculator\recipes.json',)

# return JSON object as a dictionary
data = json.load(f)

# Iterating through the json list
for element in data:
    print(element)
# for layers in range(3):
#     dictionary_formulas["layers_{0}".format(layers)] = "hola"

# print(dictionary_formulas)

f.close()