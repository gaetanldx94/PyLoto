import random
import os 

rnd = random.Random()
bcl = True
Alphabet = [
  "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
  "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
]

Number_ = [
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9
] 

KeyFrame = [
  Alphabet[rnd.randint(0, 25)],
  Number_[rnd.randint(0, 9)],

  Alphabet[rnd.randint(0, 25)],
  Number_[rnd.randint(0, 9)],

  Alphabet[rnd.randint(0, 25)],
  Number_[rnd.randint(0, 9)], 

  Alphabet[rnd.randint(0, 25)],
  Number_[rnd.randint(0, 9)],

  Alphabet[rnd.randint(0, 25)],
  Number_[rnd.randint(0, 9)],

  Alphabet[rnd.randint(0, 25)],
  Number_[rnd.randint(0, 9)]
]

IaKey = str(KeyFrame[rnd.randint(0, 5)]) + str(KeyFrame[rnd.randint(0, 5)]) + str(KeyFrame[rnd.randint(0, 5)]) + str(KeyFrame[rnd.randint(0, 5)]) + str(KeyFrame[rnd.randint(0, 5)]) + str(KeyFrame[rnd.randint(0, 5)])

"""print(IaKey)"""

print("""
    Règles : 

    La clé du loto et composé uniquement de 
    lettre minuscule et de nombre de 0 a 9
    aucune Majuscule n'est pris en compte
""")
UserKey = input("Code du loto : ")
if UserKey == IaKey:
  print("\nBravo vous avez trouvé la clé : {}".format(IaKey))
elif UserKey != IaKey:
  print("\nDommage la clé du loto était : {}".format(IaKey))

pause = input("Appuyer sur une touche pour quitter...")