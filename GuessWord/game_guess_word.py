#
# DONE BY IVÁN MORENO VALERO
# 1) You are provide with some blank spaces like _ _ _ _ _ _(6 letters)
# so you know how long the word is.
# 2) You make a guess like 'planes' and you receive a puntuation like:
# '2 semi-correct 1 correct' where 'semi-correct' means that the letter is in the
# word but not in that position while 'correct' means it is in the correct
# position
import os
import finding_the_word
import user_manage
########################   GAME LOGIC  ########################
globalWord = finding_the_word.read_from_file_eng(5)
globalTries = 10
language = "english"
globalLength = 5
userName = ""
Total = 0
Wins = 0
Loses = 0

def get_word():
    return globalWord

def get_tries():
    return globalTries

def check_win(word, guess):
    if(word == guess):
        return True
    else:
        return False

def puntuation(word, guess):
    correct = 0
    semiCorrect = 0
    correct_position = []
    semiCorrect_position = []

    for i in range(0, len(guess)):
        if guess[i] == word[i]:
            correct = correct + 1
            correct_position.append(guess[i])
        else:
            for j in range(0, len(word)):
                if word[j] == guess[i]:
                    semiCorrect = semiCorrect + 1
                    semiCorrect_position.append(guess[i])
    semiCorrect_position.sort()
    if language == "english":
        print("You have Correct:", correct, "on letters", correct_position,
              "\tSemi-correct:", semiCorrect,"on letters", semiCorrect_position, "\n")
    if language == "spanish":
        print("Correctas:", correct, "las letras", correct_position,
              "\tSemi-correctas:", semiCorrect,"las letras", semiCorrect_position, "\n")

def is_guess_correct(word, guess):
    wordLetters = len(word)
    guessLetters = len(guess)
    if wordLetters != guessLetters:
        if language == "english":
            print("WARNING: Please introduce,", wordLetters, "letters\n")
        if language == "spanish":
            print("CUIDADO: Por favor introduce,", wordLetters, "letras\n")
        return False
    elif guess.isalpha() != True:
        if language == "english":
            print("WARNING: Your word can not contain white spaces or special characters\n")
        if language == "spanish":
            print("CUIDADO: Tu palabra contiene espacios en blanco o carácteres especiales\n")
        return False
    elif guess.islower() != True:
        if language == "english":
            print("WARNING: Your word have to be in lower case\n")
        if language == "spanish":
            print("CUIDADO: Tu palabra debe estar en minúsculas\n")
        return False
    elif isisogram(guess) == False:
        if language == "english":
            print("WARNING: Your word must be an isogram(not contain repeated characters)")
        if language == "spanish":
            print("CUIDADO: Tu palabra debe ser un isograma(no contener carácteres repetidos)")
        return False
    else:
        return True



def play():
    global globalLength
    os.system('cls')
    head()
    tries = get_tries()
    word = get_word()
    globalLength = len(word)
    guess = " "
    while tries > 0 and check_win(word, guess) == False:
        if language == "english":
            print("The word you are looking for has", globalLength, "letters. You have", tries, "tries left. Write 0 to exit.")
        if language == "spanish":
            print("La palabra que estas buscando tiene", globalLength, "letras. Tienes", tries, "intentos restantes. Escribe 0 para salir.")
        guess = input()
        if guess == "0":
            menu()
        print()
        isGuessCorrect = is_guess_correct(word, guess)
        if isGuessCorrect == True:
            puntuation(word, guess)
            tries = tries - 1
        print("*"*100, "\n")
    if check_win(word, guess) == True:
        if language == "english":
            print("Congratulations, You won!")
        if language == "spanish":
            print("Felicidades, ¡Tú ganas!")
        user_manage.update_user_win(userName)
    else:
        if language == "english":
            print("You are out of tries, sorry. The word was", word)
        if language == "spanish":
            print("No te quedan intentos, lo siento. La palabra era", word)
        user_manage.update_user_lose(userName)
    print("*"*100, "\n")
    user_manage.read_user_data(userName)
    play_again_menu(globalLength)
########################   INSTRUCTIONS  ########################

def instructions():
    os.system('cls')
    head()
    if language == "english":
        print("You are provide with the number of letters certain word has, example: 6 letters"
        " so you know how long the word is.\nYou have a limited amount of tries"
        " to guess the correct word\n"
        "You make a guess like 'planes' and you receive a puntuation like:\n"
        "'2 correct 1 semi-correct'\nWhere 'semi-correct' means that the letter is in the"
        " word but not in that position\nWhile 'correct' means it is in the correct"
        " position\n\n")
    if language == "spanish":
        print("Se te provee con el número de letras de una palabra, por ejemplo: 5 letras"
        " así que sabes la longitud de la palabra.\nTienes un número limitado de intentos"
        " para acertar la palabra\n"
        "Haces un intento como 'avión' y recibes una puntuación:\n"
        "'2 correctas 1 semi-correcta'\nDonde 'semi-correcta' significa que la letra esta en la"
        " palabra pero no en esa posición\nMientras que 'correcta' significa que esta en la"
        "position correcta\n\n")
    mini_menu()

########################  OPTIONS  ########################
def options():
    os.system('cls')
    head()
    choice = options_menu()

    if choice == 1:
        options_menu_1()
        options()
    elif choice == 2:
        options_menu_2()
        options()
    elif choice == 3:
        options_menu_3()
        options()
    else:
        menu()

########################   USERS  ########################

def select_user():
    global userName
    os.system('cls')
    head()
    if language == "english":
        userName = input("Write user name: ")
    if language == "spanish":
        userName = input("Escribe un nombre de usuario: ")
    data_user(userName)
    menu()

def data_user(user):
    global Total
    global Wins
    global Loses
    global language
    list_data = []
    list_data.append(user_manage.read_user_data(user))
    Total = list_data[0][0]
    Wins = list_data[0][1]
    Loses = list_data[0][2]
    language = list_data[0][3]

def delete_user():
    os.system('cls')
    head()
    if language == "english":
        option = int(input("Do you want to delete your user?\n"
                           "1 ==> Delete your user\n"
                           "2 ==> Back to users menu\n"))
    if language == "spanish":
        option = int(input("¿Quieres eliminar tu usuario?\n"
                           "1 ==> Eliminar usuario\n"
                           "2 ==> Volver al menu de usuario\n"))
    if option == 1:
        user_manage.delete_user(userName)
        select_user()
    if option == 2:
        user_menu()

########################   MENUS  ########################
def head():
    global userName
    if userName != "":
        data_user(userName)
    if language == "english":
        print("\nWELCOME TO THE WORDS GAME",userName,"\n\nlanguage:English\ttries:"
              ,globalTries,"\tletters:",len(globalWord),"\n"
              "Total games played:",Total,"\t\tWins:",Wins,"\tLoses",Loses,"\n\n")
    if language == "spanish":
        print("\nBIENVENIDO A ADIVINA LA PALABRA",userName,"\n\nidioma:Español\tintentos:"
              ,globalTries,"\tletras:",len(globalWord),"\n"
              "Total partidas jugadas:",Total,"\tVictorias:",Wins,"\tDerrotas",Loses,"\n\n")
        print("¡Cuidado, en español 'á' y 'a' son letras distintas! ¡Tenlo en cuenta!\n\n")

def menu():
    os.system('cls')
    head()
    if language == "english":
        option = int(input("What do you want to do?. Press the number of the action you want to choose\n"
        "1 ==> Play\n"
        "2 ==> Set Options\n"
        "3 ==> Instructions\n"
        "4 ==> Change User\n"
        "Other ==> Quit\n"))
    if language == "spanish":
        option = int(input("¿Qué quieres hacer?. Pulsa un número dependiendo de la acción que quieras realizar\n"
        "1 ==> Jugar\n"
        "2 ==> Configuración\n"
        "3 ==> Instrucciones\n"
        "4 ==> Cambiar usuario\n"
        "Otro ==> Salir\n"))
    if option == 1:
        play()
    elif option == 2:
        options()
    elif option == 3:
        instructions()
    elif option == 4:
        user_menu()

def user_menu():
    os.system('cls')
    head()
    if language == "english":
        option = int(input("What do you want to do with the users?\n"
                           "1 ==> Select user\n"
                           "2 ==> Delete user\n"
                           "3 ==> Back to main menu\n"))
    if language == "spanish":
        option = int(input("¿Qué quieres hacer con los usuarios?\n"
                           "1 ==> Seleccionar usuario\n"
                           "2 ==> Eliminar usuario\n"
                           "3 ==> Volver al menu principal\n"))
    if option == 1:
        select_user()
    if option == 2:
        delete_user()
    if option == 3:
        menu()

def options_menu():
    os.system('cls')
    head()
    if language == "english":
        opt = int(input("What do you want to do?. Press the number of the action you want to choose\n"
                        "1 ==> Set language\n"
                        "2 ==> Set letters\n"
                        "3 ==> Set tries\n"
                        "4 ==> Back to main menu\n"))
    if language == "spanish":
        opt = int(input("¿Qué quieres hacer?. Pulsa un número dependiendo de la acción que quieras realizar\n"
                        "1 ==> Seleccionar idioma\n"
                        "2 ==> Seleccionar letras\n"
                        "3 ==> Seleccionas intentos\n"
                        "4 ==> Volver al menú principal\n"))
    return opt

def options_menu_1():
    global language
    global globalWord
    os.system('cls')
    head()
    if language == "english":
        chosenLanguage = int(input("What language do you want?. Not selecting language will let you"
                                   " with the current one\n"
                                   "1 ==> English\n"
                                   "2 ==> Spanish\n"))
    if language == "spanish":
        chosenLanguage = int(input("¿Qué idioma prefieres?. Si no seleccionas ninguno, seguirá"
                                   " el actual\n"
                                   "1 ==> Inglés\n"
                                   "2 ==> Español\n"))
    if chosenLanguage == 1:
        language = "english"
        globalWord = finding_the_word.read_from_file_eng(globalLength)
        user_manage.update_language(userName, "english")
    elif chosenLanguage == 2:
        language = "spanish"
        globalWord = finding_the_word.read_from_file_spa(globalLength)
        user_manage.update_language(userName, "spanish")
def options_menu_2():
    global globalWord
    global globalTries
    os.system('cls')
    head()
    if language == "english":
        letters = int(input("How many letters do you want it to have?\n"))
    if language == "spanish":
        letters = int(input("¿Cuántas letras quieres que tenga?\n"))
    if language == "english":
        globalWord = finding_the_word.read_from_file_eng(letters)
    if language == "spanish":
        globalWord = finding_the_word.read_from_file_spa(letters)
    globalTries = int((letters) * 2)

def options_menu_3():
    global globalTries
    os.system('cls')
    head()
    if language == "english":
        print("How many tries do you want?. Less tries, more difficult\n"
              "CARE: Currently you have",globalTries,"tries, if you use less than",globalTries,"tries, the game will become really challenging\n")
    if language == "spanish":
        print("¿Cuántos intentos quieres?. Menos intentos, más difícil\n"
              "Cuidado: Ahora dispones de",globalTries,"intentos, si usas menos de",globalTries,"intentos, el juego se volverá muy difíci\n")
    tries = int(input())
    globalTries = tries

def mini_menu():
    if language == "english":
        opt = int(input("1 ==> Back to main menu\nOther ==> Quit\n"))
    if language == "spanish":
        opt = int(input("1 ==> Volver al menú principal\nOtro ==> Salir\n"))
    if(opt == 1):
        menu()

def play_again_menu(letters_new_word):
    global globalWord
    if language == "english":
        print("Do you want to play again?")
        opt = int(input("1 ==> Play again\n"
                        "2 ==> Back to Main Menu\n"
                        "Other ==> Quit\n"))
    if language == "spanish":
        print("Quieres volver a jugar?")
        opt = int(input("1 ==> Jugar de nuevo\n"
                        "2 ==> Volver al menú principal\n"
                        "Otro ==> Salir\n"))
    if opt == 1:
        if language == "english":
            globalWord = finding_the_word.read_from_file_eng(letters_new_word)
        if language == "spanish":
            globalWord = finding_the_word.read_from_file_esp(letters_new_word)
        play()
    elif opt == 2:
        menu()
########################   OTHERS METHODS  ########################
def isisogram(word):
    for w in range(0, len(word)):
        if word.count(word[w]) != 1:
            return False
    return True
########################   MAIN  ########################
select_user()
