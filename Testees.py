# Ecrit par Régis Lomba
# Tester au Makilab @FABLAB @Louvain-La-Neuve


# -*-coding:Latin-1 -*

# ------------- espace fonction ---------------------------#

# --- FONCTION 1 : CRENEAU X --- #
#startXF = coordonnéeX du point de départ
#startYF = coordonnéeY du point de départ
#distF = longueur du côté
#posORneg = direction 1 = vers la droite, -1 = vers la gauche
#thickF = epaisseur du materiaux
#upORdown = sens des créneaux: 1 vers le bas, -1 vers le haut (attention le repère actuel est Y+ vers le bas)

def creneauX(startXF, startYF, distF, posORneg, thickF, upORdown):
    listePoints= list()
    modF = (distF%10)/2
    distParcourueF = 0
    distXF = startXF + (modF + 5)*posORneg 
    distYF = startYF
    listePoints.append((distXF, distYF))
    distParcourueF = distParcourueF + (modF + 5)   
    
    while distParcourueF < distF - modF - 5 :
        #on avance de 2,5
        distXF = distXF+2.5*posORneg 
        listePoints.append((distXF, distYF))
        #on rentre de épaisseur
        distYF = distYF + thickF*upORdown
        listePoints.append((distXF, distYF))
        #on avance de 5
        distXF = distXF+ 5*posORneg 
        listePoints.append((distXF, distYF))
        #on sort de épaisseur
        distYF = distYF - thickF*upORdown
        listePoints.append((distXF, distYF))
        #on avance de 2,5
        distXF = distXF+2.5*posORneg 
        listePoints.append((distXF, distYF))
        distParcourueF = distParcourueF + 10    
    
    distXF = distXF + (modF + 5)*posORneg 
    listePoints.append((distXF, distYF))    
    
    return listePoints

# --- FONCTION 2 : CRENEAU Y --- #
#startXF = coordonnéeX du point de départ
#startYF = coordonnéeY du point de départ
#distF = longueur du côté
#posORneg = direction 1 = vers la droite, -1 = vers la gauche
#thickF = epaisseur du materiaux
#upORdown = sens des créneaux: 1 vers le bas, -1 vers le haut (attention le repère actuel est Y+ vers le bas)

def creneauY(startXF, startYF, distF, posORneg, thickF, upORdown):
    listePoints= list()
    modF = (distF%10)/2
    distParcourueF = 0
    distXF = startXF 
    distYF = startYF + (modF + 5)*posORneg 
    listePoints.append((distXF, distYF))
    distParcourueF = distParcourueF + (modF + 5)   
    
    while distParcourueF < distF - modF - 5 :
        #on avance de 2,5
        distYF = distYF+2.5*posORneg 
        listePoints.append((distXF, distYF))
        #on rentre de épaisseur
        distXF = distXF + thickF*upORdown
        listePoints.append((distXF, distYF))
        #on avance de 5
        distYF = distYF+ 5*posORneg 
        listePoints.append((distXF, distYF))
        #on sort de épaisseur
        distXF = distXF - thickF*upORdown
        listePoints.append((distXF, distYF))
        #on avance de 2,5
        distYF = distYF+2.5*posORneg 
        listePoints.append((distXF, distYF))
        distParcourueF = distParcourueF + 10    
    
    distYF = distYF + (modF + 5)*posORneg 
    listePoints.append((distXF, distYF))    
    
    return listePoints

def Hatch(drawingF, startXF, startYF, lengthXF, lengthYF):
    trayLength = (lengthYF - 5)/2
    maxX = startXF + lengthXF - 3
    
    refX = startXF + 3
    refY = startYF 
    while refX <  maxX:
        a = svgwrite.shapes.Polyline([(refX,refY),(refX,refY+trayLength)], stroke='black', fill='white')
        drawingF.add(a)
        a = svgwrite.shapes.Polyline([(refX,refY+trayLength+5),(refX,refY+lengthYF)], stroke='black', fill='white')
        drawingF.add(a)
        refX = refX + 3
        if refX < maxX:
            a = svgwrite.shapes.Polyline([(refX,refY+5),(refX,refY+lengthYF-5)], stroke='black', fill='white')
            drawingF.add(a)
        refX = refX + 3
    return drawingF
#---------------------------UNDER DEV

# --- FONCTION 4 : CIRCLE ARC CLOCKWISE --- #
#startXF = coordonnéeX du point de départ
#startYF = coordonnéeY du point de départ
#distF = longueur du côté
#posORneg = direction 1 = vers la droite, -1 = vers la gauche
#thickF = epaisseur du materiaux
#upORdown = sens des créneaux: 1 vers le bas, -1 vers le haut (attention le repère actuel est Y+ vers le bas)

def creneauCircClockWise(startXF, startYF, radiusF, angleF, thickF):
    listePoints= list()
    angleParcouru = 0
    distParcourueF = 0
    
    #---FIRST POINT
    
    distF = 2*math.pi*radiusF*angleF/360
    modF = (distF%10)/2
    
    distParcourueF = distParcourueF + (modF + 5) 
    angleParcouru = distParcourueF*360/2/math.pi/radiusF
    
    arcX = startXF + (radiusF) * math.cos(angleParcouru*math.pi/180)
    arcY = startYF + (radiusF) * math.sin(angleParcouru*math.pi/180)    
    listePoints.append((arcX, arcY))
       
    
    while distParcourueF < distF - modF - 5 :
        #on avance de 2,5
        distParcourueF = distParcourueF + 2.5
        angleParcouru = distParcourueF*360/2/math.pi/radiusF
        arcX = startXF + (radiusF) * math.cos(angleParcouru*math.pi/180)
        arcY = startYF + (radiusF) * math.sin(angleParcouru*math.pi/180)    
        listePoints.append((arcX, arcY))        
        
        #on rentre de épaisseur
        arcX = startXF + (radiusF-thick) * math.cos(angleParcouru*math.pi/180)
        arcY = startYF + (radiusF-thick) * math.sin(angleParcouru*math.pi/180)           
        listePoints.append((arcX, arcY))
        
        #on avance de 5
        distParcourueF = distParcourueF + 5
        angleParcouru = distParcourueF*360/2/math.pi/radiusF
        arcX = startXF + (radiusF - thick) * math.cos(angleParcouru*math.pi/180)
        arcY = startYF + (radiusF - thick) * math.sin(angleParcouru*math.pi/180)    
        listePoints.append((arcX, arcY))         

        #on sort de épaisseur
        arcX = startXF + (radiusF) * math.cos(angleParcouru*math.pi/180)
        arcY = startYF + (radiusF) * math.sin(angleParcouru*math.pi/180)           
        listePoints.append((arcX, arcY))    

        #on avance de 2,5
        distParcourueF = distParcourueF + 2.5
        angleParcouru = distParcourueF*360/2/math.pi/radiusF
        arcX = startXF + (radiusF) * math.cos(angleParcouru*math.pi/180)
        arcY = startYF + (radiusF) * math.sin(angleParcouru*math.pi/180)    
        listePoints.append((arcX, arcY))    
    #On finalise
    distParcourueF = distF
    angleParcouru = distParcourueF*360/2/math.pi/radiusF
    arcX = startXF + (radiusF) * math.cos(angleParcouru*math.pi/180)
    arcY = startYF + (radiusF) * math.sin(angleParcouru*math.pi/180)    
    listePoints.append((arcX, arcY))    
    return listePoints
#---------------------------UNDER DEV

# --- FONCTION 5 : CIRCLE ARC COUNTERCLOCKWISE --- #
def creneauCircCounterClockWise(startXF, startYF, radiusF, angleF, thickF):
    listePoints= list()
    angleParcouru = 0
    distParcourueF = 0
    
    #---FIRST POINT
    
    distF = 2*math.pi*radiusF*angleF/360
    modF = (distF%10)/2
    
    distParcourueF = distParcourueF + (modF + 5) 
    angleParcouru = distParcourueF*360/2/math.pi/radiusF
    
    arcX = startXF + (radiusF) * math.sin(angleParcouru*math.pi/180)
    arcY = startYF + (radiusF) * math.cos(angleParcouru*math.pi/180)    
    listePoints.append((arcX, arcY))
       
 
    while distParcourueF < distF - modF - 5 :
        #on avance de 2,5
        distParcourueF = distParcourueF + 2.5
        angleParcouru = distParcourueF*360/2/math.pi/radiusF
        arcX = startXF + (radiusF) * math.sin(angleParcouru*math.pi/180)
        arcY = startYF + (radiusF) * math.cos(angleParcouru*math.pi/180)    
        listePoints.append((arcX, arcY))        
        
        #on rentre de épaisseur
        arcX = startXF + (radiusF + thick) * math.sin(angleParcouru*math.pi/180)
        arcY = startYF + (radiusF + thick) * math.cos(angleParcouru*math.pi/180)           
        listePoints.append((arcX, arcY))
        
        #on avance de 5
        distParcourueF = distParcourueF + 5
        angleParcouru = distParcourueF*360/2/math.pi/radiusF
        arcX = startXF + (radiusF + thick) * math.sin(angleParcouru*math.pi/180)
        arcY = startYF + (radiusF + thick) * math.cos(angleParcouru*math.pi/180)    
        listePoints.append((arcX, arcY))         

#        #on sort de épaisseur
        arcX = startXF + (radiusF) * math.sin(angleParcouru*math.pi/180)
        arcY = startYF + (radiusF) * math.cos(angleParcouru*math.pi/180)           
        listePoints.append((arcX, arcY))    

        #on avance de 2,5
        distParcourueF = distParcourueF + 2.5
        angleParcouru = distParcourueF*360/2/math.pi/radiusF
        arcX = startXF + (radiusF) * math.sin(angleParcouru*math.pi/180)
        arcY = startYF + (radiusF) * math.cos(angleParcouru*math.pi/180)    
        listePoints.append((arcX, arcY))    
    #On finalise
    distParcourueF = distF
    angleParcouru = distParcourueF*360/2/math.pi/radiusF
    arcX = startXF + (radiusF) * math.sin(angleParcouru*math.pi/180)
    arcY = startYF + (radiusF) * math.cos(angleParcouru*math.pi/180)    
    listePoints.append((arcX, arcY))    
    return listePoints
# ----------------------------------------------------------#
import svgwrite
import math
from svgwrite import mm 
#on crée l'espace de travail
dwg = svgwrite.Drawing('testees.svg', size=('600mm','400mm'))

#on récupère les paramètres du dessin
R_A = float(input('Quel est le rayon intérieur en mm ? :'))
R_B = float(input('Quel est le rayon extérieur en mm ? :'))
H = float(input('Quel est la hauteur en mm ? :'))
angle = 90 #float(input('Quel est l\'angle d\'ouverture en degré ? :'))
thick = float(input('Quel est l\'épaisseur du matériaux ? : '))

print('les paramètres du tiroir sont (R_A, R_B, H, angle):', R_A, ' ', R_B, ' ', H, ' ', angle)

# OBJET 1 et 2 : les petits rectangles de côté
#on déduit les paramètres utiles:
smallSideLargeur = R_B - R_A
smallSideHauteur = H

#on définit le point d'ancrage:
refX = 10
refY = 10
#on crée le Polyline 
smallSide = svgwrite.shapes.Polyline([(refX,refY)], stroke='black', fill='white')


#---- COTE 1 --- on dessine la base ( = crenelage)
#Point de départ 
distX = refX 
distY = refY 

a = creneauX(distX, distY, smallSideLargeur, 1, thick, -1)
smallSide.points.extend(a)

#---- COTE 2 ---- on dessine un côté montant ( = crenelage)
#Point de départ
distX = distX + smallSideLargeur - thick
distY = distY - thick
smallSide.points.append((distX, distY))

a = creneauY(distX, distY, smallSideHauteur, 1 , thick, 1)
smallSide.points.extend(a)

#---- COTE 3 ----  on dessine le dessus (= ligne)
distX = distX - smallSideLargeur + 2*thick
distY = distY + smallSideHauteur
smallSide.points.append((distX, distY))

#---- COTE 4 ----  on dessine le côté descendant ( = crénelage, = premier coté montant)
a = creneauY(distX, distY, smallSideHauteur, -1 , thick, -1)
smallSide.points.extend(a)
               
dwg.add(smallSide)

#OBJET 3: rectangle à courber pour petit côté
#on déduit les paramètres utiles:
smallRoundedSideLong = 2*math.pi*(R_A+thick)*angle/360
smallRoundedSideHauteur = H
#on définit le point d'ancrage:
refX = refX
refY = refY + smallSideHauteur +10

#on crée le Polyline 
smallRoundedSide = svgwrite.shapes.Polyline([(refX,refY)], stroke='black', fill='white')

#---- COTE 1 --- on dessine la base ( = crenelage)
#Point de départ 
distX = refX 
distY = refY

a = creneauX(distX, distY, smallRoundedSideLong, 1, thick, 1)
smallRoundedSide.points.extend(a)

#---- COTE 2 ---- on dessine un côté montant ( = crenelage)
#Point de départ
distX = distX + smallRoundedSideLong

a = creneauY(distX, distY, smallRoundedSideHauteur, 1 , thick, -1)
smallRoundedSide.points.extend(a)

#---- COTE 3 ----  on dessine le dessus (= ligne)
distX = distX - smallRoundedSideLong 
distY = distY + smallRoundedSideHauteur
smallRoundedSide.points.append((distX, distY))

#---- COTE 4 ----  on dessine le côté descendant ( = crénelage, = premier coté montant)
a = creneauY(distX, distY, smallRoundedSideHauteur, -1 , thick, 1)
smallRoundedSide.points.extend(a)

dwg.add(smallRoundedSide)

#---On Hachure---#

#Point de départ 
distX = refX 
distY = refY

dwg = Hatch(dwg, distX+thick, distY+thick, smallRoundedSideLong-2*thick, smallRoundedSideHauteur -thick)

#OBJET 4: rectangle à courber pour grand côté

#on déduit les paramètres utiles:
largeRoundedSideLong = 2*math.pi*(R_B-thick)*angle/360
largeRoundedSideHauteur = H

#on définit le point d'ancrage:
refX = refX
refY = refY + smallRoundedSideHauteur +10

#on crée le Polyline 
largeRoundedSide = svgwrite.shapes.Polyline([(refX,refY)], stroke='black', fill='white')

#---- COTE 1 --- on dessine la base ( = crenelage)
#Point de départ 
distX = refX 
distY = refY

a = creneauX(distX, distY, largeRoundedSideLong, 1, thick, 1)
largeRoundedSide.points.extend(a)

#---- COTE 2 ---- on dessine un côté montant ( = crenelage)
#Point de départ
distX = distX + largeRoundedSideLong

a = creneauY(distX, distY, largeRoundedSideHauteur, 1 , thick, -1)
largeRoundedSide.points.extend(a)

#---- COTE 3 ----  on dessine le dessus (= ligne)
distX = distX - largeRoundedSideLong 
distY = distY + largeRoundedSideHauteur
largeRoundedSide.points.append((distX, distY))

#---- COTE 4 ----  on dessine le côté descendant ( = crénelage, = premier coté montant)
a = creneauY(distX, distY, largeRoundedSideHauteur, -1 , thick, 1)
largeRoundedSide.points.extend(a)

dwg.add(largeRoundedSide)

#---On Hachure---#

#Point de départ 
distX = refX 
distY = refY

dwg = Hatch(dwg, distX+thick, distY+thick, largeRoundedSideLong-2*thick, largeRoundedSideHauteur -thick)

#OBJET 5: fond du tiroir

#on définit le point d'ancrage:
refX = refX
refY = refY + largeRoundedSideHauteur +10

#on crée le Polyline 
bottomSide = svgwrite.shapes.Polyline([(refX+R_A+thick,refY)], stroke='black', fill='white')

#---- COTE 1 --- on dessine la base ( = petit rayon et crenelage)
#Point de départ 
distX = refX 
distY = refY

a = creneauCircClockWise(distX, distY, R_A+thick, angle, thick)
bottomSide.points.extend(a)

#---- COTE 2 --- on dessine la verticale
distX = refX 
distY = refY+R_A

a = creneauY(distX, distY, smallSideLargeur, 1 , thick, 1)
bottomSide.points.extend(a)

distY = refY+R_B-thick
bottomSide.points.append((distX, distY))

#---- COTE 3 --- on dessine l'extérieur ( = petit rayon et crenelage)
#Point de départ 
distX = refX 
distY = refY
a=creneauCircCounterClockWise(distX, distY, R_B-thick, angle, thick)
bottomSide.points.extend(a)

#---- COTE 4 --- on dessine l'horizontale ( = petit rayon et crenelage)
#Point de départ
distX = refX + R_B 
distY = refY
a = creneauX(distX, distY, smallSideLargeur, -1, thick, 1)
bottomSide.points.extend(a)
dwg.add(bottomSide)
    
dwg.save()


 

