from abc import ABC, abstractmethod

import pygame 
import os

class Obstacle(ABC) : 

    """
    Classe obstacle : Elle permet de créer un obstacle en fonction de ses coordonées et de son image référente

    Attributes : 
        x (int) la coordonée x 
        y (int) la coordonée y 
        image (pygame.image) image correspondant a l'obstacle 
        largeur (int) 
    """
        
    @abstractmethod

    def __init__(self,x,y) :
        self.x = x 
        self.y = y
    
    @property
    @abstractmethod    
    def dessiner(self,ecran) : 
        """
        Méthode permettant de dessiner l'obstacle sur l'ecran en fonction de l'image importée 

        Args : 
            self (Obstacle) l'obstacle concerné 
            ecran (pygame.display) l'ecran de jeu concerné 
        """
        pass