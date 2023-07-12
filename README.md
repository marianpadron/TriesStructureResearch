# Research Paper

Name: Marian Padron

Semester: Fall 2023

Topic: Tries Data Structure

Link The Repository: https://github.com/Spring23-CS5008-BOS-Lionelle/research-project-mpadron-neu.git

## Introduction

Tries (also known as a prefix trees) are a type of abstract data structure used for locating specific keys within a set. They are implemented in the form of a sorted tree and are mainly used for storing and searching strings. The idea of using tries was first proposed in 1912 by mathematician Axel Thue as a way to represent a set of strings. In 1959, tries were described in the context of computer science by René de la Briandais, and in 1960 they were coined as 'tries' by Professor Edward Fredkin, who named them for 'retrieval trees'. They were originally developed to support information retrieval and natural language processing, and are now used in various computer applications, such as search engines, autocomplete, and network routing tables.

The use of tries for fast searching in a large collection of strings interested me, particularly because of their application within search engines and other tools such as autocomplete and spell checker. Because tries are typically used to store associative arrays, they are often compared to hash tables. Thus, the advantages and disadvantages of both are often debated depending on their application. For this reason, I decided to conduct more research on tries, try to implement them by using Python programming, and run them against a hash table to compare what the speed and memory implications of this data structure are relative to a more widely used structure such as a hash table.

## Overview of Tries Structure

A trie is a multiway tree data structure that starts with an empty root node. The root node holds children nodes representing characters in a string. Unlike other tree-based data structures, tries may not be necessarily balanced, and each child node can have as many nodes within the chosen alphabet. If the trie is being implemented in English, each child node could possibly have up to 26 children. When searching through the tree, we begin at the root node and find a child node that holds the first character in our string. We traverse to that node and perform the same check for the second character in our string. The tree will continue to be traversed until it finds the desired word, at which point it can access the allotted value within the node that represents the end of the word. If no children nodes are found that correspond with a given character, then new nodes will be added for each letter until we reach the end of the word. For this reason, one can think of every internal node in the tree as being a prefix for all the possible string combinations below it.

[![](https://mermaid.ink/img/pako:eNpFkEsOgjAURbdC3uiS6AYYmKj1D2r8xEknDS1KIpRgGRjC3i2lxA6a23N6m_S1lGqpKKJnLapXcGO8DOyaAxetTRgG0-ksWNhTGHrjyB7YenkAdqPcOxIDJy8T4DHK2JEjkHh5BlajXDiy_Dc3wN3HLXD0cQewsbJ0hP0ra_f0IJkjK2Ddk4H1O02oUHUhcmn_3PaEk3mpQnGKbJQqE83bcOJlZ6-Kxujrt0wpMnWjJtRUUhjFcmGnVVCUiffHUiVzo-tkmGOqyyx_UvcDxNNWQg?type=png)](https://mermaid.live/edit#pako:eNpFkEsOgjAURbdC3uiS6AYYmKj1D2r8xEknDS1KIpRgGRjC3i2lxA6a23N6m_S1lGqpKKJnLapXcGO8DOyaAxetTRgG0-ksWNhTGHrjyB7YenkAdqPcOxIDJy8T4DHK2JEjkHh5BlajXDiy_Dc3wN3HLXD0cQewsbJ0hP0ra_f0IJkjK2Ddk4H1O02oUHUhcmn_3PaEk3mpQnGKbJQqE83bcOJlZ6-Kxujrt0wpMnWjJtRUUhjFcmGnVVCUiffHUiVzo-tkmGOqyyx_UvcDxNNWQg)

In the above trie we have an empty root node with two children, "R" and "H". If you traverse through their children you find the the node "R" maps to the letter "O" which then becomes the prefix for the words "roof", "round" and "room". Similarly, the child node "H" maps to the words "hi", "how", and "home". A good tool to visualize how tries insert and find nodes can be found [here.](https://www.cs.usfca.edu/~galles/visualization/Trie.html) 

## Time and Space Complexity

The time and space complexity of a trie will depend on factors such as the size/type of the alphabet used, the number of keys stored, and the length of the keys. Because we must traverse a node in the tree for each character in the key, the Big O time complexity of a trie for insertion, searching, and deletion is O(n), where n is the length of the string being searched. Relative to a hash table, after a key has been converted to a hash, the lookup and insertion time within the table is O(1). This is only assuming a very good hash function that limits collisions within the table. Since tries don’t have the problem of collisions, the worst-case performance for a trie is better than that of a poorly implemented hash table.

|Time Complexity | Space Complexity |
|----------------|------------------|
|      O(n)      |     O(n * m)     |

In terms of memory usage, the trie requires more overhead to retrieve a whole string as it must have access to all potential children nodes before it reaches the end of the string. The space complexity for a trie is O(n * m), where n is the number of strings stored in the trie and m is the average length of those strings. This is because the total number of nodes in the trie is proportional to the total number of characters in all the strings. However, the space complexity can be reduced if many strings in the trie share a common prefix. In general, hash tables have a space complexity of O(n). However, hash tables do have the issue of load factor and having to pre-allocate a good amount of memory to avoid collisions, which is an important consideration in terms of memory.

## Analysis Approach and Implementation

I used the comparison between hash tables and tries as my primary approach for conducting an empirical analysis on the tries data structure. To study the structure, I ran its insertion and retrieval methods against varying amounts of data and compared its runtime and memory usage to that of a hash table.

I began by researching how a trie tree would be implemented with code and opted for writing a simple approach in Python. For this I created a Node class representing each node within the trie, which holds a key, value, and reference to its children. The main trie operations are written within a Trie class, which uses the nodes to build its structure. The two main functionalities of a trie structure are insertion and retrieval. The code for insertion works by starting at the root node and checking the first character in the string against the root’s children. Once a node has been found, our current node will be set to the child node and the same check will be done on its children for the next character in the string. Once we reach a node in which there is no corresponding child node, for each letter following, a new node will be added to the previous one. Retrieval works in a similar matter, traversing the tree until the current node becomes the node representing the last character in the searched string. After implementing these functionalities I proceeded to test the structure, and as I refactored code and fixed some errors, I scaled up the size of my tests until I felt comfortable with the structure handling large amounts of data.

    class Node:
    """Node class, for creating nodes within trie data structure."""

        def __init__(self):
            """Initialize with key, value, children, and number of children."""
            self.key = None
            self.value = None
            self.children = {}
            self.num_children = 0


    class Trie:
    """ Trie class for representing a trie data structure."""

        def __init__(self):
            """Initialize with an empty root node."""
            self.root = Node()

For the hash table I used my implementation of a hash table for Homework 9 of this class and translated it to Python code. To account for the varying performance of a hash table given its hashing function, I ran the same tests conducted on the trie with different hashing methods on the hash table. A simple hashing function (using ASCII values), a DJB2 function, FNV function, and Jenkins One-at-a-Time hash were used. Although all results were looked at, my analysis mainly focused on the behavior of tables with the FNV and Jenkins hash, given as they are more effective in terms of hashing and collision prevention.

As for the test data itself, I used Python’s Natural Language Toolkit (NLKT) library to create a Python file that generates random words in the English language. With it, I created txt files containing a list of words, with approximately 1,000 words ([words_small.txt](data_files/words_small.txt)), 10,000 words ([words_medium.txt](data_files/words_medium.txt)), 100,000 words ([words_large.txt](data_files/words_large.txt)), and 200,000 words ([words_x_large.txt](data_files/words_x_large.txt)). Because a trie would have better insertion and lookup time when dealing with already existing words, I decided to remove any potential duplicates from the lists. So, the txt files with larger amounts of data may be smaller by a couple of values, but for the purposes of this report I will refer to them by the rounded amount. I also investigated potentially passing through even larger data, but there are only so many words in the English language, and the NLKT didn’t allow for number much higher than 200,000.

Below are the program files used to test the data strucutes.
* [trie.py](program_files/trie.py), contains the main trie structure
* [test_trie.py](program_files/test_trie.py), tests the trie structure
* [hashmap.py](program_files/hashmap.py), contains the main hashmap structure
* [test_hashmap.py](program_files/test_hashmap.py), tests the hashmap structure
* [hashing.py](program_files/hashing.py), contains the different hashing functions used by the hashmap
* [word_generator.py](program_files/word_generator.py), writes txt files with random English words
* [collisions.py](program_files/collisions.py), tests amount of collisions caused in hashmap with different load factor and hashing fucntion

Once I had all my programs and data files, I ran an insertion and search test on all the files for the trie and each implementation of the hash table. The Python tests inserted all words in the txt file and proceeded to retrieve them. For each operation, I used Python’s [time](https://docs.python.org/3/library/time.html) and [tracemalloc](https://docs.python.org/3/library/tracemalloc.html ) modules to keep track of the run time and memory usage per call.

## Empirical Data

### Collisions

To better gauge and compare the behavior of the hash map relative to the trie structure, I conducted the above-mentioned tests with a hash map of an initialized array at the size of the passed words and another with an initialized array of 100 million (500x the size of the largest data file of 200,000 words). This was to better visualize how collisions might play a role in skewing my data towards the trie preforming better for both the speed and memory tests. 

<div style="display: flex; justify-content: space-between;">
<img src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSDbUPjwEKUPDfDQzZK37mHi4TUXc4BZKEoekN5IKOFS_AnjFhocJ4Bj0vblxH50MHgHskQvJcuTO3B/pubchart?oid=1738172052&amp;format=image" alt="p_iter_dp" style="width:50%; height:50%"/>
<img src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSDbUPjwEKUPDfDQzZK37mHi4TUXc4BZKEoekN5IKOFS_AnjFhocJ4Bj0vblxH50MHgHskQvJcuTO3B/pubchart?oid=547298304&amp;format=image" alt="p_iter_dp" style="width:50%; height:50%"/>
</div>

As can be seen from the two bar graphs, although the collision amounts between the hash table initialized at word count and the table initialized at size 100 mil are vastly greater in the former, there are still a significant amount of collisions happening once the passed data size reaches the 100,000 mark. This is despite the initialized array being around 1,000x greater than the data load. Another thing to note is that when passed with the largest data file, the load factor for the hash tables initialized at word count stayed around 0.63, and those initialized at the large count had a load factor of around 0.001. The fact that there are collisions present within the hash tables may be of importance when further comparing the behavior of the trie and the table.

### Speed Analysis

<div style="display: flex; justify-content: space-between;">
<img src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSDbUPjwEKUPDfDQzZK37mHi4TUXc4BZKEoekN5IKOFS_AnjFhocJ4Bj0vblxH50MHgHskQvJcuTO3B/pubchart?oid=1016699300&format=image" alt="p_iter_dp" style="width:50%; height:50%"/>
<img src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSDbUPjwEKUPDfDQzZK37mHi4TUXc4BZKEoekN5IKOFS_AnjFhocJ4Bj0vblxH50MHgHskQvJcuTO3B/pubchart?oid=860130258&format=image" alt="p_iter_dp" style="width:50%; height:50%"/>
</div>

In the following speed graphs, the vertical axis represents how long it took each structure to preform the operations. The graphs provided above show a speed analysis with hash tables initialized at data size. One can see that the trie preforms slower at inserting words than the hash table with the FNV and DBJ2 hashes, but still preforms better than the Jenkins table. In terms of searching for words, the trie preforms better than all three implementations of the hash table.

<div style="display: flex; justify-content: space-between;">
<img src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSDbUPjwEKUPDfDQzZK37mHi4TUXc4BZKEoekN5IKOFS_AnjFhocJ4Bj0vblxH50MHgHskQvJcuTO3B/pubchart?oid=1241946334&format=image" alt="p_iter_dp" style="width:50%; height:50%"/>
<img src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSDbUPjwEKUPDfDQzZK37mHi4TUXc4BZKEoekN5IKOFS_AnjFhocJ4Bj0vblxH50MHgHskQvJcuTO3B/pubchart?oid=1994237320&format=image" alt="p_iter_dp" style="width:50%; height:50%"/>
</div>

With tables initialized at the larger size, both Jenkins and DBJ2 preform worse than the trie at insertion, which is somewhat matched by the FNV hash table. For lookup the trie still preforms faster than all three implementations of the hash table.

### Memory Usage

<div style="display: flex; justify-content: space-between;">
<img src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSDbUPjwEKUPDfDQzZK37mHi4TUXc4BZKEoekN5IKOFS_AnjFhocJ4Bj0vblxH50MHgHskQvJcuTO3B/pubchart?oid=603777352&format=image" style="width:50%; height:50%"/>
<img src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSDbUPjwEKUPDfDQzZK37mHi4TUXc4BZKEoekN5IKOFS_AnjFhocJ4Bj0vblxH50MHgHskQvJcuTO3B/pubchart?oid=1210084750&format=image" alt="p_iter_dp" style="width:50%; height:50%"/>
</div>

The trend being established for the trie is reinforced  when looking at its memory performance when inserting and searching. For the following graphs I directly compared the trie’s behavior with the FNV hash table, since it was the better preforming implementation. When inserting items into the tree, the trie requires a lot more current memory, and peaks at a higher value than the hash table. However, when looking up keys, the current memory usage of the trie is about the same as that of the hash table, with the hash table actually peaking more than the trie. Although the behavior of the data is similar when run with the smaller data file and on the hash tables initialized at word count, I’ve included links the other graphs below.
* [Insertion Memory Usage (small file, at list size)](https://docs.google.com/spreadsheets/d/e/2PACX-1vSDbUPjwEKUPDfDQzZK37mHi4TUXc4BZKEoekN5IKOFS_AnjFhocJ4Bj0vblxH50MHgHskQvJcuTO3B/pubchart?oid=575121581&format=image)
* [Insertion Memory Usage (large file, at list size)](https://docs.google.com/spreadsheets/d/e/2PACX-1vSDbUPjwEKUPDfDQzZK37mHi4TUXc4BZKEoekN5IKOFS_AnjFhocJ4Bj0vblxH50MHgHskQvJcuTO3B/pubchart?oid=936588105&format=interactive)
* [Lookup Memory Usage (small file, at list size)](https://docs.google.com/spreadsheets/d/e/2PACX-1vSDbUPjwEKUPDfDQzZK37mHi4TUXc4BZKEoekN5IKOFS_AnjFhocJ4Bj0vblxH50MHgHskQvJcuTO3B/pubchart?oid=139175139&format=image)
* [Lookup Memory Usage (large file, at list size)](https://docs.google.com/spreadsheets/d/e/2PACX-1vSDbUPjwEKUPDfDQzZK37mHi4TUXc4BZKEoekN5IKOFS_AnjFhocJ4Bj0vblxH50MHgHskQvJcuTO3B/pubchart?oid=387403034&format=image)
* [Insertion Memory Usage (small file, at large size)](https://docs.google.com/spreadsheets/d/e/2PACX-1vSDbUPjwEKUPDfDQzZK37mHi4TUXc4BZKEoekN5IKOFS_AnjFhocJ4Bj0vblxH50MHgHskQvJcuTO3B/pubchart?oid=566345889&format=image)
* [Lookup Memory Usage (small file, at large size)](https://docs.google.com/spreadsheets/d/e/2PACX-1vSDbUPjwEKUPDfDQzZK37mHi4TUXc4BZKEoekN5IKOFS_AnjFhocJ4Bj0vblxH50MHgHskQvJcuTO3B/pubchart?oid=1179052416&format=image)

### Summary

Overall, the trie displayed faster search speed than that of the hash table. Despite hash table generally having an average search time of O(1), we can see that the collisions caused by such a large data size could’ve contributed to a slower runtime for the hash tables over the tries in lookups. In terms of insertion, the trie preformed a bit slower than the hash map (depending on the hashing function), but it stayed generally at around the same speeds. Tries overall require more current memory for storing its values, and the memory peaks for tries are certainly higher when it comes to insertion. When searching, the memory peak of the hash table is a bit higher than that of the trie, but the hashing function used and load factor must be taken into account.

## Considerations

While writing out the code for the trie and running the tests proved to be thought provoking and interesting, there are some aspects in my approach that I would possibly give more consideration to if looking to expand on this research. I had some challenges trying to isolate factors that might make my hash table perform worse than my trie, such as the need for an effective hash function to avoid collisions and providing a good load factor. That same consideration should be taken into account when considering what type of data structure you would like to implement. I was also a bit surprised to see the trie’s speed and memory performance when searching for items. Given that a good hash map in general has a O(1) search time, it surprised me to see that the tries average runtime of O(n) outperformed the hash map. However, this is likely due to the collisions, so perhaps using a more complex hashing method might have produced results more in favor of the hash map. I also would’ve liked to have researched a bit more how my Python program was allocating and using memory during the different function calls. With more time, I would’ve implemented a delete function and run tests on its performance relative to the insertion and lookup. Lastly, while conducting more research, I found that tries can be made to insert items alphabetically, which I found particularly interesting for its application in searching and sorting.

## Applications

Because of its effectiveness in storing and searching sets of strings or sequences, tries have several different applications. In the field of natural language processing, tries are particularly used for tools such as spell checking and autocomplete. Depending on how the trie is implemented, with a provided prefix, a trie can generate different word or sentence suggestions which can then be sorted and provided to a user. In search engines, tries are used to enable fast and efficient search in a large corpus of text data. Alongside spell checking and autocompletion, search engines use tries to quickly find all the documents that contain a particular word or combination of words. 

In addition to its effectiveness is longest suffix or prefix matching, tries can also be implemented for structures such as radix trees which are often used in IP routing. Additionally, research has been conducted on how tries can be an effective data structure for [data mining algorithms](https://www.sciencedirect.com/science/article/pii/0895717703900586). Branching outside the field of computer science, tries’ strength with string patterns has found applications within [DNA sequencing](https://dl.acm.org/doi/fullHtml/10.1145/3445967) where it can be used for genomic research.


## Conclusion

While conducting this research, I learned about a new data structure with powerful applications. Learning about how my phone may implement a tries data structure as a tool to spell check or autocomplete my text was particularly interesting to me because it’s an application that everyone uses day to day. Given the empirical analysis, I was also able to better understand why a trie might be a more effective tool when wanting to lookup data, but not necessarily add it. This makes sense when considering that tries are usually used for things such as dictionaries and text queries.

Whether one data structure should be used over the other is completely dependent on the type of data that one will be using the structure for. Although trie seemed to perform worse than hash tables in terms of insertion, they are still particularly good at searching for a key. Tries can also have more specific implementations that a hash table is not able to provide, such as finding words that fit a prefix. A hash table is very efficient in terms of adding data, but it only supports the exact match of a whole string. In the end, the implications of each data structure must be weighted alongside its use to find which is the best fit for a particular program.

## References
* Data structures to represent a set of $k$-long DNA sequences data structures to represent a set of -long DNA sequences. Data Structures to Represent a Set of -long DNA Sequences. (n.d.). Retrieved from https://dl.acm.org/doi/fullHtml/10.1145/3445967 
* Doglio, F. (2022, December 5). Advanced Data Structures and algorithms: "tries". Medium. Retrieved April 23, 2023, from https://blog.bitsrc.io/advanced-data-structures-and-algorithms-tries-47db931e20e 
* F. Bodon, &amp; L. Ronyai. (2003, December 18). Trie: An alternative data structure for data mining algorithms. Mathematical and Computer Modelling. Retrieved April 23, 2023, from https://www.sciencedirect.com/science/article/pii/0895717703900586 
* GeeksforGeeks. (2022, December 15). Hash table vs trie. GeeksforGeeks. Retrieved from https://www.geeksforgeeks.org/hash-table-vs-trie/ 
* GeeksforGeeks. (2023, February 20). Trie: (insert and search). GeeksforGeeks. Retrieved from https://www.geeksforgeeks.org/trie-insert-and-search/ 
* Kumar, R. (2020, June 6). IP-model (storing IP addresses in radix tree). Medium. Retrieved from https://medium.com/@rakesht2499/ip-model-radix-tree-implementation-cc4485e68a9e 
* TRACEMALLOC - trace memory allocations. Python documentation. (n.d.). Retrieved from https://docs.python.org/3/library/tracemalloc.html 
* Trie data structure - javatpoint. www.javatpoint.com. (n.d.). Retrieved April 23, 2023, from https://www.javatpoint.com/trie-data-structure 
* Tries. Brilliant Math & Science Wiki. (n.d.). Retrieved from https://brilliant.org/wiki/tries/#applications 
* Wikimedia Foundation. (2023, April 20). Trie. Wikipedia. Retrieved April 23, 2023, from https://en.wikipedia.org/wiki/Trie 
* Wu, W. by: G. (2023, March 11). Hash table vs. Trie (prefix tree). Baeldung on Computer Science. Retrieved from https://www.baeldung.com/cs/hash-table-vs-trie-prefix-tree#:~:text=Although%20the%20hash%20table%20has,alphabetic%20order%20with%20a%20trie. 
