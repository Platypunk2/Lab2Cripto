import string
import random as ran
def GenNombre():
    nom = ""
    for i in range(5):
        nom = nom + str(ran.randint(0,99))
    return nom

def GenPassword():
    password=""
    for i in range(5):
        password = password + str(ran.randint(0,99))
    return password


def GenNombreES():
    nom = ""
    for i in range(5):
        nom = nom + ran.choice(string.ascii_letters)
    return nom
