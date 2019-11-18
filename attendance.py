import os
import pandas as pd
import math

# CONSTANTS

master_file_path = "data/MASTER.xlsx"

list_of_folder_names = [
    "data/B1/",
    "data/B2/",
    "data/B3/",
    "data/B4/",
    "data/B5/"
]

# GET ID TO NAMES

id_to_name = {}

df = pd.read_excel(master_file_path, index_row=0)

for i in df.index:
    id = df['ID'][i]
    name = df['Resident Name'][i]
    id_to_name[id] = name

# GET ATTENDANCE FOR IDS

id_to_attendance = {}


def file_paths():
    paths = []
    for dir_name in list_of_folder_names:
        for file_name in os.listdir(dir_name):
            paths.append(dir_name + file_name)
    return paths


def handle_row(i, df):
    badge_as_num = df['Badge'][i]
    if not math.isnan(badge_as_num):
        tally_for_res = None
        badge_as_int = int(badge_as_num)
        tally_for_res = id_to_attendance.get(badge_as_int, 0)
        id_to_attendance[badge_as_int] = tally_for_res + 1


files = file_paths()
for file_name in files:
    print("handing - " + file_name)
    dataframe = pd.read_excel(file_name, index_row=0)
    first_column = dataframe.columns[0]

    if first_column == 'Badge':
        for i in dataframe.index:
            handle_row(i, dataframe)
    elif first_column == 'ID':
        new_dataframe = pd.read_excel(
            file_name, sheet_name="SIGN IN", index_row=0)
        new_first_col = new_dataframe.columns[0]
        print("new_first_col = " + new_first_col)
        if new_first_col == 'Badge':
            for j in new_dataframe.index:
                handle_row(j, new_dataframe)
        else:
            print("SOME ISSUE" + file_name)
    else:
        print("MANUALLY MARK: " + file_name)

# PRINT ATTENDANCES

for key in id_to_attendance:
    if key in id_to_name:
        res_name = id_to_name[key]
        count = id_to_attendance[key]

        line = res_name + "ID (" + str(key) + ") came " + \
            str(count) + " times."
        print(line)
    else:
        print("Unknown Badge: " + str(key))
