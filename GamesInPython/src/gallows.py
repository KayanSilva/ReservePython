import random

def play():
    show_initial()
    
    word_secret = load_wordsecret()
    
    list_hit =  ["_" for lette in word_secret]
    hung_up = False
    hit = False
    error = 0

    print(list_hit)
    while(not hung_up and not hit):
        kick = capture_kick()

        if(kick in word_secret):
            right_kick(kick, list_hit, word_secret)
        else:
            error += 1
            draw_gallows(error)

        hung_up = error == 7
        hit =  "_" not in list_hit
        print(list_hit)
    
    if(hit):
        show_winnermessage()
    else:
        show_losermessage(word_secret)
    print("End of the game.")

def show_initial():
    print("****************************")
    print("Welcome to the game Gallows.")
    print("****************************")

def load_wordsecret():
    archive = open("fruts.txt", "r", encoding="UTF-8")
    list_words = []
    for line in archive:
        list_words.append(line.strip())
    archive.close()

    number = random.randrange(0,len(list_words))
    return list_words[number].upper()

def capture_kick():
    kick = input("Choice a word: ")
    return kick.strip().upper()

def right_kick(kick, list_hit, word_secret):
    index = 0
    for letter in word_secret:
        if(kick == letter):
            list_hit[index] = letter
        index += 1

def draw_gallows(error):
    print("  _______     ")
    print(" |/      |    ")

    if(error == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(error == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(error == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(error == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(error == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(error == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (error == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def show_winnermessage():
    print("Congratulations, You win!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def show_losermessage(word_secret):
    print("Ohhh, You were hanged!")
    print("The word was {}".format(word_secret))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if(__name__ == "__main__"):
    play()