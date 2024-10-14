list = {
    "1": "True",
    "2": "True",
    "3": "True",
    "4": "True",
    "5": "True",
    "6": "True",
    "7": "True",
    "8": "True",
    "9": "True", }

list["2"] = "False"
list["7"] = "False"
del list["3"]
list["4"] = None

print(list)


