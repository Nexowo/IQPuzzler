Rouge = [["R","R","R","R"],["R",0,0,0]]
Rose = [["Ro","Ro","Ro", 0],[0,0,"Ro","Ro"]]
Jaune = [["J","J","J","J"],[0,"J",0,0]]
BleuMarine = [["M","M","M"],["M",0,0],["M",0,0]]
Violet = [["V",0,0],["V","V",0],[0,"V","V"]]
Orange = [[0,"O",0],["O","O",0],[0,"O","O"]]
Vert = [["Ve","Ve","Ve"],["Ve",0,"Ve"]]
Turquoise = [["T","T","T"],["T","T",0]]
BleuVert = [["BV","BV","BV"],[0,"BV",0]]
Bordeaux = [["Bo","Bo",0],[0,"Bo","Bo"]]
BleuFonce = [["Bf","Bf","Bf"],["Bf",0,0]]
BleuClair = [["Bc","Bc"],["Bc",0]]

Pieces = [Rouge, Rose, Jaune, BleuMarine, Violet, Orange, Vert, Turquoise, BleuVert, Bordeaux, BleuFonce, BleuClair]

Piecesplacees = []

Plateau =  [[0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0]]

def testPiece(Piece, X, Y, Plat):
    Xi = 0
    for i in Piece:
        Yi=0
        for j in i:
            if j != 0 and Plat[X+Xi][Y+Yi] != 0:
                return False
            Yi+=1
        Xi+=1
    return True

def placerPiece(Piece, X, Y,Plat):
    Xi = 0
    for i in Piece:
        Yi=0
        for j in i:
            if j != 0:
                Plat[X+Xi][Y+Yi]=j
            Yi+=1
        Xi+=1
    return Plat

def afficherPlateau(Plat):
    for i in Plat:
        print(i)

def copy(plat1,plat2):
    for i in range(len(plat1)) :
        for j in range(len(plat1[0])):
            plat2[i][j] = plat1[i][j]

def copyNew(plat):
    platane = plat.copy()
    for i in range(len(platane)):
        platane[i] = plat[i].copy()
    return platane

def rotate_matrix(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

def transpose(m):
    return [[m[row][col] for row in range(0,len(m))] for col in range(0,len(m[0]))]

def remplissagePlateau(nbRotation, nbTransposee, Piece, Plat,out):
    if Pieces == []:
        return True
    else:
        for i in range(0,len(Plateau)-len(Piece)+1):
            for j in range(0,len(Plateau[0])-len(Piece[0])+1):
                if Piece in Pieces:
                    Pieces.remove(Piece)
                if testPiece(Piece, i, j, Plat):
                    if Pieces != []:
                        if remplissagePlateau(0,0,Pieces[0],placerPiece(Piece,i,j,copyNew(Plat)),out):
                            return True
                    else:
                        copy(placerPiece(Piece,i,j,copyNew(Plat)),out)
                        return True
        if nbRotation != 3:
            remplissagePlateau(nbRotation+1,nbTransposee,rotate_matrix(Piece),copyNew(Plat),out)
        elif nbTransposee != 1:
            remplissagePlateau(0,nbTransposee+1,transpose(Piece),copyNew(Plat),out)
        else:
            Pieces.insert(0,Piece)
            return False

outup = Plateau.copy()
if remplissagePlateau(0,0,Pieces[0],Plateau,outup):
    afficherPlateau(outup)
else:
    print("Erreur plateau")
    afficherPlateau(outup)
    afficherPlateau(Plateau)