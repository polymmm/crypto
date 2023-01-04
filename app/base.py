alphabet_cyrillic = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 
                'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я' ]

alphabet_latin = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
                'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','+','*','!']

language='RU'

def detect_language(word):
    temp=0
    global language
    for letter in word:
        if (letter in alphabet_cyrillic): temp+=1
    if (temp==len(word)): language='RU'
    elif (temp==0): language='EN'
    else: print('Вы ввели слово некорректно'); exit()

        
def word_indexes(word):
    word_indexes=[]
    for letter in word:
        if (language=='RU'):
            word_indexes.append(alphabet_cyrillic.index(letter))
        else:
            word_indexes.append(alphabet_latin.index(letter))
    return word_indexes


def word_by_indexes(list_of_indexes):
    word_letters=[]
    if (language=='RU'):
        for index in list_of_indexes:
            word_letters.append(alphabet_cyrillic[index])
    else:
        for index in list_of_indexes:
            word_letters.append(alphabet_latin[index])
    return word_letters


clear_text = 'рибосома'

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

dict = {'.': 'тчк', ',': 'зпт'}


def replace_all_to(input_text, dict):
    input_text = input_text.replace(' ', '')
    for i, j in dict.items():
        input_text = input_text.replace(i, j)
    return input_text


def replace_all_from(input_text, dict):
    for i, j in dict.items():
        input_text = input_text.replace(j, i)
    return input_text


def file_to_string(name):
    with open(name) as f:
        input_short_text = " ".join([l.rstrip() for l in f]) + ' '
    return input_short_text.lower()


def input_for_cipher_short():
    return replace_all_to(file_to_string('short.txt'), dict)


def input_for_cipher_long():
    return replace_all_to(file_to_string('long.txt'), dict)


def output_from_decrypted(decrypted_text):
    return replace_all_from(decrypted_text, dict)


alphabet_cyrillic = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 
                'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я' ]

alphabet_latin = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
                'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','+','*','!']

language='RU'

def detect_language(word):
    temp=0
    global language
    for letter in word:
        if (letter in alphabet_cyrillic): temp+=1
    if (temp==len(word)): language='RU'
    elif (temp==0): language='EN'
    else: print('Вы ввели слово некорректно'); exit()



        
def word_indexes(word):
    word_indexes=[]
    for letter in word:
        if (language=='RU'):
            word_indexes.append(alphabet_cyrillic.index(letter))
        else:
            word_indexes.append(alphabet_latin.index(letter))
    return word_indexes


def word_by_indexes(list_of_indexes):
    word_letters=[]
    if (language=='RU'):
        for index in list_of_indexes:
            word_letters.append(alphabet_cyrillic[index])
    else:
        for index in list_of_indexes:
            word_letters.append(alphabet_latin[index])
    return word_letters