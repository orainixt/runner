import pygame
import sys
import os 
from obstacle import Obstacle
from echap import *

class Personnage : 

    """
    Classe représentant le personnage, respresenté par un stickman 

    Attributs : 
        x (int) la coordonée x du personnage
        y (int) la coordonée y du personnage
        velY (int) la velocité de la gravité 
        sol (int) hauteur (en px) du sol du niveau 
        solTrue (bool) indicateur si le personnage touche le sol 
        frames ([]) liste d'images pour l'animation 
        frameIndex (int) index de l'adresse actuelle 
        animationSpeed (int) vitesse de l'animation (optionnal)
        vitesse (int) vitesse de déplacement du personnage
        gauche (bool) si le perso va a gauche
        droite (bool) si le perso va a droite
        haut (bool) si le perso va en haut
        bas (bool) si le perso va en bas
        stay (bool) si le perso reste immobile
    """

    GRAVITE = 1

    def __init__(self, x = 0,y=550) : 
        self.x = x
        self.y = y
        self.velY = 0
        self.sol = 550 
        self.solTrue = False 
        self.frames = [] 
        self.frameIndex = 0 
        self.animationSpeed = 10
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


    def sauter(self) : 
        """
        Methode permettant au personnage de sauter 

        Args : 
            self (Personnage) le personnage concerné 
        """
        if self.solTrue : 
            self.velY = -20
            self.solTrue = False
            
    def dessiner(self,ecran) :
        """
        Méthode permettant de dessiner le personnage sur l'ecran en fonction de l'image d'animation actuelle

        Args : 
            self (Personnage) le personnage concerné 
            ecran (pygame.display) l'ecran de jeu concerné 
        """
        #Afficher l'image actuelle 
        ecran.blit(self.frames[self.frameIndex],(self.x,self.y))

    def deplacer(self,touches) : 
        """
        Méthode permettant de déplacer le personnage en fonction de la touche appuyée

        Args : 
            self (Personnage) le personnage concerné 
            touches ([]) contenant la touche pressée  
        """
        if touches[pygame.K_LEFT] : 

            self.x -= self.vitesse
            self.gauche = True
            self.droite = False 
            self.haut = False
            self.bas = False 
            self.stay = False

        elif touches[pygame.K_RIGHT] :

            self.x += self.vitesse
            self.gauche = False
            self.droite = True 
            self.haut = False
            self.bas = False
            self.stay = False

        elif (touches[pygame.K_SPACE] or touches[pygame.K_UP]): 

            self.sauter()
            self.gauche = False
            self.droite = False 
            self.haut = True
            self.bas = False
            self.stay = False

        elif touches[pygame.K_DOWN] : 

            self.y += self.vitesse
            self.gauche = False
            self.droite = False 
            self.haut = False
            self.bas = True
            self.stay = False

        else : 
            self.gauche = False
            self.droite = False 
            self.haut = False
            self.bas = False
            self.stay = True
        
        self.velY += self.GRAVITE
        self.y += self.velY
        
        if self.y > self.sol: 
            self.y = self.sol 
            self.solTrue = True
            self.velY = 0




