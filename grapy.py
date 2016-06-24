import os,sys
import pygame

ROJO=(255,0,0)
BLANCO=(255,255,255)
NEGRO=(0,0,0)
ANCHO=1000
ALTO=600

class Vertice(pygame.sprite.Sprite):
        
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.click = False
            self.sel=False
            #Necesario para conocer si se esta trazando arco
            self.arco=False
            self.conexos=[]
            self.grado=len(self.conexos)
            self.id=0
            self.img1=pygame.image.load('grapy/img/vminb.png').convert_alpha()
            self.img2=pygame.image.load('grapy/img/vminr.png').convert_alpha()
            self.image = self.img1
            self.rect = self.image.get_rect()
            
        def adArco(self, a):
            self.conexos.append(a)
            self.grado=len(self.conexos)

        def update(self, pantalla):
            if self.click:
                    self.image = self.img2
                    self.rect = self.image.get_rect() 
                    self.rect.center = pygame.mouse.get_pos()
            else:
                self.image = self.img1
                #self.rect = self.image.get_rect()
                
            if self.arco:
                self.image = self.img2
            else:
                self.image = self.img1
                
            fuente = pygame.font.Font(None, 28)
            texto = fuente.render(str(self.grado), 0, NEGRO)
            if self.rect.x > 55:                
                pantalla.blit(self.image,self.rect)
                pantalla.blit(texto, (self.rect.x-8,self.rect.y-10))
            else:
                self.rect.x=56
                pantalla.blit(self.image,self.rect)
                

class Arco():
        
        def __init__(self):
            self.v1=Vertice()
            self.v2=Vertice()
            self.color=NEGRO
     
        def AdVertices(self,v1, v2):
            self.v1=v1
            self.v2=v2
            
        def defColor(self, c):
            self.color=c
            
        def update(self, pantalla):
            pygame.draw.line(pantalla,NEGRO,self.v1.rect.center, self.v2.rect.center,1)
            
            
        

def seleccion(pantalla, op):
    if op == 1:
       vb=pygame.image.load('grapy/img/vbsel.png').convert_alpha()    
       pantalla.blit(vb,(5,10))
       vb=pygame.image.load('grapy/img/ab.png').convert_alpha()    
       pantalla.blit(vb,(5,60))
       vb=pygame.image.load('grapy/img/apn.png').convert_alpha()    
       pantalla.blit(vb,(5,110))
    if op == 2:
       vb=pygame.image.load('grapy/img/vb.png').convert_alpha()    
       pantalla.blit(vb,(5,10))
       vb=pygame.image.load('grapy/img/absel.png').convert_alpha()    
       pantalla.blit(vb,(5,60))
       vb=pygame.image.load('grapy/img/apn.png').convert_alpha()    
       pantalla.blit(vb,(5,110))
    if op == 3:
       vb=pygame.image.load('grapy/img/vb.png').convert_alpha()    
       pantalla.blit(vb,(5,10))
       vb=pygame.image.load('grapy/img/ab.png').convert_alpha()    
       pantalla.blit(vb,(5,60))
       vb=pygame.image.load('grapy/img/apnsel.png').convert_alpha()    
       pantalla.blit(vb,(5,110))
    


def Principal(pantalla,v,op):
        #Captura de teclas
        v, op=Lienzo(pantalla,v, op)
        pantalla.fill(BLANCO)
        seleccion(pantalla, op)
        v.update(pantalla)
        #print len(v)
        return v
        
def Lienzo(pantalla, lista, lsarcos, op):
        nop=op
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y=event.pos
                #print event.pos
                if op == 1 or op==3:
                   for ve in lista:
                       if ve.rect.collidepoint(event.pos):
                          ve.click = True
                          ve.sel=True
                          ve.rect.center = pygame.mouse.get_pos()
                                
                if op==2:
                   for ve in lista:
                       if ve.rect.collidepoint(event.pos):
                          if ve.arco:
                             ve.arco=False
                          else:
                             ve.arco = True
                          
                          print ve.id, ' ', ve.arco
                                
                if (x<=55) and (y>=0 and y<=55):
                     # Nuevo vertice
                     nop=1
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
                                  
                                  
                if (x<=55) and (y>55 and y<=110):
                     #opcion 2 Crear arco
                     nop=2                            
                     
                                
                if (x<=55) and (y>110 and y<=160):
                     #opcion 3 apuntador
                     nop=3
                     

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
                
                           
                #verificamos si hay arco
                con=0
                for v in lista:
                    if v.arco:
                        con+=1
                if con==2:
                    ps=[]
                    for v in lista:
                        if v.arco:
                           v.arco=False
                           v.sel=False
                           ps.append(v)
                           print 'sel: ', v.id, v.rect.center
                    if ps[0].id != ps[1].id:
                       print 'no circular' 
                       a=Arco()
                       a.AdVertices(ps[0],ps[1])
                       lsarcos.append(a)
                       for p in ps:
                         for v in lista:
                             if v.id == p.id:
                                v.adArco(p)
                        
                    print len(lsarcos)  
                        
                
            elif event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
        
            #print nop
        return lista, lsarcos, nop


#Modo edicion de grafo
def Editar():
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pantalla = pygame.display.set_mode((ANCHO, ALTO))
        reloj = pygame.time.Clock()
        vertices=pygame.sprite.Group()
        arcos=[]
        op=1
        '''
        v = Vertice()
        v.rect.center = pantalla.get_rect().center
        v.sel=True
        vertices.add(v)
        '''
        while 1:
            #vertices=Principal(pantalla,vertices, op)
            v, arcos, op=Lienzo(pantalla,vertices, arcos, op)
            pantalla.fill(BLANCO)
            seleccion(pantalla, op)            
            for a in arcos:
                a.update(pantalla)
            v.update(pantalla)
            pygame.display.update()
        #construimos arreglo de vertices y arcos para trabajo
        
        return vertices, arcos


