import pygame
import sys
import os 
from obstacle import Obstacle
from echap import *

class Personnage : 

    GRAVITE = 1

    def __init__(self, x = 0,y=550) : 
        self.x = x
        self.y = y
        self.velY = 0
        self.sol = 550 #hauteur du sol 
        self.solTrue = False #indicateur si le perso touche le sol
        self.frames = [] # liste d'images pour l'animation
        self.frameIndex = 0 # index de l'image actuelle
        self.animationSpeed = 10 #vitesse de l'animation 
        self.vitesse = 5
        self.gauche = False 
        self.droite = False
        self.haut = False
        self.bas = False 
        self.stay = True

        #Charger les images de l'animation 
        dossierActuel = os.path.dirname(__file__)
        stickmanLeftPath = os.path.join(dossierActuel, "..", "ressources","goingLeft.png")
        stickmanRightPath = os.path.join(dossierActuel, "..", "ressources","goingRight.png")
        stickmanUpPath = os.path.join(dossierActuel, "..", "ressources","jumping.png")
        stickmanDownPath = os.path.join(dossierActuel, "..", "ressources","crawling.png")
        stickmanWaitPath = os.path.join(dossierActuel, "..", "ressources","notMoving.png")
        
        self.frames.append(pygame.image.load(stickmanLeftPath))
        self.frames.append(pygame.image.load(stickmanRightPath))
        self.frames.append(pygame.image.load(stickmanUpPath))
        self.frames.append(pygame.image.load(stickmanDownPath))
        self.frames.append(pygame.image.load(stickmanWaitPath))


    def dessiner(self,ecran) :

        #Afficher l'image actuelle 
        ecran.blit(self.frames[self.frameIndex],(self.x,self.y))




