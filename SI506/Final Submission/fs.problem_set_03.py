# SI 506 2019F - Problem Set 03

# SETUP
# We provide you with a selection of famous love quotes and who wrote them.
# In the future, such data will be provided in a file which you will read into python with some useful functions.
# However, for today, the teaching team has provided this list for you to use.

love_quotes = [
    "Love is not love which alters when it alteration finds",
    "Love, the itch, and a cough cannot be hid",
    "That love is all there is, Is all we know of love",
    "I am two fools, I know, for loving, and saying so",
    "Love lives on propinquity, but dies on contact",
    "You really have to love yourself to get anything done in this world",
    "The irony of love is that it guarantees some degree of anger, fear and criticism",
    "I see you everywhere, in the stars, in the river",
    "Respect is love in plain clothes",
    "If you want to be loved, be lovable",
]

authors = [
    "William Shakespeare",
    "Thomas Fuller",
    "Emily Dickinson",
    "John Donne",
    "Thomas Hardy",
    "Lucille Ball",
    "Harold H. Bloomfield",
    "Virginia Woolf",
    "Frankie Byrne",
    "Ovid",
]

# END SETUP


# PROBLEM 1
# Extract the indices of all the quotes which begin with "Love" into a new list named love_quotes_indices. Print love_quotes_indices.
# Note: You're not allowed to change the original quotes.
# Hint: Use for loop, if statement and string slicing.


# BEGIN PROBLEM 1 SOLUTION

love_quotes_indices = []
for i in range(len(love_quotes)):
    bagOfWords=love_quotes[i].strip().split()
    firstWord=bagOfWords[0]
    if len(firstWord)>=4 and firstWord[:4]=="Love":
        love_quotes_indices.append(i)

print(love_quotes_indices)

# END PROBLEM 1 SOLUTION


# PROBLEM 2
# Create quote-author pairs by concatenating the quotes indicated in love_quote_indices with the the corresponding author in authors.
# Concatenate the values using the format "<quote> - <author>" (the <text> are placeholders that your code should replace).
# Save these strings into the list quotes_with_author. Print quotes_with_author.


# BEGIN PROBLEM 2 SOLUTION

quotes_with_author = []
for index in love_quotes_indices:
    concatenation=love_quotes[index]+" - "+authors[index]
    quotes_with_author.append(concatenation)

print(quotes_with_author)

# END PROBLEM 2 SOLUTION


# PROBLEM 3
# Write a function named who_wrote_it which will return the author of a quote when given the combined string "<quote> - <author>".
# Apply the function to quotes_with_author and store the result in the list i_wrote_it.
# Sort the list i_wrote_it based on alphabetic order. Print i_wrote_it.
# BEGIN PROBLEM 3 SOLUTION

i_wrote_it = []

def who_wrote_it(quotes_with_author):
    return quotes_with_author.strip().split(" - ")[-1]
for quote in quotes_with_author:
    i_wrote_it.append(who_wrote_it(quote))

i_wrote_it.sort()
print(i_wrote_it)

# END PROBLEM 3 SOLUTION


# PROBLEM 4
# Write a function named count_words_in_quote which will return the number of words in a given quote.
# Apply the function to the quotes indexed by the first and the last elements in love_quotes_indices.
# Assign the word count values to the variables first_word_count and last_word_count as appropriate.
# Print first_word_count and last_word_count.
# Note: Words in quotes are not only separated by blanks, but also by comma.
# Hint: Use split(), if-else statement, len() or sum().


# BEGIN PROBLEM 4 SOLUTION
lst=[]
def count_words_in_quote(quote):
    return len(quote.strip().split())
for index in love_quotes_indices:
    lst.append(count_words_in_quote(love_quotes[index]))

first_word_count = lst[0]
last_word_count = lst[-1]

print(first_word_count, last_word_count)

# END PROBLEM 4 SOLUTION


# PROBLEM 5
# Love quotes don't necessarily use "love"!
# Write a function named is_quote_with_love, which will determine whether the given quote contains the words
# "love", "loving", "loved", "lovable", "Love" or not.
# If the quote contains one of the words the function should return True otherwise return False.
# Use a while loop and is_quote_with_love to identify all quotes without "love", "loving", "loved", "lovable", "Love"
# Once identified append the quote to the no_love_quotes list.
# Print no_love_quotes
# Hint: You can search on the characters 'lov' if you use a built-in string function to convert quote to lower case.

# BEGIN PROBLEM 5 SOLUTION
def is_quote_with_love(quote):
    trueWords=["love", "loving", "loved", "lovable", "Love"]
    for trueWord in trueWords:
             if trueWord in quote:
                 return True

    return False




no_love_quotes = []
for quuote in love_quotes:
    if is_quote_with_love(quuote)==False:
        no_love_quotes.append(quuote)




print(no_love_quotes)

# END PROBLEM 5 SOLUTION


# PROBLEM 6
# Finally, put all you've learned together.
# Reuse functions created above to sum up the word counts of quotes which contain "love", "loving", "loved", "lovable"
# or "Love" in love_quotes.
# Assign the total word count to the variable total_word_count.
# Print total_word_count.

# BEGIN PROBLEM 6 SOLUTION

total_word_count = 0

for aq in love_quotes:
    if is_quote_with_love(aq)==True:
        total_word_count+=(count_words_in_quote(aq))
print(total_word_count)

# END PROBLEM 6 SOLUTION

# END PROBLEM SET
