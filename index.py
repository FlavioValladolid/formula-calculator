
from tkinter import StringVar

dictionary_formulas = {}

for layers in range(3):
    dictionary_formulas["layers_{0}".format(layers)] = "hola"

print(dictionary_formulas)