from hashmap import Hashmap
from hashing import simple_hash, djb2, jenkins_one_at_a_time_hash, fnv_hash
import csv
import tracemalloc
import time

"""
    CS 5008
    Fall 2023
    Final Research Project
    Marian Padron
    Test_hashmap file, runs a test script for running different calls to a hashmap.
"""


def insert_map(map, words):
    """
    Puts a list of words into a hashmap with a value.
    :param map: Hashmap object
    :param words: list of words
    :return: None
    """
    for i in range(0, len(words)):
        # Put word as key and its appearance in the list as the value
        map.map_put(words[i], i + 1)


def search_map(hashmap, words):
    """
    Gets each word in a list of words from the hashmap.
    :param hashmap: Hashmap object
    :param words: list of words
    :return: count of all the words looked up
    """
    count = 0
    for word in words:
        if (map.map_get(word) > 0):
            count += 1
    return count


if __name__ == "__main__":
    # Files to iterate through
    word_files = ["data_files/words_small.txt", "data_files/words_medium.txt", "data_files/words_large.txt", "data_files/words_x_large.txt"]
    
    hashes = [
        simple_hash,
        djb2,
        jenkins_one_at_a_time_hash,
        fnv_hash
    ]
    
    # Placeholder for data to write to csv
    hash_data = []
    
    for hash in hashes:
        
        # For csv
        insertion_data = [
            ["Insertion", "Speed", "Current Memory", "Peak Memory", "Words"],
        ]
        lookup_data = [
            ["Lookup", "Speed", "Current Memory", "Peak Memory", "Words"],
        ]
        
        # Iterate through files
        for w_file in word_files:
            insertion = []
            lookup = []
            
            # Get list of words within current file
            with open(w_file, "r") as file:
                words = [word.strip() for word in file.readlines()]
    
            # Add file name to data
            insertion.append(w_file)
            lookup.append(w_file)
            map = Hashmap(100000000, hash)  # initialize the hashmap with a given size and hash type
    
            #Insertion Call
            tracemalloc.start()  # start memory tracing
            start_time = time.time()  # start runtime
            insert_map(map, words)  # function call
            current, peak = tracemalloc.get_traced_memory()  # save memory usage
            tracemalloc.stop()
            end_time = time.time()
            runtime = end_time - start_time  # get runtime
    
            # Add data
            insertion.append(runtime)
            insertion.append(current)
            insertion.append(peak)
            insertion.append(map.map_get(words[-1]))
            insertion_data.append(insertion)
    
            # Search Call
            tracemalloc.start()  # start memory tracing
            start_time = time.time()  # start runtime
            total = search_map(map, words)  # function call
            current, peak = tracemalloc.get_traced_memory()  # save memory usage
            tracemalloc.stop()
            end_time = time.time()
            runtime = end_time - start_time  # get runtime
    
            lookup.append(runtime)
            lookup.append(current)
            lookup.append(peak)
            lookup.append(total)
            lookup_data.append(lookup)
    
        # Add data to one list
        hash_data.append([hash])
        hash_data.append(insertion_data)
        hash_data.append(lookup_data)
        hash_data.append([])
    
    # Write to csv file
    with open('hash_output.csv', "w", newline='') as file:
        writer = csv.writer(file)
        for line in hash_data:
            if len(line) > 1:
                for row in line:
                    writer.writerow(row)
            else:
                writer.writerow(line)
