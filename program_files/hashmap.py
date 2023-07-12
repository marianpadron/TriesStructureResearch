"""
    CS 5008
    Fall 2023
    Final Research Project
    Marian Padron
    Hashmap file, contains H_node class, and Hashmap class for creating a hashmap object.
"""


class H_node:
    """ Node class for hashmap."""

    def __init__(self, key: str, value: float):
        self.key = key
        self.value = value
        self.next = None


class Hashmap:
    """ Hashmap class."""

    def __init__(self, size: int, hash_type):
        """Initialize object with given array size, and type of hashing function."""

        self.size = size
        self.contents = [None] * size
        self.hash_type = hash_type

    def map_get(self, key: str) -> float:
        """
        Gets the value in hashmap of a given string key, returns -1 if can't find the key.
        :param key: str
        :return: float value at key
        """

        # Get hash
        index = self.get_hash(key) % self.size

        # If no value at hash
        if self.contents[index] is None:
            return -1.0
        else:
            # Get value
            cur = self.contents[index]
            while cur is not None:
                if cur.key == key:
                    return cur.value
                cur = cur.next
        return -1.0

    def map_put(self, key: str, value: float) -> None:
        """
        Puts a key value pair into the hash map.
        :param key: str 
        :param value: float associated with key
        :return: None
        """

        # Get hash
        index = self.get_hash(key) % self.size
        
        new_node = H_node(key, value) # initialize node
        
        # Add to index if empty
        if self.contents[index] is None:
            self.contents[index] = new_node
        else:
            # Iterate through linked list and add at the end
            cur = self.contents[index]
            if cur.key == key:
                cur.value = value
            while cur.next is not None:
                if cur.key == key:
                    cur.value = value
                    return
                cur = cur.next
            if cur.key == key:
                cur.value = value
            else:
                cur.next = new_node

    def get_hash(self, string: str) -> int:
        """
        Returns the hash value of a string using the hash function passed to the class object.
        :param string: key
        :return: int hash value
        """
        
        return self.hash_type(string)

