import os
from glob import glob
import re
import json


def import_dictionary_from_json(path: str) -> dict:
    with open('file.txt') as json_file:
        data = json.load(json_file)['words_dic']
    return data


def search_word(str_input:str,dict_of_word:dict):
    input_words = str_input.split()
    if any(key in dict_of_word for key in input_words):
        for i in range(len(input_words)-1):
            first_group = [[t[1], t[2]] for t in dict_of_word[input_words[i].lower()]]
            second_group = [[t[1], t[2]] for t in dict_of_word[input_words[i+1].lower()]]
            print(first_group)
            print(second_group)
            save_location=[f for f in first_group for s in second_group if (s[0]==f[0] and s[1]-f[1]==1)]
            print(save_location)


def user_service(words:dict):
    str_input = input("The system is ready. Enter your text")
    search_word(str_input,words)


def correct_text(current_line: str) -> list:
    """
    This function converts the entire sentence to lowercase and removes all the characters that are not alphanumeric.
    :param current_line: The line we are now converting.
    :return: The given line but when it contains only lowercase alphanumeric words.
    """
    correct_line = current_line.lower()
    correct_line = re.split('[^a-z\d]', correct_line)
    correct_line = list(filter(None, correct_line))
    return correct_line


def create_words_dictionary() -> dict:
    """
    This function creates the dictionary of words that we will use for the autocomplete.
    :return: The dictionary of words from all the given files.
    """
    path = "C:\\GoogleAutoComplete\\google-project-group-1"
    result = [y for x in os.walk(path) for y in glob(os.path.join(x[0], '*.txt'))]
    words_dic = {}

    # For each file we add all the words and their locations.
    # for index in range(len(result)):
    for index in range(1):
        file_to_read = open(result[index], "r", encoding="utf-8")
        for line_index, line in enumerate(file_to_read):
            temp_line = correct_text(line)
            for word_index, word in enumerate(temp_line):
                print(word)
                # The given word is already a key of a certain value in the dictionary of words.
                if word in words_dic:
                    words_dic[word] += [(result[index], line_index, word_index)]
                # The given word is not a key of a certain value in the dictionary of words.
                else:
                    words_dic[word] = [(result[index], line_index, word_index)]

    return words_dic


if __name__ == '__main__':

    # offline
    words_dictionary = create_words_dictionary()
    exDict = {'words_dic': words_dictionary}
    with open('file.txt', 'w') as file:
        file.write(json.dumps(exDict))

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
