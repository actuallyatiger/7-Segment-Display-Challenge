import re
import os


outputFile = "output_file.txt"

if os.path.exists(outputFile):
    os.remove(outputFile)

regexExclusions = "[kmqvwxz]"

longestWords = [""]

with open("words_alpha.txt", "r") as file:
    for word in file:
        word = word.strip()

        if (len(word) > len(longestWords[0])) and (not re.search(regexExclusions, word)):
            del longestWords
            longestWords = [word]
        elif (len(word) == len(longestWords[0])) and (not re.match(regexExclusions, word)):
            longestWords.append(word)


with open(outputFile, "w") as file:
    file.write("\n".join(longestWords))
