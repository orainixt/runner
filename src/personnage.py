import pygame
import sys
import os 
from obstacle import Obstacle

class Personnage : 

    """
    Classe représentant le personnage, respresenté par un stickman 

    Attributes : 
        x (int) la coordonée x du personnage
        y (int) la coordonée y du personnage
        velY (int) la velocité de la gravité 
        sol (int) hauteur (en px) du sol du niveau 
        solTrue (bool) indicateur si le personnage touche le sol 
        frames ([]) liste d'images pour l'animation 
        frameIndex (int) index de l'adresse actuelle 
        animationSpeed (int) vitesse de l'animation (optionnal)
        vitesse (int) vitesse de déplacement du personnage
        gauche (bool) si le perso va a gauche
        droite (bool) si le perso va a droite
        haut (bool) si le perso va en haut
        bas (bool) si le perso va en bas
        stay (bool) si le perso reste immobile
        rect (pygame.Rect) est le rectangle qui encadre le personnage (utilisé pour la fin des niveaux)
    """

    GRAVITE = 1

    def __init__(self, x ,y) : 
        self.x = x
        self.y = y
        self.velY = 0
        self.sol = 550 
        self.solTrue = False 
        self.frames = [] 
        self.frameIndex = 0 
        self.animationSpeed = 10
        self.vitesse = 5
        self.gauche = False 
        self.droite = False
        self.haut = False
        self.bas = False 
        self.stay = True
        self.rect = pygame.Rect(x,y,120,120)

        #Charger les images de l'animation 
        dossierActuel = os.path.dirname(__file__)
        stickmanLeftPath = os.path.join(dossierActuel, "..", "ressources","personnage","goingLeft.png")
        stickmanRightPath = os.path.join(dossierActuel, "..", "ressources","personnage","goingRight.png")
        stickmanUpPath = os.path.join(dossierActuel, "..", "ressources","personnage","jumping.png")
        stickmanDownPath = os.path.join(dossierActuel, "..", "ressources","personnage","crawling.png")
        stickmanWaitPath = os.path.join(dossierActuel, "..", "ressources","personnage","notMoving.png")
        
        self.frames.append(pygame.image.load(stickmanLeftPath))
        self.frames.append(pygame.image.load(stickmanRightPath))
        self.frames.append(pygame.image.load(stickmanUpPath))
        self.frames.append(pygame.image.load(stickmanDownPath))
        self.frames.append(pygame.image.load(stickmanWaitPath))


    def sauter(self) : 
        """
        Methode permettant au personnage de sauter 

        Args : 
            self (Personnage) le personnage concerné 
        """
        if self.solTrue : 
            self.velY = -20
            self.solTrue = False
            
    def dessiner(self,ecran) :
        """
        Méthode permettant de dessiner le personnage sur l'ecran en fonction de l'image d'animation actuelle

        Args : 
            self (Personnage) le personnage concerné 
            ecran (pygame.display) l'ecran de jeu concerné 
        """
        #Afficher l'image actuelle 
        ecran.blit(self.frames[self.frameIndex],(self.x,self.y))

    def deplacer(self,touches) : 
        """
        Méthode permettant de déplacer le personnage en fonction de la touche appuyée

        Args : 
            self (Personnage) le personnage concerné 
            touches ([]) contenant la touche pressée  
        """
        if touches[pygame.K_LEFT] : 

            self.x -= self.vitesse
            self.gauche = True
            self.droite = False 
            self.haut = False
            self.bas = False 
            self.stay = False

        elif touches[pygame.K_RIGHT] :

            self.x += self.vitesse
            self.gauche = False
            self.droite = True 
            self.haut = False
            self.bas = False
            self.stay = False

        elif (touches[pygame.K_SPACE] or touches[pygame.K_UP]): 

            self.sauter()
            self.gauche = False
            self.droite = False 
            self.haut = True
            self.bas = False
            self.stay = False

        elif touches[pygame.K_DOWN] : 

            self.y += self.vitesse
            self.gauche = False
            self.droite = False 
            self.haut = False
            self.bas = True
            self.stay = False

        else : 
            self.gauche = False
            self.droite = False 
            self.haut = False
            self.bas = False
            self.stay = True
        
        self.velY += self.GRAVITE
        self.y += self.velY
        
        if self.y > self.sol: 
            self.y = self.sol 
            self.solTrue = True
            self.velY = 0

    def update(self,touches) :    
        """
        Méthode appelée à chaque tour de la boucle principale du jeu, permettant de déplacer le joueur 
        et de choisir quelle frame d'animation utiliser (dossier "/ressources")

        Args : 
            self (Personnage) le joueur 
            touches ([pygame.K]) le tableau de touches
        """
        self.deplacer(touches)

        #Gestion de l'animation 
        if self.gauche : 
            #Animation pour la gauche 
            self.frameIndex = 0 #Utiliser l'image 0
        elif self.droite : 
            self.frameIndex = 1 
        elif self.haut : 
            self.frameIndex = 2
        elif self.bas : 
            self.frameIndex = 3 
        elif self.stay : 
            self.frameIndex = 4

    def collisionObstacle(self,obstacle) :
        """
        Méthode permettant de gérer la collision entre deux objets 

        Args : 
            self (Personnage) le joueur, il doit avoir des arguments x et y
                                    il doit également avoir un tableau de frames correponsand aux animations
            obstacle (Obstacle) l'obstacle, il doit aussi avoir des arguments x et y

        """
        if (
        self.x < obstacle.x + obstacle.largeur and
        self.x + self.frames[self.frameIndex].get_width() > obstacle.x and
        self.y < obstacle.y + obstacle.longueur and
        self.y + self.frames[self.frameIndex].get_height() > obstacle.y
        ):
            return True  # Collision détectée
        return False
