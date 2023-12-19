# aoc_day1
print("aoc_day1 module loaded")


class TrieNode:
    def __init__(self, char='*'):
        self.char = char
        self.is_end = False
        self.children = {}
        self.parents = {}

    def append_child(self, char):
        new_child = TrieNode(char)
        new_child.parents[char] = self.char
        self.children[char] = new_child

    def get_parents(self):
        # Return parents as a string
        result = []
        curr_node = self
        while curr_node.char != '*':
            result.append(curr_node.char)
            curr_node = curr_node.parents[curr_node.char]
        return ''.join(result[::-1])


class Trie:
    def __init__(self):
        self.ends = set()
        self.parents = {}


digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_digit(word):
    # We assume we are given valid input here.
    i, j = 0, len(word) - 1
    first, sec = 0, 0
    found_first, found_sec = False, False
    while not (found_first and found_sec):
        if not found_first and word[i].isdigit():
            first = int(word[i])
            found_first = True
        if not found_sec and word[j].isdigit():
            sec = int(word[j])
            found_sec = True
        i += 1
        j -= 1
    return int(str(first) + str(sec))


def get_first(word):
    # The first digit might also be spelled out, so we need to check for that.
    i = 0
    while i < len(word):
        # If we found a digit, we are done.
        if word[i].isdigit():
            return word[i]
        # Otherwise check if the next word is in the digits map
        for key in digits.keys():
            if i + len(key) - 1 < len(word) and word[i:i + len(key)] == key:
                return digits[key]
        i += 1


def get_last(word):
    i = len(word) - 1
    while i > -1:
        if word[i].isdigit():
            return word[i]
        for key in digits.keys():
            if i - len(key) > -1 and word[i - len(key) - 1:i] == key:
                return digits[key]
        i -= 1


def get_digit2(word):
    first, sec = get_first(word), get_last(word)
    return int(str(first) + str(sec))


def construct_trie():
    root = TrieNode()
    tmp = root
    for key in digits.keys():
        for char in key:
            root.append_child(char)
            root = root.children[char]
        root.is_end = True
    return tmp


def get_first_trie(word, trie):
    pass


def get_last_trie(word, trie):
    pass


def get_digit3(word, trie):
    first, sec = get_first_trie(word, trie), get_last_trie(word, trie)
    return int(str(first) + str(sec))


def main():
    root = construct_trie()
    # Two things we are doing here:
    # 1. finding a 2 digit number based on the first and last integer found
    # 2. adding all the 2 digit numbers together
    _sum = 0
    with open("aoc_day1/input.txt", "r") as f:
        for line in f:
            word = line
            _sum += get_digit3(word, root)
    print(_sum)
