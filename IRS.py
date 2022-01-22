import numpy as np
import fnmatch
import os

# Here we have intialized some variables, you can add more if required.

file_count = 0             # file_count to count number of files
files_dict = {}            # files_dic to store count of every file
unique_word_set = set()    # unique_word_set to store all the unique words in a set

# Your code starts here
path = os.walk("./DATA")
count = 0
for root, directories, files in path:
    for file in files:
        # total files
        file_count += 1

        # count of files
        files_dict[file] = count
        count += 1
# Your code ends here

# write code to print all the unique words in every file and store them in a set
# Your code starts here
unique_words = set()

for file in files_dict.keys():
    f = open(f"./DATA/{file}", "r")
    string = f.read()
    for word in string.split():
        if word not in unique_words:
            unique_words.add(word)

# Your code ends here

# --> Term document matrix <--
mat = np.zeros((len(files_dict), len(unique_words)))

# --> dict of unique words <--
words_dict = dict()
count = 0
for word in unique_words:
    if word not in words_dict:
        words_dict[word] = count
        count += 1

# Your code ends here

# --> Fill the term doc matrix <--
# Your code starts here
for file in files_dict.keys():
    f = open(f"./DATA/{file}", "r")
    string = f.read()
    for word in unique_words:
        for value in string.split():
            if word in value:
                row = files_dict[f"{file}"]
                col = words_dict[f"{word}"]
                mat[row][col] = 1

# Your code ends here

# --> For user query make a column vector of length of all the unique words present in a set <--
# Your code starts here

query_mat = np.zeros((1, len(unique_words))).T

# Your code ends here

query = input("\nWrite something for searching: ")
# Check every word of query if it exists in the set of unique words or not
# If exixts then increment the count of that word in word dictionary

# Your code starts here
missing_word = set()
found_word = set()
for word in query.split():
    if word in unique_words:
        found_word.add(word)
        col = words_dict[word]
        query_mat[col][0] += 1
    else:
        missing_word.add(word)

# Your code ends here

# <-- Matrix multiplication <--
# Your code starts here
resMat = np.matmul(mat, query_mat)
maxRes = resMat.max()
index = 0
for i in range(0,len(resMat)):
    if maxRes == resMat[i][0]:
        index = i
        break

# Your code ends here

# --> Write the code to identify the file_name having maximum value in the resultant vector and display its contents <--
# Your code starts here
key_list = list(files_dict.keys())
val_list = list(files_dict.values())

# print key with val 100
position = val_list.index(index)
file = key_list[position]

print("\nShowing result for: ", found_word)
print("\nMissing words: ", missing_word)

f = open(f"./DATA/{file}", "r")
string = f.read()
print("\nResult: ", string)

# Your code ends here
