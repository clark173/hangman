import sys

def get_words():
    dictionary = []

    f = open('/usr/share/dict/words', 'r')
    for line in f:
        if len(dictionary) > 1:
            if dictionary[-1] == line.strip().lower():
                continue
            else:
                dictionary.append(line.strip().lower())
        else:
            dictionary.append(line.strip().lower())
    return dictionary

def get_length():
    return input('Enter the number of characters: ')

def print_char(char):
    print "Try the letter '%s'" % char

def check_input():
    while True:
        try:
            correct = raw_input('Was the letter correct? [y/n]: ')
            if correct.lower() == 'y':
                return True
            elif correct.lower() == 'n':
                return False
        except KeyboardInterrupt:
            print 'Exiting script...'
            sys.exit(0)

def update_length(dictionary, length):
    new_dictionary = []

    for word in dictionary:
        if len(word) == length:
            new_dictionary.append(word)
    return new_dictionary

def update_dictionary(dictionary, used_letters, incorrect_letters):
    new_dictionary = []

    for word in dictionary:
        skip_word = False
        for letter in incorrect_letters:
            if letter in word:
                skip_word = True
                break
        if skip_word:
            continue
        for letter in used_letters:
            if letter not in word:
                skip_word = True
                break
        if not skip_word:
            new_dictionary.append(word)

    return new_dictionary

def analyze_character(dictionary, used_letters, incorrect_letters):
    char = ''
    num = 0
    letters = {}

    for word in dictionary:
        for letter in word:
            if letter.lower() not in used_letters and\
                letter.lower() not in incorrect_letters:
                if letter.lower() in letters:
                    letters[letter.lower()] += 1
                else:
                    letters[letter.lower()] = 1

    for letter, value in letters.items():
        if value > num:
            char = letter
            num = value
    return char

def main():
    used_letters = []
    unused_letters = []

    dictionary = get_words()
    length = get_length()
    dictionary = update_length(dictionary, length)
    char = analyze_character(dictionary, used_letters, unused_letters)
    while True:
        print_char(char)
        correct = check_input()
        if correct:
            used_letters.append(char)
        else:
            unused_letters.append(char)
        dictionary = update_dictionary(dictionary, used_letters, unused_letters)
        char = analyze_character(dictionary, used_letters, unused_letters)
        if char == '':
            print 'Solved!'
            break
        print dictionary

if __name__ == "__main__":
    main()
