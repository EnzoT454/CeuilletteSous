# Cueillette de sous — Jeu web en Python

Projet web interactif implémentant le jeu **« Cueillette de sous »**, inspiré du principe du démineur.  
Le joueur clique sur une grille 10×10 afin de découvrir des pièces cachées, tout en évitant de faire trop d’erreurs.

Ce programme est écrit en **Python exécuté côté client** (environnement type Brython / Pyodide), avec génération dynamique du HTML et stylisation via CSS.

---

## Fonctionnalités

- Génération aléatoire d’une **grille 10×10**
- Placement de **15 à 20 pièces cachées**, sans pièces adjacentes
- Calcul automatique des **valeurs numériques** indiquant le nombre de pièces voisines
- Gestion des **clics utilisateur**
- Comptage :
  - des pièces trouvées
  - des erreurs (maximum 3)
- Conditions de **victoire / défaite**
- Redémarrage automatique de la partie après la fin du jeu
- Interface web dynamique (HTML généré en Python)

---

## Règles du jeu

- Le joueur clique sur des cases de la grille :
  - 🪙 **Pièce** : la pièce est révélée
  - ❌ **Case vide** : compte comme une erreur
- Le joueur :
  - **gagne** s’il trouve toutes les pièces avec moins de 3 erreurs
  - **perd** s’il atteint 3 erreurs avant de trouver toutes les pièces
- Le jeu redémarre automatiquement après un message de victoire ou de défaite

---

## Détails techniques

### Génération des pièces
- Nombre de pièces cachées : **entre 15 et 20**
- Aucune pièce ne peut être placée dans une case adjacente :
  - horizontalement
  - verticalement
  - diagonalement

### Valeur des cases
- Chaque case non occupée affiche un nombre entre **0 et 8**
- Cette valeur représente le nombre de pièces présentes dans les cases voisines

---

## Fonctions principales

- `listIndexAlea()` : génère les positions aléatoires des pièces
- `valeurCases()` : calcule les valeurs numériques des cases
- `genererGrille()` : crée la grille HTML complète
- `clic(index)` : gère le clic sur une pièce
- `compterErreurs()` : gère les clics erronés
- `etatJeu()` : détermine victoire ou défaite
- `init()` : initialise ou réinitialise une partie

---

## Hypothèses

- Le joueur clique **une seule fois par case**
- Le joueur cesse de jouer après l’affichage :
  - *« Vous avez gagné ! »*
  - *« Vous avez perdu ! »*

---

## Exécution

Ce projet est conçu pour être exécuté dans un environnement web supportant Python côté client  
(ex. **Brython**, **Pyodide**, ou un framework pédagogique).

1. Charger la page HTML principale contenant un élément :
  
2. Inclure tp2.py et tp2.css

3. Lancer la fonction init() au chargement de la page



