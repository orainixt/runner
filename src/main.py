# -*- coding: utf-8 -*-

import pygame

from obstacleButton import ObstacleButton
import lvl1
import levels

def main():

    pygame.init()

    LARGEUR_ECRAN = 1280
    HAUTEUR_ECRAN = 720
    COULEUR_FOND = (255, 255, 255)
    TITRE_ECRAN = "DeathRunner - Main Menu"
    running = True


    ecran = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
    pygame.display.set_caption(TITRE_ECRAN)


    start = ObstacleButton(500,100,"../ressources/global/start.png")
    lvl = ObstacleButton(500,300,"../ressources/global/level.png")


    while running : 

        #Gestion des événements 
        for event in pygame.event.get() : 

            if event.type == pygame.QUIT : 
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN: 

                if start.collision_point(event.pos) :
                    
                    lvl1.run()

                if lvl.collision_point(event.pos) : 
                    levels.run()

        ecran.fill(COULEUR_FOND)

        start.dessiner(ecran)
        lvl.dessiner(ecran)
        pygame.display.flip()

if __name__ == "__main__":
    main()