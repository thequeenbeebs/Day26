# LIST COMPREHENSION

# How To Create Lists Using List Comprehension
#   Case where you create a new list from a previous list
#   new_list = [new_item for item in list]

numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]

#   Can also use things besides lists

name = "Angela"
new_list = [letter for letter in name]

#   Python Sequences: have a specific order; list, string, tuple, range
#   Can all be used for list comprehension

num_range = range(1, 5)
final_list = [num * 2 for num in num_range]

#   Conditional List Comprehension
#   new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) <= 4]
# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)

# How to Use Dictionary Comprehension
#   new_dict = {new_key:new_value for item in list}
#   creating a dictionary using shorter syntax
#   new_dict = {new_key:new_value for (key, value) in dict.items() if test}

import random

students_scores = {name: random.randint(1, 100) for name in names}

passed_students = {name: score for (name, score) in students_scores.items() if score >= 60}

print(passed_students)

# How to Iterate over a Pandas DataFrame
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#   Looping through dictionaries
# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)

#   Loop through a dataframe
# for(key, value) in student_data_frame.items():
#     print(key)

#   Loop through rows of a dataframe
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)