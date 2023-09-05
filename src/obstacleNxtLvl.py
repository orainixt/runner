import pygame
import os

from obstacle import Obstacle


class ObstacleNxtLvl(Obstacle) : 

    """
    Classe qui permet de créer les objets permettant au joueur d'avancer dans les niveaux

    Args :
        x (int) la position x
        y (int) la position y
        largeur (int)
        longueur (int)
    """
    def __init__(self,x,y,imagePath) :
        self.x = x 
        self.y = y 

        dossierActuel = os.path.dirname(__file__)
        imagePathComplet = os.path.join(dossierActuel,imagePath)
        self.image = pygame.image.load(imagePathComplet)
        self.largeur = self.image.get_width()
        self.longueur = self.image.get_height()

    
    def dessiner(self,ecran) : 
        """
        Méthode permettant de dessiner l'obstacle correspondant 
        """
        ecran.blit(self.image,(self.x,self.y))

    def collision_personnage(self, personnage):
        return self.rect.colliderect(personnage.rect)


        