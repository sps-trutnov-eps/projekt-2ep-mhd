import sys
import pygame
import random

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 1920, 1080
BARVA_POZADI = 255, 255, 255

#Rozměry pro nepřátele
w_nepratele = 50
h_nepratele = 50
x_nepritele = 260
mezera_mezi_neprateli = 100
y_prvni_rady = 100
y_druhe_rady = 200
y_treti_rady = 300

#cerna
cerna = (0,0,0)

#nepratele - 1.rada
nepritel1 = (x_nepritele,y_prvni_rady,w_nepratele,h_nepratele)
nepritel2 = (x_nepritele + w_nepratele +   mezera_mezi_neprateli,y_prvni_rady,w_nepratele,h_nepratele)
nepritel3 = (x_nepritele + 2*w_nepratele + 2*mezera_mezi_neprateli,y_prvni_rady,w_nepratele,h_nepratele)
nepritel4 = (x_nepritele + 3*w_nepratele + 3*mezera_mezi_neprateli,y_prvni_rady,w_nepratele,h_nepratele)
nepritel5 = (x_nepritele + 4*w_nepratele + 4*mezera_mezi_neprateli,y_prvni_rady,w_nepratele,h_nepratele)
nepritel6 = (x_nepritele + 5*w_nepratele + 5*mezera_mezi_neprateli,y_prvni_rady,w_nepratele,h_nepratele)
nepritel7 = (x_nepritele + 6*w_nepratele + 6*mezera_mezi_neprateli,y_prvni_rady,w_nepratele,h_nepratele)
nepritel8 = (x_nepritele + 7*w_nepratele + 7*mezera_mezi_neprateli,y_prvni_rady,w_nepratele,h_nepratele)
nepritel9 = (x_nepritele + 8*w_nepratele + 8*mezera_mezi_neprateli,y_prvni_rady,w_nepratele,h_nepratele)
nepritel10 = (x_nepritele + 9*w_nepratele + 9*mezera_mezi_neprateli,y_prvni_rady,w_nepratele,h_nepratele)

#nepratele - 2.rada
nepritel11 = (x_nepritele,y_druhe_rady,w_nepratele,h_nepratele)
nepritel12 = (x_nepritele + w_nepratele + mezera_mezi_neprateli,y_druhe_rady,w_nepratele,h_nepratele)
nepritel13 = (x_nepritele + 2*w_nepratele + 2*mezera_mezi_neprateli,y_druhe_rady,w_nepratele,h_nepratele)
nepritel14 = (x_nepritele + 3*w_nepratele + 3*mezera_mezi_neprateli,y_druhe_rady,w_nepratele,h_nepratele)
nepritel15 = (x_nepritele + 4*w_nepratele + 4*mezera_mezi_neprateli,y_druhe_rady,w_nepratele,h_nepratele)
nepritel16 = (x_nepritele + 5*w_nepratele + 5*mezera_mezi_neprateli,y_druhe_rady,w_nepratele,h_nepratele)
nepritel17 = (x_nepritele + 6*w_nepratele + 6*mezera_mezi_neprateli,y_druhe_rady,w_nepratele,h_nepratele)
nepritel18 = (x_nepritele + 7*w_nepratele + 7*mezera_mezi_neprateli,y_druhe_rady,w_nepratele,h_nepratele)
nepritel19 = (x_nepritele + 8*w_nepratele + 8*mezera_mezi_neprateli,y_druhe_rady,w_nepratele,h_nepratele)
nepritel20 = (x_nepritele + 9*w_nepratele + 9*mezera_mezi_neprateli,y_druhe_rady,w_nepratele,h_nepratele)

#nepratele - 3.rada
nepritel21 = (x_nepritele,y_treti_rady,w_nepratele,h_nepratele)
nepritel22 = (x_nepritele + w_nepratele + mezera_mezi_neprateli,y_treti_rady,w_nepratele,h_nepratele)
nepritel23 = (x_nepritele + 2*w_nepratele + 2*mezera_mezi_neprateli,y_treti_rady,w_nepratele,h_nepratele)
nepritel24 = (x_nepritele + 3*w_nepratele + 3*mezera_mezi_neprateli,y_treti_rady,w_nepratele,h_nepratele)
nepritel25 = (x_nepritele + 4*w_nepratele + 4*mezera_mezi_neprateli,y_treti_rady,w_nepratele,h_nepratele)
nepritel26 = (x_nepritele + 5*w_nepratele + 5*mezera_mezi_neprateli,y_treti_rady,w_nepratele,h_nepratele)
nepritel27 = (x_nepritele + 6*w_nepratele + 6*mezera_mezi_neprateli,y_treti_rady,w_nepratele,h_nepratele)
nepritel28 = (x_nepritele + 7*w_nepratele + 7*mezera_mezi_neprateli,y_treti_rady,w_nepratele,h_nepratele)
nepritel29 = (x_nepritele + 8*w_nepratele + 8*mezera_mezi_neprateli,y_treti_rady,w_nepratele,h_nepratele)
nepritel30 = (x_nepritele + 9*w_nepratele + 9*mezera_mezi_neprateli,y_treti_rady,w_nepratele,h_nepratele)



pygame.init()

pygame.display.set_caption('Mongol House Defense')
okno = pygame.display.set_mode(ROZLISENI_OKNA)

while True:
    udalosti = pygame.event.get()
    for u in udalosti:
        if u.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if u.type == pygame.MOUSEWHEEL:
            if u.y < 0:
                pygame.display.iconify()
    
    stisknuto = pygame.key.get_pressed()
    if stisknuto[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
        
        
        
        
    okno.fill(BARVA_POZADI)
    #1. rada nepratel
    pygame.draw.rect(okno, cerna, nepritel1)
    pygame.draw.rect(okno, cerna, nepritel2)
    pygame.draw.rect(okno, cerna, nepritel3)
    pygame.draw.rect(okno, cerna, nepritel4)
    pygame.draw.rect(okno, cerna, nepritel5)
    pygame.draw.rect(okno, cerna, nepritel6)
    pygame.draw.rect(okno, cerna, nepritel7)
    pygame.draw.rect(okno, cerna, nepritel8)
    pygame.draw.rect(okno, cerna, nepritel9)
    pygame.draw.rect(okno, cerna, nepritel10)
    #2. rada nepratel
    pygame.draw.rect(okno, cerna, nepritel11)
    pygame.draw.rect(okno, cerna, nepritel12)
    pygame.draw.rect(okno, cerna, nepritel13)
    pygame.draw.rect(okno, cerna, nepritel14)
    pygame.draw.rect(okno, cerna, nepritel15)
    pygame.draw.rect(okno, cerna, nepritel16)
    pygame.draw.rect(okno, cerna, nepritel17)
    pygame.draw.rect(okno, cerna, nepritel18)
    pygame.draw.rect(okno, cerna, nepritel19)
    pygame.draw.rect(okno, cerna, nepritel20)
    #3.rada nepratel
    pygame.draw.rect(okno, cerna, nepritel21)
    pygame.draw.rect(okno, cerna, nepritel22)
    pygame.draw.rect(okno, cerna, nepritel23)
    pygame.draw.rect(okno, cerna, nepritel24)
    pygame.draw.rect(okno, cerna, nepritel25)
    pygame.draw.rect(okno, cerna, nepritel26)
    pygame.draw.rect(okno, cerna, nepritel27)
    pygame.draw.rect(okno, cerna, nepritel28)
    pygame.draw.rect(okno, cerna, nepritel29)
    pygame.draw.rect(okno, cerna, nepritel30)
    
    
    
    
    pygame.display.update()
    

