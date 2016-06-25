import os,sys
import pygame
import inputbox

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
            self.lscon=[]
            self.grado=len(self.conexos)
            self.id=0
            self.img1=pygame.image.load('grapy/img/vminb.png').convert_alpha()
            self.img2=pygame.image.load('grapy/img/vminr.png').convert_alpha()
            self.image = self.img1
            self.rect = self.image.get_rect()
            
        def adArco(self, a):
            self.conexos.append(a)
            self.grado=len(self.conexos)
            v=V()
            v.id=self.id
            v.grado=self.grado
            v.arcos.append((v.id,a.id))
            self.lscon.append(v)
            
        def retArcos(self):
            return self.conexos   

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
            self.peso=0
            
     
        def AdVertices(self,v1, v2):
            self.v1=v1
            self.v2=v2
            self.arco=[v1.id, v2.id]
            
        def defColor(self, c):
            self.color=c
            
        def pmedio(self, p1,p2):
            x1=p1[0]
            y1=p1[1]
            x2=p2[0]
            y2=p2[1]
            sx=abs(x1-x2)/2
            sy=abs(y1-y2)/2
            if x1<x2:
               px=x1+sx
            else:
               px=x2+sx
            if y1<y2:
               py=y1+sy
            else:
               py=y2+sy
            p=(px,py)
            return p
            
        def update(self, pantalla):
            fuente = pygame.font.Font(None, 28)
            texto = fuente.render(str(self.peso), 0, NEGRO)
            pygame.draw.line(pantalla,NEGRO,self.v1.rect.center, self.v2.rect.center,1)
            p=self.pmedio(self.v1.rect.center, self.v2.rect.center)
            pantalla.blit(texto, p)


      
class V():
        def __init__(self):
           self.id=0
           self.grado=0
           self.arcos=[]
         
class E():
        def __init__(self):
           self.e=[]
           

        

def seleccion(pantalla, op):
    if op == 1:
       vb=pygame.image.load('grapy/img/vbsel.png').convert_alpha()    
       pantalla.blit(vb,(5,10))
       vb=pygame.image.load('grapy/img/ab.png').convert_alpha()    
       pantalla.blit(vb,(5,60))
       vb=pygame.image.load('grapy/img/apb.png').convert_alpha()    
       pantalla.blit(vb,(5,110))
       vb=pygame.image.load('grapy/img/apn.png').convert_alpha()    
       pantalla.blit(vb,(5,160))
    if op == 2:
       vb=pygame.image.load('grapy/img/vb.png').convert_alpha()    
       pantalla.blit(vb,(5,10))
       vb=pygame.image.load('grapy/img/absel.png').convert_alpha()    
       pantalla.blit(vb,(5,60))
       vb=pygame.image.load('grapy/img/apb.png').convert_alpha()    
       pantalla.blit(vb,(5,110))
       vb=pygame.image.load('grapy/img/apn.png').convert_alpha()    
       pantalla.blit(vb,(5,160))
    if op == 3:
       vb=pygame.image.load('grapy/img/vb.png').convert_alpha()    
       pantalla.blit(vb,(5,10))
       vb=pygame.image.load('grapy/img/ab.png').convert_alpha()    
       pantalla.blit(vb,(5,60))
       vb=pygame.image.load('grapy/img/apbsel.png').convert_alpha()    
       pantalla.blit(vb,(5,110))
       vb=pygame.image.load('grapy/img/apn.png').convert_alpha()    
       pantalla.blit(vb,(5,160))
    if op == 5:
       vb=pygame.image.load('grapy/img/vb.png').convert_alpha()    
       pantalla.blit(vb,(5,10))
       vb=pygame.image.load('grapy/img/ab.png').convert_alpha()    
       pantalla.blit(vb,(5,60))
       vb=pygame.image.load('grapy/img/apb.png').convert_alpha()    
       pantalla.blit(vb,(5,110))
       vb=pygame.image.load('grapy/img/apnsel.png').convert_alpha()    
       pantalla.blit(vb,(5,160))
    


        
def Lienzo(pantalla, lista, lsarcos, op, fin):
        nop=op
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y=event.pos
                #print event.pos
                if op == 1 or op==5:
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
                             
                if op==3:
                   for ve in lista:
                       if ve.rect.collidepoint(event.pos):
                          if ve.arco:
                             ve.arco=False
                          else:
                             ve.arco = True
                   
                   
                          
                                
                if (x<=55) and (y>=0 and y<=55):
                     # Nuevo vertice
                     nop=1
                     v = Vertice()
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
                     
                if (x<=55) and (y>160 and y<=210):
                     #opcion 3 apuntador
                     nop=5
                     

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
                    if ps[0].id != ps[1].id:
                       a=Arco()
                       a.AdVertices(ps[0],ps[1])
                       if op==3:
                          inp = inputbox.ask(pantalla, 'Peso ')
                          if len(inp)==0:
                             a.peso=0
                          else:      
                             a.peso=int(inp)
                          #print type(inp)
                       lsarcos.append(a)
                       for p in ps:
                         for v in lista:
                             if v.id == p.id:
                                v.adArco(p)
                    #print len(lsarcos)       
                
            elif event.type == pygame.QUIT:
                fin=True
        
            #print nop
        return lista, lsarcos, nop, fin


def ListaVertices(lista):
        vl=[]
        for v in lista:
            vl.append(v.id)
        return vl

def ListaArcos(lista):
        al=[]
        for a in lista:
            arco=a.arco
            al.append(arco)
        return al

def ResumenV(l):
    lv=[]
    for v in l:
        #lista de vertices conexos
        lcon=v.lscon
        '''
        for e in lcon:
            print e.id
        '''
        lv.append(v.id)
    return lv

#Modo edicion de grafo
def Editar():
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pantalla = pygame.display.set_mode((ANCHO, ALTO))
        reloj = pygame.time.Clock()
        vertices=pygame.sprite.Group()
        arcos=[]
        op=1
        fin =False
        while not fin:
            #vertices=Principal(pantalla,vertices, op)
            vertices, arcos, op, fin=Lienzo(pantalla,vertices, arcos, op, fin)
            pantalla.fill(BLANCO)
            seleccion(pantalla, op)            
            for a in arcos:
                a.update(pantalla)
            vertices.update(pantalla)
            pygame.display.update()
        #construimos arreglo de vertices y arcos para trabajo
        lv=ResumenV(vertices)
        return vertices, arcos


