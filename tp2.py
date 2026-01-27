#  Hamza Aqel
#  Programme web pour jouer au jeu « Cueillette de sous »

#  Hypothèses: on considère que le joueur clique une seule fois sur
#  la même case. On considère que le joueur arrête de cliquer aprés
#  l'affichage du message "Vous avez gagné" ou "Vous avez perdu". 

import math
import random
import time

def table(content):
  # Ajoute du contenu dans une balise <table></table>

  return "<table>"+content+"</table>"

def div(content):
  # Ajoute du contenu dans une balise <div></div>

  return "<div>"+content+"</div>"

def tr(content):
  # Ajoute du contenu dans une balise <tr></tr>

  return "<tr>"+content+"</tr>"

def td(content):
  # Ajoute du contenu dans une balise <td></td>

  return "<td>"+content+"</td>"

def element(id):
  # Selectionne l'element id dans le html

  return document.querySelector('#'+id)

def case(index):
  # Selectionne la case(index)

  return element('case'+str(index))

def image(index):
  # Selectionne la image(index)

  return element('image'+str(index))

def clic(index):
  # Permet d'afficher le contenu d'une casse selectionnée contenant une piece, incrémente
  # cmpSous de 1 à chaque clic

  global listAlea, cmpSous, cmpErreur 
  cmpSous += 1

  img = image(index)
  img.removeAttribute("hidden")

  etatJeu()


def etatJeu():
  # Permet de determiner si le joueur a gagné ou si il a perdu

  global listAlea, cmpSous, cmpErreur 

  erreurVal = document.querySelector('#sousCaches')
  erreurVal.innerHTML = 'Nombre de sous cachés:  ' + str(len(listAlea) - cmpSous)

  if len(listAlea) == cmpSous and cmpErreur<3: # Conditions partie gagnée
    message = document.querySelector('#msg')
    message.innerHTML = 'Vous avez gagné!'
    # redemarrer le jeu après 10s:
    time.sleep(10)
    init()

  elif len(listAlea)>cmpSous and cmpErreur>2: # Conditions partie perdue
    message = document.querySelector('#msg')
    message.innerHTML = 'Vous avez perdu!'
    # redemarrer le jeu après 10s:
    time.sleep(10)
    init()

  else:
    message = document.querySelector('#msg')
    message.innerHTML = 'Jouer!'

def compterErreurs():
  # Permet de compter le nombre d'erreurs et de l'afficher dans le html

  global cmpErreur
  cmpErreur += 1

  erreurVal = document.querySelector('#affichErreur')
  erreurVal.innerHTML = 'Erreurs:  ' + str(cmpErreur)

  etatJeu()

def is_adjacent(index, indexAlea):
  # Permet de determiner si une piece à indice (index) peut etre ajoutée à la liste (indexAlea), en s'assurant 
  # qu'il n'y a pas de pieces dans les cases voisines

  for k in indexAlea:
      if abs(index-k)==1 or abs(index-k)==10 or abs(index-k)==9 or abs(index-k)==11 or abs(index-k)==0:
        return True
  return False

def listIndexAlea():
  # Retourne une liste d'indices aléatoires entre 0 et 99, le nombre d'indices est entre 15 et 20
  
  nombrePiecesCaches = math.floor(random.random()*5)+15 # Nombre pieces cachées
  indexAlea = []

  while len(indexAlea) != nombrePiecesCaches:
    indexA = math.floor(random.random()*100) # Position aléatoire d'une pièce entre 0 et 99
    if not is_adjacent(indexA, indexAlea): # Si il n'y a pas de pièces dans les cases adjacentes
        indexAlea.append(indexA)
  return indexAlea

def valeurCases(listIndex):
  # Permet de calculer la valeur numérique dans les cases de la grille, la valeur indique le nombre de pièces 
  # se trouvant dans les cases voisines (pour un maximum de huit), qu’elles se touchent par un côté ou par un coin.
  # Le résultat est retourné sous forme d'une liste
  listValeur = []

  for i in range(100):
    temp = 0 # valeur numérique case

    if i not in listIndex:  # Vérifier si la case actuelle (i) ne contient pas de pièce

      if i%10 != 0 and i%10 != 9 and i>9 and i<90: # au milieu
        # Vérifier les cases voisines et incrémenter temp si une pièce est présente
        if (i + 1) in listIndex:
            temp += 1
        if (i - 1) in listIndex:
            temp += 1
        if (i + 10) in listIndex:
            temp += 1
        if (i - 10) in listIndex:
            temp += 1
        if (i + 9) in listIndex:
            temp += 1
        if (i - 9) in listIndex:
            temp += 1
        if (i + 11) in listIndex:
            temp += 1
        if (i - 11) in listIndex:
            temp += 1

      elif i < 9 and i > 0: # premiere ligne entre 1 et 8
        # Vérifier les cases voisines et incrémenter temp si une pièce est présente
        if (i + 1) in listIndex:
            temp += 1
        if (i - 1) in listIndex:
            temp += 1
        if (i + 10) in listIndex:
          temp += 1
        if (i + 9) in listIndex:
            temp += 1
        if (i + 11) in listIndex:
            temp += 1

      elif i > 90 and i < 99: # 10eme ligne entre 90 et 98
        # Vérifier les cases voisines et incrémenter temp si une pièce est présente
        if (i + 1) in listIndex:
            temp += 1
        if (i - 1) in listIndex:
            temp += 1
        if (i - 10) in listIndex:
          temp += 1
        if (i - 9) in listIndex:
            temp += 1
        if (i - 11) in listIndex:
            temp += 1

      elif i%10 == 0 and i > 9 and i < 90: # premiere colonne entre 10 et 80
        # Vérifier les cases voisines et incrémenter temp si une pièce est présente
        if (i + 1) in listIndex:
            temp += 1
        if (i + 10) in listIndex:
            temp += 1
        if (i - 10) in listIndex:
          temp += 1
        if (i - 9) in listIndex:
            temp += 1
        if (i + 11) in listIndex:
            temp += 1

      elif i%10 == 9 and i > 9 and i < 90: # 10eme colonne entre 19 et 89
        # Vérifier les cases voisines et incrémenter temp si une pièce est présente
        if (i - 1) in listIndex:
            temp += 1
        if (i + 10) in listIndex:
            temp += 1
        if (i - 10) in listIndex:
          temp += 1
        if (i + 9) in listIndex:
            temp += 1
        if (i - 11) in listIndex:
            temp += 1

      elif i == 0: # case 0
        # Vérifier les cases voisines et incrémenter temp si une pièce est présente
        if (i + 1) in listIndex:
            temp += 1
        if (i + 10) in listIndex:
            temp += 1
        if (i + 11) in listIndex:
            temp += 1
      
      elif i == 9: # case 9
        # Vérifier les cases voisines et incrémenter temp si une pièce est présente
        if (i - 1) in listIndex:
            temp += 1
        if (i + 10) in listIndex:
            temp += 1
        if (i + 9) in listIndex:
            temp += 1
      
      elif i == 90: # case 90
        # Vérifier les cases voisines et incrémenter temp si une pièce est présente
        if (i + 1) in listIndex:
            temp += 1
        if (i - 10) in listIndex:
            temp += 1
        if (i - 9) in listIndex:
            temp += 1
      
      elif i == 99: # case 99
        # Vérifier les cases voisines et incrémenter temp si une pièce est présente
        if (i - 1) in listIndex:
            temp += 1
        if (i - 10) in listIndex:
            temp += 1
        if (i - 11) in listIndex:
            temp += 1


    listValeur.append(temp)

  return listValeur


def genererGrille():
  # Fonction principale permettant la création de la grille, et l'affichage des options

  global cmpErreur, listAlea, cmpSous 
  returnValue=""
  listAlea = listIndexAlea() # liste postions pieces dans la grille
  listValeurs = valeurCases(listAlea) # liste valeurs numériques des cases adjacentes aux pieces

  for i in range(0,10):
    temp=""
    for j in range(0,10):
      index = i*10+j

      if index in listAlea: # Case qui doit contenir une pièce
        temp += "<td class=piecesCaches id=case"+str(index)+" onclick= clic("+str(index)+")><img id=image"+str(index)+" src=symboles/coste.svg alt=Piece hidden=hidden></td>"
      
      else:
        if listValeurs[index] == 0: # Case vide car aucune piece n'est adjacente
          temp += "<td class=casesVide id=case"+str(index)+" onclick= compterErreurs()>""</td>"
        
        else: # Case où on affiche la valeur numérique
          temp += "<td id=case"+str(index)+">"+str(listValeurs[index])+"</td>"

    returnValue += tr(temp)

  Grille = table(returnValue)

  bouton1 = "<div class= blocBouton><button id=boutonNP onclick=init()>Nouvelle partie</bouton></div>"

  msg="<div class= blocMessage><p id=msg>Jouer!</p></div>"

  valeurErreurs ="<p id=affichErreur>Erreurs: 0</p>"

  NombreSous="<p id=sousCaches>Nombre de sous cachés:  "+str(len(listAlea))+"</p>"

  Sortie= "<div class= centered>"+str(bouton1 + msg + div(valeurErreurs) + div(NombreSous) + div(Grille))+"</div>"

  return Sortie

def init():
  # Variables globales: cmpErreur: compteur d'erreurs, listAlea: liste de postions des
  #  pieces dans la grille, cmpSous: compteur de sous trouvés

    global cmpErreur, listAlea, cmpSous 
    listAlea = []
    cmpErreur = 0
    cmpSous = 0

    main = document.querySelector("#main")
    main.innerHTML = genererGrille()
    
