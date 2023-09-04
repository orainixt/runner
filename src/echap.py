import pygame
import os

import lvl1

pygame.init()

# Variables nécessaires au chargement de la fenêtre 

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


def runEchap() : 
    """
    Méthode permettant de lancer la fenêtre de menu 

    Returns :
        returnGame (bool) vrai quand la méthode doit s'arrêter pour retourner au jeu
    """

    running = True
    returnGame = False

    while running : 

        #Gestion des événements 
        for event in pygame.event.get() : 

            if event.type == pygame.QUIT : 
                running = False
            
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE : 
                    lvl1.ETAT_JEU = "ingame"
                    returnGame = True 
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
    return returnGame
