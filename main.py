import os
from aho_corasick import Node, ac_tree_creation, build_failure_links, patterns_in_text
from file_utils import read_txt

textFile = input("Introduce the path of the text file (.txt): ")
if not os.path.isfile(textFile):
    print(f"Error: File '{textFile}' does not exist.")
    exit()

patternFile = input("Introduce the path of the pattern file (.txt): ")
if not os.path.isfile(patternFile):
    print(f"Error: File '{patternFile}' does not exist.")
    exit()

text = read_txt(textFile).lower()
patterns_text = read_txt(patternFile).lower()

if not text.strip():
    print("Error: The text file is empty.")
    exit()

if not patterns_text.strip():
    print("Error: The pattern file is empty.")
    exit()

root = Node()
for line in patterns_text.strip().splitlines():
    word = line.strip()
    if word:
        ac_tree_creation(word, root)

build_failure_links(root)

results = patterns_in_text(text, root)

if results:
    for position, pattern in results:
        print(f"Found '{pattern}' at position {position}")
else:
    print("No patterns found.")
