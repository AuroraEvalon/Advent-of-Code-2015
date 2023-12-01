import re
import os

data = open("Day 1\\apartmentInput.txt", "r")
data = data.read()
increase = int(data.count("("))
decrease = int(data.count(")"))

print(increase - decrease)