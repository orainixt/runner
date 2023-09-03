import pygame
import sys
import os 

class Personnage : 

    def __init__(self) : 
        self.x = 0
        self.y = 0
        self.frames = [] # liste d'images pour l'animation
        self.frameIndex = 0 #index de l'image actuelle
        self.animationSpeed = 10 #vitesse de l'animation 
        self.vitesse = 5
        self.gauche = False 
        self.droite = False

        #Charger les images de l'animation 
        dossierActuel = os.path.dirname(__file__)
        stickmanWaitingPath = os.path.join(dossierActuel, "..","ressources","notMoving.png")
        stickmanRightPath = os.path.join(dossierActuel, "..", "ressources","goingRight.png")
        self.frames.append(pygame.image.load(stickmanWaitingPath))
        self.frames.append(pygame.image.load(stickmanRightPath))

    def deplacer(self,touches) : 
        if touches[pygame.K_LEFT] : 
            self.x -= self.vitesse
        if touches[pygame.K_RIGHT] :
            self.x += self.vitesse
        if touches[pygame.K_UP] : 
            self.y -= self.vitesse 
        if touches[pygame.K_DOWN] : 
            self.y += self.vitesse
    
    def dessiner(self, fenetre) : 
        # Dessine la tête
        pygame.draw.circle(fenetre, (0, 0, 0), (self.x + self.taille // 2, self.y + self.taille // 4), self.taille // 4)

        # Dessine le corps (ligne verticale)
        pygame.draw.line(fenetre, (0, 0, 0), (self.x + self.taille // 2, self.y + self.taille // 2), (self.x + self.taille // 2, self.y + self.taille), 2)

        # Dessine les bras (lignes diagonales)
        pygame.draw.line(fenetre, (0, 0, 0), (self.x + self.taille // 2, self.y + self.taille // 2), (self.x + self.taille // 4, self.y + self.taille), 2)
        pygame.draw.line(fenetre, (0, 0, 0), (self.x + self.taille // 2, self.y + self.taille // 2), (self.x + 3 * self.taille // 4, self.y + self.taille), 2)

        # Dessine les jambes (lignes diagonales)
        pygame.draw.line(fenetre, (0, 0, 0), (self.x + self.taille // 2, self.y + self.taille), (self.x + self.taille // 4, self.y + 3 * self.taille // 2), 2)
        pygame.draw.line(fenetre, (0, 0, 0), (self.x + self.taille // 2, self.y + self.taille), (self.x + 3 * self.taille // 4, self.y + 3 * self.taille // 2), 2)
