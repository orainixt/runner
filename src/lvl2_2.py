import pygame
import sys

import lvl3

from personnage import Personnage
from obstacleNxtLvl import ObstacleNxtLvl
from obstacleLvl import ObstacleLvl
from obstacleButton import ObstacleButton

def run() : 

    pygame.init()

    # Variables nécessaires au chargement de la fenêtre 

    LARGEUR_ECRAN = 600 
    HAUTEUR_ECRAN = 500
    COULEUR_FOND = (255,255,255)
    TITRE_ECRAN = "DeathRunner"
    FPS = 60
    ECHAP = False
    running = True
    clock = pygame.time.Clock()

    # Création de la fenêtre 

    ecran = pygame.display.set_mode((LARGEUR_ECRAN,HAUTEUR_ECRAN))
    pygame.display.set_caption(TITRE_ECRAN)

    # Gestion des décors 

    # Création du perso 
    personnage = Personnage(0,300)

    # Gestion des obstacles du niveau 
    obstacleGround = ObstacleLvl(0,660,"../ressources/global/ground.png")
    obstacleTxtName = ObstacleLvl(0,0,"../ressources/lvl/lvl2/missingLetters5.png")
    obstacleTxt = ObstacleLvl(400,0,"../ressources/lvl/lvl2/txtLvl2_2_1.png")
    obstacleFirstLetter = ObstacleNxtLvl(100,600,"../ressources/lvl/endLvl.png")
    obstacleSecondLetter = ObstacleNxtLvl(0,0,"../ressources/lvl/endLvl.png")
    obstacleThirdLetter = ObstacleNxtLvl(0,0,"../ressources/lvl/endLvl.png")
    obstacleFourthLetter = ObstacleNxtLvl(0,0,"../ressources/lvl/endLvl.png")
    obstacleFifthLetter = ObstacleNxtLvl(0,0,"../ressources/lvl/endLvl.png")
    obstacleEndLvl = ObstacleNxtLvl(0,0,"../ressources/lvl/endLvl.png")

    # Obstacle de fin de niveau


    while running : 

        #Gestion des événements 
        for event in pygame.event.get() : 

            if event.type == pygame.QUIT : 
                running = False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE : 
                    ECHAP = not ECHAP
            if ECHAP : 
                if event.type == pygame.MOUSEBUTTONDOWN : 
                    if buttonResume.collision_point(event.pos) : 
                        ECHAP = False
                    elif buttonQuit.collision_point(event.pos) : 
                        running = False

        #MAJ du jeu 
        # Gestion des mouvements du perso 

        touches = pygame.key.get_pressed()
    
        personnage.update(touches)


        #Efface l'écran 
        ecran.fill(COULEUR_FOND)
        
        #Dessine le décor 

        #Dessine le perso 
        personnage.dessiner(ecran)

        #Dessine les obstacles 
        obstacleGround.dessiner(ecran)
        obstacleFirstLetter.dessiner(ecran)
        obstacleTxt.dessiner(ecran)
        obstacleTxtName.dessiner(ecran)

        if personnage.collisionObstacle(obstacleFirstLetter) : 
            obstacleTxtName = ObstacleLvl(0,0,"../ressources/lvl/lvl2/missingLetters4.png")
            obstacleSecondLetter = ObstacleNxtLvl(500,600,"../ressources/lvl/endLvl.png")
            obstacleFirstLetter = ObstacleNxtLvl(0,0,"../ressources/lvl/endLvl.png")

        if personnage.collisionObstacle(obstacleSecondLetter) : 
            obstacleTxtName = ObstacleLvl(0,0,"../ressources/lvl/lvl2/missingLetters3.png")
            obstacleThirdLetter = ObstacleNxtLvl(0,600,"../ressources/lvl/endLvl.png")
            obstacleSecondLetter = ObstacleNxtLvl(0,0,"../ressources/lvl/endLvl.png")

        if personnage.collisionObstacle(obstacleThirdLetter) : 
            obstacleTxtName = ObstacleLvl(0,0,"../ressources/lvl/lvl2/missingLetters2.png")
            obstacleFourthLetter = ObstacleNxtLvl(500,600,"../ressources/lvl/endLvl.png")
            obstacleThirdLetter = ObstacleNxtLvl(0,0,"../ressources/lvl/endLvl.png")

        if personnage.collisionObstacle(obstacleFourthLetter) : 
            obstacleTxtName = ObstacleLvl(0,0,"../ressources/lvl/lvl2/missingLetters1.png")
            obstacleFifthLetter = ObstacleNxtLvl(500,600,"../ressources/lvl/endLvl.png")
            obstacleFourthLetter = ObstacleNxtLvl(0,0,"../ressources/lvl/endLvl.png")

        if personnage.collisionObstacle(obstacleFifthLetter) : 
            obstacleTxtName = ObstacleLvl(0,0,"../ressources/lvl/lvl2/missingLetters0.png")
            obstacleEndLvl = ObstacleNxtLvl(600,600,"../ressources/lvl/endLvl.png")
            obstacleFifthLetter = ObstacleNxtLvl(0,0,"../ressources/lvl/endLvl.png")
        
        if personnage.collisionObstacle(obstacleEndLvl) : 
            lvl3.run()

        # Gestion du menu Echap 
        if ECHAP : 

            ecran.fill(COULEUR_FOND)
            
            # Création du menu 
            buttonOption = ObstacleButton(500,100,"../ressources/global/optionButton.png")
            buttonResume = ObstacleButton(500,300,"../ressources/global/resumeButton.png")
            buttonQuit = ObstacleButton(500,500,"../ressources/global/quitButton.png")

            # Dessin du menu 
            buttonOption.dessiner(ecran)
            buttonResume.dessiner(ecran)
            buttonQuit.dessiner(ecran)


        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()