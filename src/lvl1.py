import pygame
import sys
import os

from utils import update, collisionObstacle
from personnage import Personnage
from obstacle import Obstacle

pygame.init()

## Variables of the screen 

LARGEUR_ECRAN = 1280
HAUTEUR_ECRAN = 720 
COULEUR_FOND = (255,255,255)
TITRE_ECRAN = "DeathRunner"
FPS = 60
OPEN_NEXT_LVL = False

# Création de la fenêtre 

ecran = pygame.display.set_mode((LARGEUR_ECRAN,HAUTEUR_ECRAN))
pygame.display.set_caption(TITRE_ECRAN)

# Gestion des décors 
dossierActuel = os.path.dirname(__file__)
controlsPath = os.path.join(dossierActuel, "..", "ressources","controls_lvl1.png")
controlsPathAbsolute = pygame.image.load(controlsPath), (0,0)

# Création du perso 
personnage = Personnage(100,300)

# Gestion des obstacles du niveau 
obstacleGround = Obstacle(0,660,"../ressources/ground.png")
obstacleLarge1 = Obstacle(300,500,"../ressources/largeRectObst.png")
obstacleLarge2 = Obstacle (600,300,"../ressources/largeRectObst.png")
obstacleLarge3 = Obstacle (900,200,"../ressources/largeRectObst.png")


ETAT_JEU = "ingame"
running = True
clock = pygame.time.Clock()



while running : 

    #Gestion des événements 
    for event in pygame.event.get() : 

        if event.type == pygame.QUIT : 
            running = False

    if ETAT_JEU == "ingame" : 

        #MAJ du jeu 
        # Gestion des mouvements du perso 

        touches = pygame.key.get_pressed()

        if touches[pygame.K_ESCAPE] : 
            ETAT_JEU = "menu"
        else : 
            update(personnage,touches)


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

        #Gestion des collisions : 
        if collisionObstacle(personnage,obstacleLarge1) : 
            personnage.y = obstacleLarge1.y - 120
            personnage.velY = 0  # Arrête le saut du personnage
            personnage.solTrue = True  # Indique que le personnage est sur le sol
        
        if collisionObstacle(personnage,obstacleLarge2) : 
            personnage.y = obstacleLarge2.y - 120
            personnage.velY = 0  # Arrête le saut du personnage
            personnage.solTrue = True  # Indique que le personnage est sur le sol

        if collisionObstacle(personnage,obstacleLarge3) : 
            personnage.y = obstacleLarge3.y - 120
            personnage.velY = 0  # Arrête le saut du personnage
            personnage.solTrue = True  # Indique que le personnage est sur le sol

        #Affichage du jeu
        # Mets à jour l'affichage 
        pygame.display.flip()
        clock.tick(FPS)

    elif ETAT_JEU == "menu" : 
        import echap
        if echap.runEchap() : 
            ETAT_JEU = "ingame"
        

    
pygame.quit()
sys.exit()