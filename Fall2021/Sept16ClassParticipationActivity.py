def Spnsh():
    print("Buenos dias")

def Grmn():
    print("Guten morgen")

def Itln():
    print("Buon giorno")

def main():

    user_lang = ""

    while user_lang != "x":
        user_lang = input("Enter a language and I will say \"Good Morning\" in that language (x to exit): ").lower()
        if user_lang == "german": Grmn()
        elif user_lang == "spanish": Spnsh()
        elif user_lang == "italian": Itln()
        elif user_lang == "x": print("Good Bye!")
        else: print("I couldn't translate "+ user_lang)

if __name__ == "__main__":
    main()
