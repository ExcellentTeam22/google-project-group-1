import json


def import_dictionary_from_json(path: str) -> dict:
    return json.load(open(path))['words_dict']


def search_word(str_input: str, dict_of_word: dict):
    input_words = str_input.split()
    if any(key in dict_of_word for key in input_words):
        for i in range(len(input_words) - 1):
            first_group = [dict_of_word[input_words[i].lower()]]
         #   second_group = [[t[1], t[2]] for t in dict_of_word[input_words[i + 1].lower()]]
            print(first_group)
          #  print(second_group)
           # save_location = [f for f in first_group for s in second_group if (s[0] == f[0] and s[1] - f[1] == 1)]
           # print(save_location)


def user_service(words: dict):
    str_input = input("The system is ready. Enter your text: ")
    search_word(str_input, words)


def get_location_intersection(first_list: list, second_list: list) -> list:
    """
    This function finds all the subsequent words.
    :param first_list: This is a list of columns of the locations of all the matching words to the first word entered.
    :param first_list: This is a list of columns of the locations of all the matching words to the second word entered.
    :return: a list of all the next word's column.
    """
    first_list_index = 0
    second_list_index = 0
    result_list = []
    while first_list_index < len(first_list) or second_list_index < len(second_list):
        # If the first word appears before the second word.
        if first_list[first_list_index] < second_list[second_list_index]:
            # If the second word appears right after the first word.
            if second_list[second_list_index] - first_list[first_list_index] == 1:
                result_list.append(second_list[second_list_index])
                second_list_index += 1
            first_list_index += 1
        else:
            second_list_index += 1

    return result_list


if __name__ == '__main__':
    import_dictionary_from_json('file.txt')
