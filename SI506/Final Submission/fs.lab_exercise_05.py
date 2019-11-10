# START LAB EXERCISE 05
print('Lab Exercise 05 \n')

# [IMPORTANT NOTE]
# The autograder in Gradescope will directly test functions and files instead of variables
# So even though the variables printed seems right, it's possible your code didn't pass all the test cases.

# In this lab, we use txt files. Be very careful that a line in txt files
# should contain a new line "\n" character at the end of this line.

# PROBLEM 1 (5 Points)
# Define a function named "concatenate_name_type".
# The function accepts two arguments - one is "file_name", the other is "file_type". Both two arguments are strings.
# For given arguments, the function should return "<file_name>.<file_type>"
# Pass two defined variables "file_name", "file_type" to the function, assign the result to "full_file_name"
# Print "full_file_name".

# BEGIN PROBLEM 1 SOLUTION
f_name = "file1"
f_type = "txt"
full_file_name = None


def concatenate_name_type(file_name, file_type):
    return ''.join([file_name,".",file_type])

full_file_name=concatenate_name_type(f_name,f_type)

print(full_file_name)

# END PROBLEM 1 SOLUTION


# PROBLEM 2 (10 Points)
# Define a function named "write_into_file"
# The function accepts two arguments - one is "filename", the other is "file_content"
# "filename" is a string and "file_content" is a list of strings
# Open the file with "full_file_name", read all lines, store the last two lines into the variable "last_two_lines"
# Make sure that there is a new line character "\n" at the end of each line in "last_two_lines"
# Write "last_two_lines" into a new file called "file2.txt" using the function "write_into_file"
# Print "last_two_lines"

# BEGIN PROBLEM 2 SOLUTION
# def write_into_file(filename, file_content):

#     with open(full_file_name,'r') as source:
#         last_two_lines = source.readlines()[-2:]

#     with open(filename,'w') as target:
#         for each_line in last_two_lines:
#             target.write(each_line+'/n')

#     return last_two_lines

def write_into_file(filename, file_content):
    #print (file_content)
    with open(filename,'w') as target:
        for each_line in file_content:
            target.write(each_line+'\n')

with open(full_file_name,'r') as source:
    last_two_lines = [line.strip() for line in source.readlines()[-2:]]

write_into_file('file2.txt', last_two_lines)

print(last_two_lines)

# END PROBLEM 2 SOLUTION


# PROBLEM 3 (10 Points)
# Finally, put all you've learned together.
# Open each file with file_name in "file_name_list" and "file_type",
# read all lines and store those unique lines into the variable "unique_lines".
# Make sure that there is a new line character "\n" at the end of each line in "unique_lines".
# Write "unique_lines" into a new file called "summary.txt" using the function "write_into_file".
# Print "unique_lines".

# BEGIN PROBLEM 3 SOLUTION
file_name_list = ["file1", "file2", "file3"]
file_type = "txt"
unique_lines = []

for each_file in file_name_list:
    with open(each_file+'.'+file_type) as source:
        aList=source.readlines()
        for aLine in aList:
            if aLine.strip() not in unique_lines:
                unique_lines.append(aLine.strip())
            else:
                pass
        for eachLine in unique_lines:
            eachLine = ''.join([eachLine,'\n'])

print(unique_lines)

write_into_file('summary.txt', unique_lines)
# END PROBLEM 3 SOLUTION

# END LAB EXERCISE
