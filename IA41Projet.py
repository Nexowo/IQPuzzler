#Définition de la forme de chaque pièce sous la forme d'un tableau à double dimensions en choisissant des 0 pour les cases correspondant à des vides sur les jeux réels et un string pour les cases correspondant à des pleins.
#Les string changent en fonction des pièces pour les reconnaître
Rouge = [["R","R","R","R"],["R",0,0,0]]
Rose = [["P","P","P", 0],[0,0,"P","P"]]
Jaune = [["J","J","J","J"],[0,"J",0,0]]
BleuMarine = [["M","M","M"],["M",0,0],["M",0,0]]
Violet = [["A",0,0],["A","A",0],[0,"A","A"]] 
Orange = [[0,"O",0],["O","O",0],[0,"O","O"]]
Vert = [["V","V","V"],["V",0,"V"]] 
Turquoise = [["T","T","T"],["T","T",0]]
BleuVert = [["B","B","B"],[0,"B",0]] 
Bordeaux = [["S","S",0],[0,"S","S"]] 
BleuFonce = [["F","F","F"],["F",0,0]] 
BleuClair = [["C","C"],["C",0]]

Pieces = [Rouge, Rose, Jaune, BleuMarine, Violet, Orange, Vert, Turquoise, BleuVert, Bordeaux, BleuFonce, BleuClair] #Tableau de l'ensemble des pièces disponibles dans le jeu

Piecesplacees = [] #Tableau de toutes les pièces placées dans la configuration de départ du plateau

print('Veuillez selectionner un cas parmi les cas suivants : \n 0 --> Plateau 1 (11*5) vide \n 1 à 40 --> Problèmes du plateau 1 \n 100 --> Plateau 2 (Plateau diagonal) vide \n 101 à 140 --> Problèmes du plateau 2')
choix = int(input('Votre choix : '))

while choix<-1 or 41<choix<99 or choix>140:
    print('Option invalide')
    choix = int(input('Votre choix : '))

if -1<choix<41:

    Plateau = [[0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0,0]] #Configuration de base du plateau 1 sous la forme d'un tableau à 2 dimensions

    with open('./Plateaux1.txt','r') as file1: #Ouverture du fichier des problèmes du plateau 1
        for _ in range(3*choix+1): #Choix du problème choisi par l'utilisateur
            next(file1)
        temp = file1.readline() #Lecture du problème choisi

#Remplissage du plateau avec le problème choisi
    for i in range(5):
        for j in range(11):
            if temp[11*i+j] != '0':
                Plateau[i][j] = temp[11*i+j]

#Récupération des pièces déjà placées dans le problème choisi
    for Piece in Pieces:
        for i in Piece[0]:
            if i != 0:
                charPiece = i
        for i in range(5):
            if charPiece in Plateau[i]:
                if not Piece in Piecesplacees:
                    Piecesplacees.insert(0,Piece) 

else:

        Plateau = [[0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0]] #Configuration de base du plateau 2 sous la forme d'un tableau à 2 dimensions 

        probleme = choix - 100
    
        with open('./Plateaux2.txt','r') as file2: #Ouverture du fichier des problèmes du plateau 2
            for _ in range(3*probleme+1): #Choix du problème choisi par l'utilisateur
                next(file2)
            temp = file2.readline() #Lecture du problème choisi      
        
#Remplissage du plateau avec le problème choisi
        for i in range(9):
            for j in range(9):
                if temp[9*i+j] != '0':
                    Plateau[i][j] = temp[9*i+j]

#Récupération des pièces déjà placées dans le problème choisi
        for Piece in Pieces:
            for i in Piece[0]:
                if i != 0:
                    charPiece = i
            for i in range(9):
                if charPiece in Plateau[i]:
                    if not Piece in Piecesplacees:
                        Piecesplacees.insert(0,Piece) 


def testPiece(Piece, X, Y, Plat): #Fonction permettant de tester si une pièce peut être placée dans le plateau avec son coin supérieur en position (X,Y)
    Xi = 0
    for i in Piece:
        Yi=0
        for j in i:
            if j != 0 and Plat[X+Xi][Y+Yi] != 0:
                return False
            Yi+=1
        Xi+=1
    return True

def placerPiece(Piece, X, Y,Plat): #Fonction permettant de placer une pièce dans le plateau
    Xi = 0
    for i in Piece:
        Yi=0
        for j in i:
            if j != 0:
                Plat[X+Xi][Y+Yi]=j
            Yi+=1
        Xi+=1
    return Plat

def afficherPlateau(Plat): #Fonction permettant l'affichage du plateau
    for i in Plat:
        print(i)

def copy(plat1,plat2): #Fonction qui permet la copie d'un plateau dans un second plateau et éviter tout problème de pointeur
    for i in range(len(plat1)) :
        for j in range(len(plat1[0])):
            plat2[i][j] = plat1[i][j]

def copyNew(plat): #Fonction qui crée un nouveau plateau et qui copie les valeurs de plat dans le nouveau plateau et éviter tout problème de pointeur
    platane = plat.copy()
    for i in range(len(platane)):
        platane[i] = plat[i].copy()
    return platane

def rotate_matrix(m): #Fonction permettant d'effectuer une rotation de matrice afin de faire effectuer des rotations aux pièces, cette fonction a été récupérée ici: https://stackoverflow.com/questions/53250821/in-python-how-do-i-rotate-a-matrix-90-degrees-counterclockwise
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

def transpose(m): #Fonction permettant de faire une transposée de matrice afin de l'effectuer sur les pièces
    return [[m[row][col] for row in range(0,len(m))] for col in range(0,len(m[0]))]

def remplissagePlateau(Piece, Plat): #Fonction principale permettant de remplir le tableau de manière récursive
    if Pieces == []: #Cas Trivial
        copy(Plat,output)
        return True
    else:
        Pieces.remove(Piece) #On supprime la pièce du tableau de pièces restantes à placer
        for _ in range(2): #On considère qu'une pièce possède 1 transposée sans comptabiliser l'état de base
            for _ in range(4): #On considère qu'une pièce possède 3 rotations sans comptabiliser l'état de base
                for i in range(0,len(Plateau)-len(Piece)+1): #Pour chaque pièce du plateau on essaye de la placer avec son coin en (i,j) en faisant attention à ne pas dépasser du plateau
                    for j in range(0,len(Plateau[0])-len(Piece[0])+1):
                        if testPiece(Piece, i, j, Plat): #On teste si la pièce peut-être placée en (i,j)
                            if Pieces != []:
                                if remplissagePlateau(Pieces[0],placerPiece(Piece,i,j,copyNew(Plat))): #Appel récursif si le tableau de pièces restante n'est pas vide
                                    return True
                            else:
                                copy(placerPiece(Piece,i,j,Plat),output) #Placement de la pièce s'il s'agit de la dernière à placer
                                return True
                Piece = rotate_matrix(Piece) #Rotation de la Piece si l'appel récursif renvoie faux ou que l'on ne peux pas placer la pièce telle quelle dans le plateau (i,j)
            Piece = transpose(Piece) #Transosée de la pièce si aucune des rotations n'est plaçable
        Pieces.insert(0,Piece) #Si après toutes les rotations et les transposées la pièce n'est pas placée on la replace dans le tableau en tête de pièce et on retourne faux
        return False



for Piece in Piecesplacees: #Au lancement du programme on supprime toutes les pièces de la configuration initale du plateau des pièces restantes à placer
    if Piece in Pieces:
        Pieces.remove(Piece)

output =copyNew(Plateau)

if remplissagePlateau(Pieces[0],Plateau):
        afficherPlateau(Plateau)
        print('')
        afficherPlateau(output)
        print('R = Pièce Rouge \nP = Pièce Rose \nJ = Pièce Jaune \nM = Pièce Bleu Marine \nA = Pièce Violette \nO = Pièce Orange \nV = Pièce Verte \nT = Pièce Turquoise \nB = Pièce Bleu-Vert \nS = Pièce Bordeaux \nF = Pièce Bleu foncé \nC = Pièce Bleu Clair')
        if 99<choix<141:
            print('X = Pas de pièce')

else:
        print("Erreur plateau")
        afficherPlateau(output)
        print('')
        afficherPlateau(Plateau)
