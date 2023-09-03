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

def deplacer(personnage,touches) : 

        if touches[pygame.K_LEFT] : 

            personnage.x -= personnage.vitesse
            personnage.gauche = True
            personnage.droite = False 
            personnage.haut = False
            personnage.bas = False 
            personnage.stay = False

        elif touches[pygame.K_RIGHT] :

            personnage.x += personnage.vitesse
            personnage.gauche = False
            personnage.droite = True 
            personnage.haut = False
            personnage.bas = False
            personnage.stay = False

        elif touches[pygame.K_SPACE] : 

            personnage.sauter()
            personnage.gauche = False
            personnage.droite = False 
            personnage.haut = True
            personnage.bas = False
            personnage.stay = False

        elif touches[pygame.K_DOWN] : 

            personnage.y += personnage.vitesse
            personnage.gauche = False
            personnage.droite = False 
            personnage.haut = False
            personnage.bas = True
            personnage.stay = False
        
        elif touches[pygame.K_ESCAPE] : 
            print("Keypressed")
            escapeWindow = Echap()
            escapeWindow.executer()

        else : 
            personnage.gauche = False
            personnage.droite = False 
            personnage.haut = False
            personnage.bas = False
            personnage.stay = True
        
        personnage.velY += personnage.GRAVITE
        personnage.y += personnage.velY
        
        if personnage.y > personnage.sol: 
            personnage.y = personnage.sol 
            personnage.solTrue = True
            personnage.velY = 0
    
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


def sauter(self,personnage) : 
        
        if personnage.solTrue : 
            personnage.velY = -20
            personnage.solTrue = False