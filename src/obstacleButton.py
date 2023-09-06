import pygame 
import os


from obstacle import Obstacle

class ObstacleButton(Obstacle) : 

    def __init__(self, x, y, imagePath):
        super().__init__(x, y)

        dossierActuel = os.path.dirname(__file__)
        imagePathComplet = os.path.join(dossierActuel,imagePath)
        self.image = pygame.image.load(imagePathComplet)
        self.largeur = self.image.get_width()
        self.longueur = self.image.get_height()
        self.rect = pygame.Rect(0,0,0,0) 
    
    def dessiner(self,ecran) :
        ecran.blit(self.image,(self.x,self.y))
        self.rect = pygame.Rect(self.x,self.y,self.largeur,self.longueur)
    
    def collision_point(self, pos):
        return self.rect.collidepoint(pos)