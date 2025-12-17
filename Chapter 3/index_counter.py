import re
import sys

WORD_RE = re.compile(r'\w+')
index = {}

#opens the zen.txt file and reads in, matching the words and adding to index dict
#setdefault is used to add empty list if word is not found
#the example is also using regex to match words
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)

# display in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])