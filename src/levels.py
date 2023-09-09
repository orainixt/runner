import pygame 

import lvl1
import lvl2

from obstacleButton import ObstacleButton
def run() : 

    pygame.init()

    LARGEUR_ECRAN = 1280
    HAUTEUR_ECRAN = 720
    COULEUR_FOND = (255, 255, 255)
    TITRE_ECRAN = "DeathRunner - Level Menu"
    running = True


    ecran = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
    pygame.display.set_caption(TITRE_ECRAN)

    Olvl1 = ObstacleButton(0,0,"../ressources/levelMenu/1.png")
    Olvl2 = ObstacleButton(100,0,"../ressources/levelMenu/2.png")
    Olvl3 = ObstacleButton(200,0,"../ressources/levelMenu/3.png")
    Olvl4 = ObstacleButton(300,0,"../ressources/levelMenu/4.png")

    

    while running : 

        #Gestion des événements 
        for event in pygame.event.get() : 

            if event.type == pygame.QUIT : 
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                if Olvl1.collision_point(event.pos) : 
                    lvl1.run()
                elif Olvl2.collision_point(event.pos) : 
                    lvl2.run()

        ecran.fill(COULEUR_FOND) 

        Olvl1.dessiner(ecran)
        Olvl2.dessiner(ecran)
        Olvl3.dessiner(ecran)
        Olvl4.dessiner(ecran)

        pygame.display.flip()