import os,sys
import pygame

ROJO=(255,0,0)
BLANCO=(255,255,255)
ANCHO=1000
ALTO=600

class Vertice(pygame.sprite.Sprite):
        
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.click = False
            self.sel=False
            self.id=0
            self.img1=pygame.image.load('grapy/img/vminb.png').convert_alpha()
            self.img2=pygame.image.load('grapy/img/vminr.png').convert_alpha()
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
    vb=pygame.image.load('grapy/img/vb.png').convert_alpha()    
    pantalla.blit(vb,(5,10))
    vb=pygame.image.load('grapy/img/ab.png').convert_alpha()    
    pantalla.blit(vb,(5,60))
    


def Principal(pantalla,v):
        #Captura de teclas
        v=Lienzo(pantalla,v)
        pantalla.fill(BLANCO)
        seleccion(pantalla)
        v.update(pantalla)
        #print len(v)
        return v
        
def Lienzo(pantalla, lista):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y=event.pos
                for ve in lista:
                        if ve.rect.collidepoint(event.pos):
                                ve.click = True
                                ve.sel=True
                                #ve.rect.center = pygame.mouse.get_pos()
                                
                if x<=55 and y<=55:
                     # Nuevo vertice
                     v = Vertice()
                     #v.rect.center = pantalla.get_rect().center
                     v.rect.center = (55,50)
                     v.id=len(lista)
                     lista.add(v)
                     col=True
                     while col:
                           col=False
                           colision=pygame.sprite.spritecollide(v, lista, False)
                           for e in colision:
                               if v.id != e.id:
                                  v.rect.left = e.rect.right
                                  col=True
                     
                     #lista.add(v)
                     
                     
                
            elif event.type == pygame.MOUSEBUTTONUP:
                for ve in lista:
                    if ve.sel==True:
                        colision=pygame.sprite.spritecollide(ve, lista, False)
                        for e in colision:
                            if ve != e:
                               ve.rect.left = e.rect.right
                               if ve.rect.x >= ANCHO:
                                  ve.rect.right = e.rect.left
                        ve.click=False
                        ve.sel=False
            elif event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
                
        #colision=pygame.sprite.spritecollide(player, block_list, True)
        return lista


def Pantalla():
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pantalla = pygame.display.set_mode((ANCHO, ALTO))
        reloj = pygame.time.Clock()
        vertices=pygame.sprite.Group()
        '''
        v = Vertice()
        v.rect.center = pantalla.get_rect().center
        v.sel=True
        vertices.add(v)
        '''
        while 1:
            vertices=Principal(pantalla,vertices)
            pygame.display.update()
