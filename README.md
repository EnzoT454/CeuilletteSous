# Cueillette de sous — Jeu web interactif

Projet web interactif implémentant le jeu **« Cueillette de sous »**, inspiré du principe du démineur.  
Le joueur explore une grille 10×10 afin de découvrir des pièces cachées, tout en évitant de faire trop d’erreurs.

Le jeu est développé en **Python exécuté côté navigateur** à l’aide du moteur **CodeBoot**, avec génération dynamique du contenu HTML et mise en forme via CSS.

---

## Description

À chaque partie, le jeu génère :
- une **grille 10×10**
- entre **15 et 20 pièces cachées**, placées aléatoirement
- aucune pièce n’est adjacente à une autre (horizontalement, verticalement ou en diagonale)

Chaque case non occupée affiche un nombre indiquant le **nombre de pièces voisines**, ce qui aide le joueur à faire ses choix.

---

## Règles du jeu

- Le joueur clique sur les cases de la grille :
  - 🪙 **Case avec pièce** : la pièce est révélée
  - ❌ **Case vide** : une erreur est comptabilisée
- Le joueur :
  - **gagne** s’il découvre toutes les pièces avec moins de 3 erreurs
  - **perd** s’il atteint 3 erreurs avant d’avoir trouvé toutes les pièces
- Une fois la partie terminée :
  - un message *« Vous avez gagné ! »* ou *« Vous avez perdu ! »* est affiché
  - la partie redémarre automatiquement après quelques secondes

**Hypothèses**
- Une seule interaction par case
- Le joueur cesse de cliquer après la fin de la partie

---

## Structure du projet

```text
.
├── server-webTp2.py     # Serveur HTTP local
└── documents_tp2/
├── index.html           # Page principale
├── tp2.py               # Logique du jeu (Python)
├── tp2.css              # Style de la grille et de l’interface
├── codeboot.bundle.js   # Moteur CodeBoot
├── codeboot.bundle.css
└── symboles/
└── coste.svg            # Icône de pièce
```

---

## Prérequis

- Python 3.x
- Un navigateur web moderne (Chrome, Firefox, Safari)
- Aucun framework externe à installer

> Le jeu ne fonctionne pas si `index.html` est ouvert directement sans serveur.

---

## Étapes d’exécution

### 1️⃣ Démarrer le serveur web

Depuis le dossier contenant `server-webTp2.py` :

```bash
python3 server-webTp2.py
```

### 2️⃣ Lancer le jeu

Ouvrir un navigateur et accéder à :

```bash
http://localhost:8000
```

La page index.html est chargée automatiquement, et le jeu s’affiche dans le navigateur.

Cliquer sur Nouvelle partie pour commencer à jouer.








