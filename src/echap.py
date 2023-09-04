import pygame
import sys
import os

from personnage import Personnage

pygame.init()

## Variables of the screen 

LARGEUR_ECRAN = 1280
HAUTEUR_ECRAN = 720 
COULEUR_FOND = (255,255,255)
TITRE_ECRAN = "DeathRunner - Menu Screen"
FPS = 60

## Création de la fenêtre 


ecran = pygame.display.set_mode((LARGEUR_ECRAN,HAUTEUR_ECRAN))
pygame.display.set_caption(TITRE_ECRAN)

dossierActuel = os.path.dirname(os.path.abspath(__file__))
screenPath = os.path.join(dossierActuel, "..", "ressources", "echapScreen.png")
imageBackground = pygame.image.load(screenPath)



# Gestion des obstacles du niveau 

def runEchap() : 

    running = True

    while running : 

        #Gestion des événements 
        for event in pygame.event.get() : 

            if event.type == pygame.QUIT : 
                running = False

        #MAJ du jeu 

        #Efface l'écran 
        ecran.fill(COULEUR_FOND)

        ecran.blit(imageBackground,(0,0))
        #Dessine le perso 

        #Dessine les obstacles 

        #Affichage du jeu
        # Mets à jour l'affichage 
        pygame.display.flip()

    pygame.quit()
    sys.exit()