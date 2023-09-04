import pygame

import echap



def collisionObstacle(personnage,obstacle) :
        if (
        personnage.x < obstacle.x + obstacle.largeur and
        personnage.x + personnage.frames[personnage.frameIndex].get_width() > obstacle.x and
        personnage.y < obstacle.y + obstacle.longueur and
        personnage.y + personnage.frames[personnage.frameIndex].get_height() > obstacle.y
        ):
            return True  # Collision détectée
        return False

    
def update(personnage,touches) : 

        personnage.deplacer(touches)

        #Gestion de l'animation 
        if personnage.gauche : 
            #Animation pour la gauche 
            personnage.frameIndex = 0 #Utiliser l'image 0
        elif personnage.droite : 
            personnage.frameIndex = 1 
        elif personnage.haut : 
            personnage.frameIndex = 2
        elif personnage.bas : 
            personnage.frameIndex = 3 
        elif personnage.stay : 
            personnage.frameIndex = 4

