import pygame
import sys
from personnage import Personnage

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

#Création du perso 
personnage = Personnage()

running = True

while running : 

    #Gestion des événements 
    for event in pygame.event.get() : 

        if event.type == pygame.QUIT : 
            running = False

    #MAJ du jeu 
    # Gestion des mouvements du perso 
    touche = pygame.key.get_pressed()
    personnage.deplacer(touche)

    #Efface l'écran 
    ecran.fill(COULEUR_FOND)

    #Dessine le perso 
    personnage.dessiner(ecran)


    #Affichage du jeu
    # Mets à jour l'affichage 
    pygame.display.flip()

pygame.quit()
sys.exit()