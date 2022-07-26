# import nltk
# from nltk.corpus import words
# from nltk.metrics.distance import (edit_distance, jaccard_distance, )
# from nltk.util import ngrams
# import pandas
#
# correct_spellings = words.words()
# spellings_series = pandas.Series(correct_spellings)
#
#
# def jaccard(entries, gram_number):
#     outcomes = []
#     for entry in entries:  # iteratively for loop
#         spellings = spellings_series[spellings_series.str.startswith(entry[0])]
#         distances = (
#             (jaccard_distance(set(ngrams(entry, gram_number)), set(ngrams(word, gram_number))), word)
#             for word in spellings)
#         closest = min(distances)
#         outcomes.append(closest[1])
#     return outcomes
#
#
# def jd_reco(entries=['cormulent', 'incendenece', 'validrate']):
#     """finds the closest word based on jaccard distance"""
#     return jaccard(entries, 3)
#
#
# def editreco(entries=['cormulent', 'incendenece', 'validrate']):
#
#     outcomes = []
#     for entry in entries:
#         distances = ((edit_distance(entry,
#                                     word), word)
#                      for word in correct_spellings)
#         closest = min(distances)
#         outcomes.append(closest[1])
#     return outcomes
#
#
# # userinput = []
# # for i in range(0, 3):
# #     word = input("threa woeds pleese: ")
# #     userinput.append(word)
# #
# # jd_reco(userinput)
#
# word = "threa woeds pleese:"
# print(editreco(word.split()))
# print(jd_reco(word.split()))

import pandas as pd
import os
import numpy as np
import textdistance
import re
from collections import Counter
from glob import glob

path = "C:\\Archive"
path_list = [y for x in os.walk(path) for y in glob(os.path.join(x[0], '*.txt'))]
words_dict = {}

# For each file we add all the words and their locations.
# for index in range(len(path_list)):
for path_index in range(1):
    file_to_read = open(path_list[path_index], 'r', encoding='utf-8')


words = []

with open('auto.txt', 'r') as f:
    file_name_data = f.read()
    file_name_data = file_name_data.lower()
    words = re.findall('w+', file_name_data)
# This is our vocabulary
V = set(words)

print("Top ten words in the text are:{words[0:10]}")
print("Total Unique words are {len(V)}.")

word_freq = {}
word_freq = Counter(words)
print(word_freq.most_common()[0:10])

probs = {}
Total = sum(word_freq.values())
for k in word_freq.keys():
    probs[k] = word_freq[k]/Total


def my_autocorrect(input_word):
    input_word = input_word.lower()

    if input_word in V:
        return('Your word seems to be correct')
    else:
        sim = [1-(textdistance.Jaccard(qval=2).distance(v,input_word)) for v in word_freq.keys()]
        df = pd.DataFrame.from_dict(probs, orient='index').reset_index()
        df = df.rename(columns={'index':'Word', 0:'Prob'})
        df['Similarity'] = sim
        output = df.sort_values(['Similarity', 'Prob'], ascending=False).head()
        return(output)

my_autocorrect('neverteless')