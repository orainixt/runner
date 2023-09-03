import pygame
import sys

from personnage import Personnage
from obstacle import Obstacle

pygame.init()

## Variables of the screen 

LARGEUR_ECRAN = 1280
HAUTEUR_ECRAN = 720 
COULEUR_FOND = (255,255,255)
TITRE_ECRAN = "DeathRunner"
FPS = 60

## Création de la fenêtre 

ecran = pygame.display.set_mode((LARGEUR_ECRAN,HAUTEUR_ECRAN))
pygame.display.set_caption(TITRE_ECRAN)

# Création du perso 
personnage = Personnage(100,300)
# Gestion des obstacles du niveau 

running = True
clock = pygame.time.Clock()

while running : 

    #Gestion des événements 
    for event in pygame.event.get() : 

        if event.type == pygame.QUIT : 
            running = False

    #MAJ du jeu 
    # Gestion des mouvements du perso 
    touches = pygame.key.get_pressed()
    personnage.update(touches)

    #Efface l'écran 
    ecran.fill(COULEUR_FOND)

    #Dessine le perso 
    personnage.dessiner(ecran)


    #Affichage du jeu
    # Mets à jour l'affichage 
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()