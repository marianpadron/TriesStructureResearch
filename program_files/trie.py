"""
    CS 5008
    Fall 2023
    Final Research Project
    Marian Padron
    Trie file, contains Node class to represent nodes in trie data structure and Trie class for creating the data
    structure.
"""


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

    def insert(self, word, value):
        """
        Insertion method for trie object, retuns -1 if not found.
        :param word: string key
        :param value: value for the key
        :return: None
        """
        # Begin at top of the tree
        current_word = word
        current_node = self.root
        while len(current_word) > 0:

            # If letter in node's children set current node to found node
            if current_word[0] in current_node.children:
                current_node = current_node.children[current_word[0]]
                current_word = current_word[1:]  # keep traversing the letters in the word

            # If letter doesn't exist in children create a new node
            else:
                new_node = Node()
                new_node.key = current_word[0]

                # If at the end of the word assign value
                if len(current_word) == 1:
                    new_node.value = value

                # Update values
                current_node.children[current_word[0]] = new_node
                current_node.num_children += 1
                current_node = new_node
                current_word = current_word[1:]

        # if word already exists, update its value
        current_node.value = value

    def lookup(self, word):
        """
        Search method for trie object.
        :param word: string key to find
        :return: the value at the key
        """
        current_word = word
        current_node = self.root

        # Traverse nodes letter by letter in word
        while len(current_word) > 0:
            if current_word[0] in current_node.children:
                current_node = current_node.children[current_word[0]]
                current_word = current_word[1:]

            # If no children nodes with letter or no value at node
            else:
                print("not in trie" + current_word)
                return -1
        if current_node.value is None:
            print("no value in this node")
            return -1
        return current_node.value

