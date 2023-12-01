import re

data = open("apartmentInput.txt", "r")
increase = int(data.count("("))
decrease = int(data.count(")"))

output = increase+decrease

print(output)