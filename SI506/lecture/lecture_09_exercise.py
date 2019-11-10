#!/usr/bin/env python3

# Create a file handle, return list
path = 'whale_names.txt'
file_handle = open(path)
lines = #FIX ME
file_handle.close()

print(f"lines = {lines}\n")

# Extract headers (first row)
# Use str.rstrip() to remove newline \n
# Use str.split() to split string on comma
headers = lines[0].rstrip().split(',')

# Get whales only (skip header)
# Use str.rstrip() to remove newline \n
# Use str.split() to split string on comma
whales = []
for line in lines[#FIX ME]:
    whales.append(#FIX ME)

print(f"headers = {headers}")
print(f"whales = {whales}")


# Get common name by index position lookup
def get_common_name(names):
    """Return common name."""
    return names[headers.index(#FIX ME)]


# Open new file in write mode, get file handle
# Iterate over whales list, call function to return common name,
# and write common name to file
path = 'whale_common_names.txt'
file_handle = open(path, '#FIX ME')
#  Get whale names, write to file
for whale in whales:
    common_name = #FIX ME
    file_handle.write(f"{#FIX ME}\n")
file_handle.close()