import pygame 
import os

class Obstacle : 
    """
    Classe obstacle : Elle permet de créer un obstacle en fonction de ses coordonées et de son image référente

    Attributes : 
        x (int) la coordonée x 
        y (int) la coordonée y 
        image (pygame.image) image correspondant a l'obstacle 
        largeur (int) 
    """
    def __init__(self,x,y,imagePath) : 

        dossierActuel = os.path.dirname(__file__)

        self.x = x 
        self.y = y
        imagePathComplet = os.path.join(dossierActuel,imagePath)
        self.image = pygame.image.load(imagePathComplet)
        self.largeur = self.image.get_width()
        self.longueur = self.image.get_height()
    
        
    def dessiner(self,ecran) : 

        """
        Méthode permettant de dessiner l'obstacle sur l'ecran en fonction de l'image importée 

        Args : 
            self (Obstacle) l'obstacle concerné 
            ecran (pygame.display) l'ecran de jeu concerné 
        """
        ecran.blit(self.image,(self.x,self.y))