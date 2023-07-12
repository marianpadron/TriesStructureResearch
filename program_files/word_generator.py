from nltk.corpus import words
import random


"""
    CS 5008
    Fall 2023
    Final Research Project
    Marian Padron
    Word generator file, uses Python's NLTK library to generate lists of random words and writes to outfile
"""


if __name__ == "__main__":

    # Get a list of words form nltk.corpus and remove duplicates
    word_list = words.words()
    random_words = list(set(random.sample(word_list, 200000)))

    # Write to txt file
    with open("words_x_large.txt", "w") as outfile:
        for word in random_words:
            word = word.lower()
            # Write the string to the file
            outfile.write(word + "\n")

