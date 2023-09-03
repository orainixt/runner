import pygame 

class Obstacle : 
    
    def __init__(self,x = 0,y = 0,largeur = 100, longueur = 100) : 
        self.x = x 
        self.y = y
        self.largeur = largeur
        self.longueur = longueur 
    
    def dessiner(self,fenetre) : 
        