from pip._vendor.distlib.compat import raw_input


# print the welcome message
def print_welcome():
    print("""
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_  \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/
                        """)


# hangman photos
def hangman_photo(bad_guesse_num):
    photos = ["""   x-------x""", """
        x-------x
        |
        |
        |
        |
        |
    """, """
        x-------x
        |       |
        |       0
        |
        |
        |
    """, """
        x-------x
        |       |
        |       0
        |       |
        |
        |
    """, """
        x-------x
        |       |
        |       0
        |      /|\\
        |
        |
    """, """
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |
    """, """
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |
    """]
    return photos[bad_guesse_num]


# check win
def check_win(secret_word, old_letters_guessed):
    count = 0
    for i in secret_word:
        if i in old_letters_guessed:
            count += 1
    if count == len(secret_word):
        return True
    return False


# return the secret word with '_' and guessed letters
def show_hidden_word(secret_word, old_letters_guessed):
    word = ""
    place = 0
    for i in secret_word:
        if i in old_letters_guessed:
            word += i
        else:
            word += "_"
    return word


# check if letter is valid
def check_valid_input(letter_guessed, old_letters_guessed, secret_word):
    if not letter_guessed.isalpha():
        return False
    if letter_guessed in show_hidden_word(secret_word, old_letters_guessed):
        return False
    if letter_guessed in old_letters_guessed:
        return False
    return True


# add letter to guessed letters
def try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word):
    if check_valid_input(letter_guessed, old_letters_guessed, secret_word):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X")
        print(*old_letters_guessed, sep=' -> ')
        return False


# open file by path and choose word in file by index
# return the secret word
def choose_word(file_path, index):
    f = open(file=file_path)
    lines = f.readlines()
    return lines[index]


def main():
    print_welcome()

    # get file and index C:\Users\royko\Downloads\words.txt
    file_path = raw_input("Enter file path:")
    index = raw_input("Enter index:")

    # start
    MAX_TRIES = 6
    num_of_tries = 0
    secret_word = choose_word(file_path, int(index)).replace('\n', '')
    old_letters_guessed = []

    print(hangman_photo(0))

    while num_of_tries < MAX_TRIES:
        print(show_hidden_word(secret_word, old_letters_guessed))
        letter = raw_input("Guess a letter:")

        if try_update_letter_guessed(letter, old_letters_guessed, secret_word):
            if not letter in secret_word:
                print(":(")
                num_of_tries += 1
                print(hangman_photo(num_of_tries))

            if check_win(secret_word, old_letters_guessed):
                print("u won, good job")
                exit(0)
    print("u lost, u stupid")


if __name__ == "__main__":
    main()
