import os
from glob import glob
import re
import json


def import_dictionary_from_json(path: str) -> dict:
    with open('file.txt') as json_file:
        data = json.load(json_file)['words_dic']
        for key, value in data.items():
            print(key)
    return data

def search_word(str_input:str,input_words:dict):
    input_words = list(filter(None, str_input))
    if all(str in str_input for name in input_words):
        first_word = str_input.split()[0]



def user_service():
    str_input=input("The system is ready. Enter your text")
    search_word(str_input)





if __name__ == '__main__':

    # offline
    PATH = "C:\\GoogleAutoComplete\\google-project-group-1"
    result = [y for x in os.walk(PATH) for y in glob(os.path.join(x[0], '*.txt'))]
    words_dic = {}

    # for index in range(len(result)):
    for index in range(1):
        file_to_read = open(result[index], "r", encoding="utf-8")
        for line_index, line in enumerate(file_to_read):
            temp_line = line.lower()
            temp_line = re.split('[^a-zA-Z\d]', temp_line)
            temp_line = list(filter(None, temp_line))
            for word_index, word in enumerate(temp_line):
                if word in words_dic:
                    words_dic[word] += [(result[index], line_index, word_index)]
                else:
                    words_dic[word] = [(result[index], line_index, word_index)]
            #print(words_dic["terminal"])
    exDict = {'words_dic':words_dic}

    user_service(import_dictionary_from_json('file.txt'))

# with open('file.txt', 'w') as file:
      #  file.write(json.dumps(exDict))






    # online
#  1. read dictionary
#  2. get input from user
#  3. for every word : find all relevant lines with this word (search it in dictionary)
#  4. cut/ Set between all the relevant lines of all words
#  5. suggest based on the lines that we have

#new_word = re.split('[^a-zA-Z0-9]', word)
#new_word = list(filter(None, new_word))
