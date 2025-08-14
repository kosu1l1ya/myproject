from random import choice
list_words = ['год', 'человек', 'время', 'дело', 'жизнь', 'день']


def get_word():
    word = choice(list_words)
    word = word.upper()
    return word


def display_hangman(tries):
    man = [
        '''
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     / \\
        -
        ''',
        '''
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     / 
        -        
        ''',
        '''
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |
        -
        ''',
        '''
        --------
        |      |
        |      O
        |     \\|
        |      |
        |
        -
        ''',
        '''
        --------
        |      |
        |      O
        |      |
        |      |
        |
        -
        ''',
        '''
        --------
        |      |
        |      O
        |
        |
        |
        -
        ''',
        '''
        --------
        |      |
        |
        |
        |
        |
        -
        ''']
    return man[tries]


def play():
    word = get_word()
    # строка, содержащая символы _ на каждую букву задуманного слова
    word_completion = '_' * len(word)
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    s = ''

    print('Давайте играть в угадайку слов!')

    while tries >= 0:
        print(display_hangman(tries))
        if tries == 0:
            return 'Вы проиграли, было загадано слово', word

        print(word_completion)

        lett_word = input(
            'Хотите ввести букву или слово целиком? (б - буква, с - слово) ')

        while lett_word not in ['б', 'с']:
            lett_word = input('Введите "б" или "с"')

        if lett_word == 'б':
            letter = input('Введите букву: ').upper()
            while len(letter) != 1 or not letter.isalpha() or letter in guessed_letters:
                letter = input(
                    'Введите одну букву, которой ещё не было: ').upper()
            guessed_letters.append(letter)

            if letter in word:
                s1 = list(word_completion)
                for i in range(len(word)):
                    if word[i] == letter:
                        s1[i] = letter
                word_completion = ''.join(s1)
                if '_' not in word_completion:
                    return 'Поздравляем, вы угадали слово! Вы победили!'
            else:
                print('Этой буквы нет в слове')
                tries -= 1
        else:
            word1 = input('Введите слово: ').upper()
            if word1 == word:
                return 'Поздравляем, вы угадали слово! Вы победили!'
            else:
                tries -= 1


play()
