# ISML, Laborator 1
# wordcount.py
# Manghiuc Teodor-Adrian
# 382

"""

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys


# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def open_file(filename):

    print(filename)
    print()

    words = []

    f = open(filename, 'rt')    # able to read line by line
    for line in f:
        #print(line)
        word = line.split()
        words.append(word)

    # print(words)

    return words


def get_dictionary(words):

    aux = []

    for word in words:
        for w in word:
            x = w.lower()
            aux.append(x)

    # print(aux)
    aux.sort()
    # print(aux)

    dictionar = {}

    for a in aux:
        dictionar[a] = 0

    for a in aux:
        count = dictionar[a]
        count += 1
        dictionar[a] = count

    return dictionar


def print_words(filename):

    words = open_file(filename)

    dictionar = get_dictionary(words)

    # print(dictionar)

    for d in dictionar:
        print(d, dictionar[d])

    return dictionar


def extract(tuple):
    return tuple[0]


def print_top(filename):

    words = open_file(filename)

    dictionar = get_dictionary(words)

    # print(dictionar)

    swap = []   # nu mai merge dictionar ca se suprascriu valorile

    for d in dictionar:
        t = ()
        v = dictionar[d]
        t = (v, d)
        swap.append(t)

    # print(swap)

    swap_reversed = sorted(swap, key=extract, reverse=True)

    # print(swap_reversed)

    n = 20
    index = 0

    print(n, "most common words:")
    for s in swap_reversed:
        print(s[0], s[1])
        index += 1
        if index >= n:
            break

    return


###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
