import os
import re
import json
from glob import glob


# משימה ראשונה:
# מילון ראשון - מפתח של מילים
# מילון שני - מפתח של כתובות של קבצים
# מילון שלישי - מפתח של שורות
# בתוך המילון השלישי רשימה של מיקומים

# משימה ראשונה המשך:
# לממש פונקצית חיתוך בין שני מערכים ממויינים

# משימה שנייה:
# לחלק לשני קבצים offline online

# משימה שלישית:
# להתאים את הפונקציה של חיפוש מילה

# משימה רביעית:
# לתקן את הpath של מיקום הקבצים

# ביצוע טסטים שהחיפוש עובד עבור קלטים תקינים

# משימה חמישית:
# להתחיל לטפל במקרה של קלט לא תקין מסוים


def adjust_line(current_line: str) -> list:
    """
    This function converts the entire sentence to lowercase and removes all the characters that are not alphanumeric.
    :param current_line: The line we are now converting.
    :return: The given line but when it contains only lowercase alphanumeric words.
    """
    correct_line = current_line.lower()
    correct_line = re.split(r'[^\w\d]', correct_line)
    correct_line = list(filter(None, correct_line))
    return correct_line


def create_words_dictionary() -> dict:
    """
    This function creates the dictionary of words that we will use for the autocomplete.
    :return: The dictionary of words from all the given files.
    """
    path = "C:\\GoogleAutoComplete\\google-project-group-1"
    path_list = [y for x in os.walk(path) for y in glob(os.path.join(x[0], '*.txt'))]
    words_dict = {}

    # For each file we add all the words and their locations.
    # for index in range(len(path_list)):
    for path_index in range(2):
        file_to_read = open(path_list[path_index], 'r', encoding='utf-8')
        for line_index, line in enumerate(file_to_read):
            for word_index, word in enumerate(adjust_line(line)):
                # The given word is already a key of a certain value in the dictionary of words.
                if word not in words_dict:
                    words_dict[word] = {path_list[path_index]: {line_index: [word_index]}}

                elif path_list[path_index] not in words_dict[word]:
                    words_dict[word][path_list[path_index]] = {line_index: [word_index]}

                elif line_index not in words_dict[word][path_list[path_index]]:
                    words_dict[word][path_list[path_index]][line_index] = [word_index]

                else:
                    words_dict[word][path_list[path_index]][line_index] += [word_index]

    return words_dict


if __name__ == '__main__':
    # offline
    words_dictionary = create_words_dictionary()
    exDict = {'words_dict': words_dictionary}
    with open('file.txt', 'w') as file:
        file.write(json.dumps(exDict))


# online
#  1. read dictionary
#  2. get input from user
#  3. for every word : find all relevant lines with this word (search it in dictionary)
#  4. cut/ Set between all the relevant lines of all words
#  5. suggest based on the lines that we have
