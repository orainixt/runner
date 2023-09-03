import pygame 
import os

class Obstacle : 
    
    def __init__(self,x,y,imagePath) : 

        dossierActuel = os.path.dirname(__file__)

        self.x = x 
        self.y = y
        imagePathComplet = os.path.join(dossierActuel,imagePath)
        self.image = pygame.image.load(imagePathComplet)
        self.largeur = self.image.get_width()
        self.longueur = self.image.get_height()
        
        
    def dessiner(self,ecran) : 
        ecran.blit(self.image,(self.x,self.y))