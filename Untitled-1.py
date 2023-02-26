def utilisation():
    print("1-Nouveau lien: ")
    print("2-Afficher tous les liens")
    choix = int(input("Choisir: "))
    if choix == 1:
        new()
    elif choix == 2:
        lire()
    else:
        print("Il faut soit 1 ou 2")


def new():
    print("Votre lien: ")
    ajout = input()
    f = open("lien.txt", "a")
    f.write("Votre lien: "+ajout)
    f.close()


def lire():
    f = open("lien.txt", "r")
    print(f.read())
    f.close()


f = open("lien.txt", "a")
f.close()

utilisation()