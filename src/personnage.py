import pygame
import sys
import os 

class Personnage : 

    def __init__(self, x = 0,y=0) : 
        self.x = x
        self.y = y
        self.frames = [] # liste d'images pour l'animation
        self.frameIndex = 0 # index de l'image actuelle
        self.animationSpeed = 10 #vitesse de l'animation 
        self.vitesse = 5
        self.gauche = False 
        self.droite = False
        self.haut = False
        self.bas = False 

        #Charger les images de l'animation 
        dossierActuel = os.path.dirname(__file__)
        stickmanLeftPath = os.path.join(dossierActuel, "..", "ressources","goingLeft.png")
        stickmanRightPath = os.path.join(dossierActuel, "..", "ressources","goingRight.png")
        stickmanUpPath = os.path.join(dossierActuel, "..", "ressources","jumping.png")
        stickmanDownPath = os.path.join(dossierActuel, "..", "ressources","crawling.png")
        #stickmanWaitingPath = os.path.join(dossierActuel, "..","ressources","notMoving.png")
        
        self.frames.append(pygame.image.load(stickmanLeftPath))
        self.frames.append(pygame.image.load(stickmanRightPath))
        self.frames.append(pygame.image.load(stickmanUpPath))
        self.frames.append(pygame.image.load(stickmanDownPath))

    def deplacer(self,touches) : 
        if touches[pygame.K_LEFT] : 
            self.x -= self.vitesse
            self.gauche = True
            self.droite = False 
            self.haut = False
            self.bas = False 
        elif touches[pygame.K_RIGHT] :
            self.x += self.vitesse
            self.gauche = False
            self.droite = True 
            self.haut = False
            self.bas = False
        elif touches[pygame.K_UP] : 
            self.y -= self.vitesse 
            self.gauche = False
            self.droite = False 
            self.haut = True
            self.bas = False
        elif touches[pygame.K_DOWN] : 
            self.y += self.vitesse
            self.gauche = False
            self.droite = False 
            self.haut = False
            self.bas = True
        else : 
            self.gauche = False
            self.droite = False 
            self.haut = False
            self.bas = False
    

    def update(self,touches) : 

        self.deplacer(touches)

        #Gestion de l'animation 
        if self.gauche : 
            #Animation pour la gauche 
            self.frameIndex = 0 #Utiliser l'image 0
        elif self.droite : 
            self.frameIndex = 1 
        elif self.haut : 
            self.frameIndex = 2
        elif self.bas : 
            self.frameIndex = 3 


    def dessiner(self,ecran) :

        #Afficher l'image actuelle 
        ecran.blit(self.frames[self.frameIndex],(self.x,self.y))




