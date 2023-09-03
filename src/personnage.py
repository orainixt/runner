import pygame

class Personnage : 

    def __init__(self) : 
        self.x = 0
        self.y = 0
        self.taille = 50 
        self.vitesse = 5
    
    def deplacer(self,touches) : 
        if touches[pygame.K_LEFT] : 
            self.x -= self.vitesse
        if touches[pygame.K_RIGHT] :
            self.x += self.vitesse
        if touches[pygame.K_UP] : 
            self.y -= self.vitesse 
        if touches[pygame.K_DOWN] : 
            self.y += self.vitesse
    
    def dessiner(self, fenetre) : 
        # Dessine la tête
        pygame.draw.circle(fenetre, (0, 0, 0), (self.x + self.taille // 2, self.y + self.taille // 4), self.taille // 4)

        # Dessine le corps (ligne verticale)
        pygame.draw.line(fenetre, (0, 0, 0), (self.x + self.taille // 2, self.y + self.taille // 2), (self.x + self.taille // 2, self.y + self.taille), 2)

        # Dessine les bras (lignes diagonales)
        pygame.draw.line(fenetre, (0, 0, 0), (self.x + self.taille // 2, self.y + self.taille // 2), (self.x + self.taille // 4, self.y + self.taille), 2)
        pygame.draw.line(fenetre, (0, 0, 0), (self.x + self.taille // 2, self.y + self.taille // 2), (self.x + 3 * self.taille // 4, self.y + self.taille), 2)

        # Dessine les jambes (lignes diagonales)
        pygame.draw.line(fenetre, (0, 0, 0), (self.x + self.taille // 2, self.y + self.taille), (self.x + self.taille // 4, self.y + 3 * self.taille // 2), 2)
        pygame.draw.line(fenetre, (0, 0, 0), (self.x + self.taille // 2, self.y + self.taille), (self.x + 3 * self.taille // 4, self.y + 3 * self.taille // 2), 2)
