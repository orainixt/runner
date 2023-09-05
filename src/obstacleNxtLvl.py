import pygame
from obstacle import Obstacle

class zoneNxtLvl(Obstacle) : 

    """
    Classe qui permet de créer les objets permettant au joueur d'avancer dans les niveaux

    Args :
        x (int) la position x
        y (int) la position y
        largeur (int)
        longueur (int)
    """
    def __init__(self,x,y,largeur,longueur) :
        self.x = x 
        self.y = y 
        self.largeur = largeur
        self.longueur = longueur
        self.rect = pygame.Rect(x, y, largeur, longueur)
    
    def dessiner(self,ecran) : 
        """
        Méthode permettant de dessiner l'obstacle correspondant 
        """
        pass

    def collision_personnage(self, personnage):
        return self.rect.colliderect(personnage.rect)


        