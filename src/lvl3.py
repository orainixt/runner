import pygame
import sys

from personnage import Personnage
from obstacleNxtLvl import ObstacleNxtLvl
from obstacleLvl import ObstacleLvl
from obstacleButton import ObstacleButton


def run() : 

    pygame.init()

    # Variables nécessaires au chargement de la fenêtre 

    LARGEUR_ECRAN = 1280
    HAUTEUR_ECRAN = 720 
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
    personnage = Personnage(100,300)

    # Gestion des obstacles du niveau 
    obstacleGround = ObstacleLvl(0,660,"../ressources/global/ground.png")
    obstacleTxtName = ObstacleLvl(0,0,"../ressources/lvl/lvl3/txt1.png")
    obstacleTxt = ObstacleLvl(200,0,"../ressources/lvl/lvl3/txt2.png")
    obstacleVertical1 = ObstacleLvl(200,450,"../ressources/global/verticalObstacle1.png")
    

    # Obstacle de fin de niveau
    obstacleEndLvl = ObstacleNxtLvl(600,660,"../ressources/lvl/endLvl.png")

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
        obstacleTxtName.dessiner(ecran)
        obstacleTxt.dessiner(ecran)
        obstacleVertical1.dessiner(ecran)

        # Gestion des collisions 
        if personnage.collisionObstacle(obstacleVertical1) : 
            personnage.y = obstacleVertical1.y - 120
            personnage.velY = 0  # Arrête le saut du personnage
            personnage.solTrue = True  # Indique que le personnage est sur le sol

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