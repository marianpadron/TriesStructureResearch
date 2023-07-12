"""
    CS 5008
    Fall 2023
    Final Research Project
    Marian Padron
    Hashing file, contains different hashing functions. Primarily taken from hashing lab from class.
"""

FNV_PRIME_32 = 16777619
FNV_OFFSET_32 = 2166136261
DJB2_PRIME = 5381

def simple_hash(key):
    """The simple hash, for each character in key, sum the ascii values
    return that sum as the hash"""

    hash_val = 0
    for char in key:
        hash_val += ord(char)
    return hash_val

def djb2(key):
    """Start with prime number DJB2_PRIME as hash
    for every character in key,
    hash = hash * 33 + c
    return hash"""

    hash_val = DJB2_PRIME
    for char in key:
        hash_val = ((hash_val << 5) + hash_val) + ord(char)
    return hash_val

def fnv_hash(key):
    """FNV hash function"""

    hash_val = FNV_OFFSET_32
    for char in key:
        hash_val ^= ord(char)
        hash_val *= FNV_PRIME_32
    return hash_val

def jenkins_one_at_a_time_hash(key):
    """Jenkins one-at-a-time hash function"""

    hash_val = 0
    for char in key:
        hash_val += ord(char)
        hash_val += (hash_val << 10)
        hash_val ^= (hash_val >> 6)
    hash_val += (hash_val << 3)
    hash_val ^= (hash_val >> 11)
    hash_val += (hash_val << 15)
    return hash_val
