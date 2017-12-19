import json
import csv
from random import randint

#################################### ENGLISH TREATMENT ####################################
def creating_words_len_eng():
    file_json = open("raw_files/words_dictionary.json", "r", encoding="utf-8")
    words = json.load(file_json)
    file_json.close()
    for i in words:
        words[i] = len(i)
    file_words = open("words_len_eng/words_len.json", "w", encoding="utf-8")
    json.dump(words, file_words,ensure_ascii=False)
    file_words.close()

def creating_words_len_X_eng():
    file_words = open("words_len_eng/words_len.json", "r", encoding="utf-8")
    words = json.load(file_words)
    file_words.close()
    for i in words:
        value = words[i]
        with open("words_len_eng/words_len_" + str(value), "a") as words_file:
            words_file.write(i + ";")

def creating_words_isogram_len_X_eng():
    file_words = open("words_len_eng/words_len.json", "r", encoding="utf-8")
    words = json.load(file_words)
    flag = False
    objects_to_remove = []
    list_words = []
    file_words.close()
    for i in words:
        flag = False
        value = words[i]
        list_words.append(i)
        for j in range(0, len(i)):
            if i.count(i[j]) != 1 and flag == False:
                objects_to_remove.append(i)
                flag = True
        if i.isalpha() == False and flag == False:
            objects_to_remove.append(i)
            flag == True
        if i.islower() == False and flag == False:
            objects_to_remove.append(i)
            flag = True
    final_list = [x for x in list_words if x not in objects_to_remove]
    for i in final_list:
        length = len(i)
        word_format = i + ";"
        with open("words_len_eng/words_len_" + str(length), "a", encoding="utf-8") as words_file:
            words_file.write(word_format)

def read_from_file_eng(n):
    file_words = open("words_len_eng/words_len_" + str(n), "r", encoding="utf-8")
    words = csv.reader(file_words, delimiter=';')
    for word in words:
        set_words = word
    set_words.remove(set_words[-1])
    file_words.close()
    word_selected = randint(0, len(set_words))
    return set_words[word_selected]

#################################### SPANISH TREATMENT ####################################
def creating_words_spa_csv():
    file_words = open("raw_files/spanish_dictionary.txt", "r", encoding="utf-8")
    words = file_words.read().replace('\n', ',')
    print(words)
    file_words.close()
    file_words = open("raw_files/spanish_dictionary.csv", "w", encoding="utf-8")
    file_words.write(words)
    file_words.close

def creating_words_isogram_len_X_spa():
    with open("raw_files/spanish_dictionary.csv", "r", encoding="utf-8") as words_file:
        words = csv.reader(words_file, delimiter=',')
        flag = False
        set_words = []
        objects_to_remove = []
        for word in words:
            set_words = word
        set_words.remove(set_words[-1])
        for i in range(0, len(set_words)):
            flag = False
            for j in range(0, len(set_words[i])):
                if set_words[i].count(set_words[i][j]) != 1 and flag == False:
                    objects_to_remove.append(set_words[i])
                    flag = True
            if set_words[i].isalpha() == False and flag == False:
                objects_to_remove.append(set_words[i])
                flag = True
            if set_words[i].islower() == False and flag == False:
                objects_to_remove.append(set_words[i])
                flag = True
        final_list = [x for x in set_words if x not in objects_to_remove]
    for i in final_list:
        length = len(i)
        word_format = i + ";"
        with open("words_len_spa/words_len_" + str(length), "a", encoding="utf-8") as words_file:
            words_file.write(word_format)

def read_from_file_spa(n):
    file_words = open("words_len_spa/words_len_" + str(n), "r", encoding="utf-8")
    words = csv.reader(file_words, delimiter=';')
    for word in words:
        set_words = word
    set_words.remove(set_words[-1])
    file_words.close()
    word_selected = randint(0, len(set_words))
    return set_words[word_selected]

####################################################################################################
