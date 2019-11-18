import os

list_of_folder_names = [
    "data/B1/",
    "data/B2/",
    "data/B3/",
    "data/B4/",
    "data/B5/"
]

for folder_name in list_of_folder_names:
    list_of_file_names = os.listdir(folder_name)
    for file_name in list_of_file_names:
        print(file_name)
