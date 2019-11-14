# my_string = "hi, jamie"
# print(my_string)
# mike_string = "hi, mike"
# print(mike_string)

mike_and_jamie_baby_names = [
    "Marcus",
    "Aurelius",
    "James",
    "Jordan"
]

gender_determinant = {
    "Marcus": "boy",
    "Aurelius": "boy",
    "James": "boy",
    "Jordan": "girl"
}


# third_value_string = 'This is the third value:'
# print(third_value_string)
# third_value = mike_and_jamie_baby_names[2]
# print(third_value)
# print("this is the gender:")
# print(gender_determinant[third_value])

# for name in mike_and_jamie_baby_names:
#     print(name)
#     print(name)

# for name in mike_and_jamie_baby_names:
#     print("This is a name: " + name)
#     print("This is the gender: " + gender_determinant[name])


# a = 1
# a = a + 1
# print(a)

# Input is excel file with resident names and ID badges (name and associated badge ID number)
# Make dictionary of name and ID badge number
# Tally or sum number of times name/ID appears on all excel sheets
# for name in name list
#         tally = name + tally
#         print(tally)


tally = 0
numbers = [1, 6, 3, 69, 420, 101]
for number in numbers:
    tally = number + tally
print(tally)
