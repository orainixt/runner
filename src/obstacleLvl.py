import pygame 
import os

from obstacle import Obstacle

class ObstacleLvl(Obstacle) : 

    def __init__(self, x, y, imagePath):
        super().__init__(x, y)

        dossierActuel = os.path.dirname(__file__)
        imagePathComplet = os.path.join(dossierActuel,imagePath)
        self.image = pygame.image.load(imagePathComplet)
        self.largeur = self.image.get_width()
        self.longueur = self.image.get_height()
    
    def dessiner(self,ecran) :
        ecran.blit(self.image,(self.x,self.y))