import csv
from hashing import simple_hash, djb2, jenkins_one_at_a_time_hash, fnv_hash

"""
    CS 5008
    Fall 2023
    Final Research Project
    Marian Padron
    Collisions file, runs a test script on txt files with words and calculates the collision given a hashmap size and
    hash function.
"""


def print_collisions_only(array, data_size, line_data):
    """
    Writes collisions data into line_data list to be written to csv file.
    :param array: collision array
    :param data_size: size of array for calculating load factor
    :param line_data: list for adding data
    :return: line_data list
    """
    total = 0
    highest = 0
    counter = 0
    length = 0
    load = 0
    for i in range(data_size):
        if array[i] > 1:
            total += array[i]
            length += 1
            if array[i] > highest:
                highest = array[i]
        if array[i] > 0:
            counter += 1
            load += 1

    line_data.append(total)
    line_data.append(highest)
    line_data.append(counter)
    line_data.append(load / data_size)

    return line_data



ALGO_SIZE = 4  # amount of hashing functions
SIZE = 100000000  # size of array

hash_functions = [
    simple_hash,
    djb2,
    fnv_hash,
    jenkins_one_at_a_time_hash
]


if __name__ == "__main__":

    hash_txt = ["simple_hash", "djb2", "fnv_hash", "jenkins"]

    word_files = ["data_files/words_small.txt", "data_files/words_medium.txt", "data_files/words_large.txt", "data_files/words_x_large.txt"]

    collisions = [[] for _ in range(ALGO_SIZE)]

    for w_file in word_files:

        # Get list of words within current file
        with open(w_file, "r") as file:
            words = [word.strip() for word in file.readlines()]

        data_size = SIZE

        # Initialize table
        for i in range(ALGO_SIZE):
            collisions[i] = [0] * data_size

        # Open each file
        with open(w_file) as f:

            # Begin writing to csv
            with open("collisions.csv", "a", newline='') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csvwriter.writerow([w_file])
                csvwriter.writerow(["Hash", "Size", "Collisions", "Highest", "Filled Spot", "Load"])

                # Add to collisions
                for line in f:
                    for i in range(ALGO_SIZE):
                        loc = hash_functions[i](line.strip()) % data_size
                        collisions[i][loc] += 1

                # Check collision data and append to data lists
                for i in range(ALGO_SIZE):
                    line_data = [hash_txt[i]]
                    line_data.append(data_size)
                    new_line_data = print_collisions_only(collisions[i], data_size, line_data)
                    csvwriter.writerow(new_line_data)

                csvwriter.writerow([])
