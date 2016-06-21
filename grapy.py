import os,sys
import pygame 

ROJO=(255,0,0)
BLANCO=(255,255,255)

class Vertice(pygame.sprite.Sprite):
        
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.click = False
            self.img1=pygame.image.load('img/vminb.png').convert_alpha()
            self.img2=pygame.image.load('img/vminr.png').convert_alpha()
            self.image = self.img1
            self.rect = self.image.get_rect()

        def update(self,surface):
            if self.click:
                self.image = self.img2
                self.rect = self.image.get_rect() 
                self.rect.center = pygame.mouse.get_pos()
            else:
                self.image = self.img1
                #self.rect = self.image.get_rect()
            if self.rect.x > 55:
               surface.blit(self.image,self.rect)
            else:
                self.rect.x=55
                surface.blit(self.image,self.rect)
                

def seleccion(pantalla):
    vb=pygame.image.load('img/vb.png').convert_alpha()    
    pantalla.blit(vb,(5,10))
    

<<<<<<< HEAD
=======
def main(pantalla,v):
        #Captura de teclas
        Lienzo(v)
        pantalla.fill(BLANCO)
        seleccion(pantalla)
        v.update(pantalla)
>>>>>>> 271dcfaaf80f7718cea687af06fcff824cbd31e4
        
def Lienzo(cuadro):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y=event.pos
                if cuadro.rect.collidepoint(event.pos):
                    cuadro.click = True
                elif x<=55 and y<=55:
                    print 'nuevo'
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                cuadro.click = False
            elif event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

<<<<<<< HEAD
=======
if __name__ == "__main__":
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pantalla = pygame.display.set_mode((1000,600))
        reloj = pygame.time.Clock()
        vertices=pygame.sprite.Group()
        v = Vertice()
        v.rect.center = pantalla.get_rect().center
        while 1:
            main(pantalla,v)
            pygame.display.update()
>>>>>>> 271dcfaaf80f7718cea687af06fcff824cbd31e4
