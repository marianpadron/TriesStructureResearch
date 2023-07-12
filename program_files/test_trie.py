import csv
from trie import Trie
import tracemalloc
import time

"""
    CS 5008
    Fall 2023
    Final Research Project
    Marian Padron
    Test_trie file, runs a test script that calls different methods of the trie data structure with different data sizes.
"""


def insert_trie(trie, words):
    """
    Insert list of words into the trie with given values.
    :param trie: Trie object
    :param words: list of words
    :return:
    """
    for i in range(0, len(words)):
        trie.insert(words[i], i + 1)  # adds order in list as value to word


def search_trie(trie, words):
    """
    Searches for words in list of words within a trie.
    :param trie: Trie object
    :param words: list of words
    :return: count of how many words where searched
    """
    count = 0
    for word in words:
        if (trie.lookup(word) > 0):
            count += 1
    return count


if __name__ == "__main__":

    # Data files
    word_files = ["data_files/words_small.txt", "data_files/words_medium.txt", "data_files/words_large.txt", "data_files/words_x_large.txt"]

    # For csv
    insertion_data = [
        ["Insertion", "Speed", "Current Memory", "Peak Memory", "Words"],
    ]

    lookup_data = [
        ["Lookup", "Speed", "Current Memory", "Peak Memory", "Words"],
    ]

    for w_file in word_files:
        # Get list of words within current file
        with open(w_file, "r") as file:
            words = [word.strip() for word in file.readlines()]

        # Add file name to csv data
        insertion = [w_file]
        lookup = [w_file]
        trie = Trie()

        # Insertion Call
        tracemalloc.start()  # start memory tracing
        start_time = time.time()  # start runtime
        insert_trie(trie, words)  # function call
        current, peak = tracemalloc.get_traced_memory()  # save memory usage
        tracemalloc.stop()
        end_time = time.time()
        runtime = end_time - start_time  # get runtime

        # Append to data list
        insertion.append(runtime)
        insertion.append(current)
        insertion.append(peak)
        insertion.append(trie.lookup(words[-1]))
        insertion_data.append(insertion)

        # Search Call
        tracemalloc.start()  # start memory tracing
        start_time = time.time()  # start runtime
        total = search_trie(trie, words)  # function call
        current, peak = tracemalloc.get_traced_memory()  # save memory usage
        tracemalloc.stop()
        end_time = time.time()
        runtime = end_time - start_time  # get runtime

        # Append to data list
        lookup.append(runtime)
        lookup.append(current)
        lookup.append(peak)
        lookup.append(total)
        lookup_data.append(lookup)

    # Write to csv file
    with open('trie_output.csv', "w", newline='') as file:
        writer = csv.writer(file)
        for row in insertion_data:
            writer.writerow(row)

        writer.writerow(" ")

        for row in lookup_data:
            writer.writerow(row)

