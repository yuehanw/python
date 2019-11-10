print('Lab Exercise 09 \n')
# SI 506 2019F - Lab 9
# START LAB EXERCISE 09

# The following 3 problems will introduce you to working with tuples, JSON and CSV files.

# PROBLEM 1 (5 Points)

# In this problem you will demonstrate your understanding of tuples

# 1) Create tuples
# 2) Join tuples
# 2) Convert tuples to lists
# 3) Use tuples as keys in dictionaries


# Problem 01 SETUP - We provide you with a tuple to start the lab problems

language1 = ("English",)

# Problem 01 END SETUP

# BEGIN PROBLEM 1 SOLUTION

# Create a new tuple named <language2> with one element "Spanish"
language2 = ("Spanish",)
# Join two tuples <language1> and <language2> together to a new variable <languages>
languages = (language1 + language2)
# Convert the tuple <languages> to a list <languages_list>
languages_list = list(languages)
# Create a new dictionary named <languages_dict> and add the key-value pair <languages>-<languages_list> to the dictionary
# The expected answer is {("English", "Spanish"): ["English", "Spanish"]}
languages_dict = {languages:languages_list}

print(f"languages_dict = {languages_dict}")

# END PROBLEM 1 SOLUTION

# PROBLEM 2 (10 Points)
# In this problem, you will demonstrate your understanding of JSON

# 1) Parse Json
# 2) Convert list to JSON
# 3) Convert dictionary to JSON
# 4) Write JSON to file

# Problem 02 SETUP - We provide you with a JSON to start the problem. We also import the json library for you.

import json


json_dict = '{ "name":"John", "age":30, "city":"New York"}'
hobby = ["sing", "dance", "basketball"]

# Problem 02 END SETUP

# BEGIN PROBLEM 2 SOLUTION

# Parse <json_dict> into a Python dictionary named <profile>
profile = json.loads(json_dict)

# Convert <hobby> into a JSON named <json_list>
json_list = json.dumps(hobby)

# Add a new key-value pair "hobbies"-<hobby> to <profile>
profile["hobbies"] = hobby
# Convert <profile> into a new JSON named <json_dict2>
json_dict2 = json.dumps(profile)

# Write <json_dict2> into a text file named john.json
with open('john.json','w') as target:
	json.dump(json_dict2, target)

print(f"json_list = {json_list}")
print(f"json_dict2 = {json_dict2}")
# END PROBLEM 2 SOLUTION

# PROBLEM 3 (10 Points)

# In this problem you will demonstrate your understanding of CSV files
# 1) Read CSV file
# 2) Working with the values
# 3) Write CSV file

# Problem 03 SETUP - We provide you with a file name. We also import the csv library to start the problem
import csv
csv_name = "animals.csv"

# Problem 03 END SETUP

# BEGIN PROBLEM 3 SOLUTION

# Read the csv file with the name <csv_name> into a list of tuples (id, name) named <animals>
# You're suggested to use with open to open the file and use csv.reader to read the file
# The expected answer is [(1, "cat"), (2, "dog"), (3, "rabbit")]
animals = []
with open(csv_name,'r',encoding='utf-8-sig') as source:
	reader = csv.reader(source,delimiter = ',')
	for row in reader:
		animals.append(tuple(row))
# Add a new animal whose id is "4" and name is "bear" to <animals>
animals = animals[1:]
animals.append(('4','bear'))
print(animals)
# Write the updated <animals> into a CSV file called animals2.csv with "id", "name" as its header
# You're suggested to use with open to open the file and use csv.writer to write the file
with open('animals2.csv','w') as objfile:
	writer = csv.writer(objfile, delimiter = ',')
	writer.writerow(['id','name'])
	for item in animals:
		writer.writerow(item)
print(f"animals = {animals}")
# END PROBLEM 3 SOLUTION


# END LAB EXERCISE
