# For use in playing Contact, to choose hard to guess words.
# https://en.wikipedia.org/wiki/Botticelli_%28game%29#Games_similar_to_Botticelli
#
# From a trie on letters of English words, outputs words with maximal sum of 
# branching factor along the path from root to word terminal

from puzzpy.wordsets.sowpods import SOWPODS

num_words = 100
words = SOWPODS
word_count = []
dicty = {}

for word in words:
    cur_dict = dicty
    for char in word:
        if char not in cur_dict:
            cur_dict[char] = {}
        cur_dict = cur_dict[char]

for word in words:
    cur_dict = dicty
    count = 0
    for char in word:
        count += len(cur_dict.keys())
        cur_dict = cur_dict[char]
    word_count.append((word, count))

for word in sorted(word_count, key=lambda word_count:-word_count[1])[:num_words]:
    print word[0]
