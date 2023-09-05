import pygame
import sys
import os

import echap

from personnage import Personnage
from obstacleLvl import ObstacleLvl
from obstacleNxtLvl import ObstacleNxtLvl


pygame.init()

# Variables nécessaires au chargement de la fenêtre 

LARGEUR_ECRAN = 1280
HAUTEUR_ECRAN = 720 
COULEUR_FOND = (255,255,255)
TITRE_ECRAN = "DeathRunner"
FPS = 60
OPEN_NEXT_LVL = False
ECHAP = False
running = True
clock = pygame.time.Clock()

# Création de la fenêtre 

ecran = pygame.display.set_mode((LARGEUR_ECRAN,HAUTEUR_ECRAN))
pygame.display.set_caption(TITRE_ECRAN)

# Gestion des décors 
dossierActuel = os.path.dirname(__file__)
controlsPath = os.path.join(dossierActuel, "..", "ressources","lvl","lvl1","controls_lvl1.png")
controlsPathAbsolute = pygame.image.load(controlsPath), (0,0)

# Création du perso 
personnage = Personnage(100,300)

# Gestion des obstacles du niveau 
obstacleGround = ObstacleLvl(0,660,"../ressources/global/ground.png")
obstacleLarge1 = ObstacleLvl(300,500,"../ressources/global/largeRectObst.png")
obstacleLarge2 = ObstacleLvl(600,300,"../ressources/global/largeRectObst.png")
obstacleLarge3 = ObstacleLvl(900,200,"../ressources/global/largeRectObst.png")

# Obstacle de fin de niveau
obstacleEndLvl = ObstacleNxtLvl(1250,100,"../ressources/lvl/endLvl.png")


while running : 

    #Gestion des événements 
    for event in pygame.event.get() : 

        if event.type == pygame.QUIT : 
            running = False

   #MAJ du jeu 
    # Gestion des mouvements du perso 

    touches = pygame.key.get_pressed()
    
    if touches[pygame.K_ESCAPE] : 
        ECHAP = True
    else : 
        personnage.update(touches)


    #Efface l'écran 
    ecran.fill(COULEUR_FOND)
        
    #Dessine le décor 
    ecran.blit(controlsPathAbsolute[0], (0, 0)) 

    #Dessine le perso 
    personnage.dessiner(ecran)

    #Dessine les obstacles 
    obstacleGround.dessiner(ecran)
    obstacleLarge1.dessiner(ecran)
    obstacleLarge2.dessiner(ecran)
    obstacleLarge3.dessiner(ecran)
    obstacleEndLvl.dessiner(ecran)

    #Gestion des collisions : 
    if personnage.collisionObstacle(obstacleLarge1) : 
        personnage.y = obstacleLarge1.y - 120
        personnage.velY = 0  # Arrête le saut du personnage
        personnage.solTrue = True  # Indique que le personnage est sur le sol
        
    if personnage.collisionObstacle(obstacleLarge2) : 
        personnage.y = obstacleLarge2.y - 120
        personnage.velY = 0  # Arrête le saut du personnage
        personnage.solTrue = True  # Indique que le personnage est sur le sol

    if personnage.collisionObstacle(obstacleLarge3) : 
        personnage.y = obstacleLarge3.y - 120
        personnage.velY = 0  # Arrête le saut du personnage
        personnage.solTrue = True  # Indique que le personnage est sur le sol

    if personnage.collisionObstacle(obstacleEndLvl) : 
        running = False

    if ECHAP : 
        gameMenu = echap.runEchap(ecran)
        if gameMenu : 
            ECHAP = False
    #Affichage du jeu
    # Mets à jour l'affichage 
    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()
sys.exit()