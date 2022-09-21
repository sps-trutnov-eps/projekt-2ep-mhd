import sys
import pygame
import random

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 1920, 1080
cerna = (0,0,0)
bila = (255,255,255)
ruzova = (199,21,133)
hneda = (139,69,19)
BARVA_POZADI = cerna

#rozměry pro nepřátele
w_nepratele = 50
h_nepratele = 50
x_nepritele = 260
mezera_mezi_neprateli = 100
y_prvni_rady = 100
y_druhe_rady = 200
y_treti_rady = 300

#rozmery zizaly
velikost_zizaly = 50
barva_zizaly = (ruzova)

zizala_w = 935
zizala_h = 980
zizala_x = velikost_zizaly
zizala_y = velikost_zizaly

#rozmery hliny
sirka_spodni_hliny = 1920
vyska_spodni_hliny = 50
barva_spodni_hliny = (hneda)

spodni_hlina_w = 0
spodni_hlina_h = 1030
spodni_hlina_x = sirka_spodni_hliny
spodni_hlina_y = vyska_spodni_hliny


sirka_vrchni_hliny = 1920
vyska_vrchni_hliny = 50
barva_vrchni_hliny = (hneda)

vrchni_hlina_w = 0
vrchni_hlina_h = 850
vrchni_hlina_x = sirka_vrchni_hliny
vrchni_hlina_y = vyska_vrchni_hliny


sirka_leve_hliny = 50
vyska_leve_hliny = 300
barva_leve_hliny = (hneda)

leva_hlina_w = 0
leva_hlina_h = 900
leva_hlina_x = sirka_leve_hliny
leva_hlina_y = vyska_leve_hliny


sirka_prave_hliny = 50
vyska_prave_hliny = 300
barva_prave_hliny = (hneda)

prava_hlina_w = 1870
prava_hlina_h = 900
prava_hlina_x = sirka_prave_hliny
prava_hlina_y = vyska_prave_hliny


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
        if u.type == pygame.KEYDOWN:
            
            if u.key == pygame.K_RIGHT:
                zizala_w = zizala_w + 50
            if u.key == pygame.K_LEFT:
                zizala_w = zizala_w - 50
    
    stisknuto = pygame.key.get_pressed()
    if stisknuto[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
        
        
        
        
    okno.fill(BARVA_POZADI)
    #1. rada nepratel
    pygame.draw.rect(okno, bila, nepritel1)
    pygame.draw.rect(okno, bila, nepritel2)
    pygame.draw.rect(okno, bila, nepritel3)
    pygame.draw.rect(okno, bila, nepritel4)
    pygame.draw.rect(okno, bila, nepritel5)
    pygame.draw.rect(okno, bila, nepritel6)
    pygame.draw.rect(okno, bila, nepritel7)
    pygame.draw.rect(okno, bila, nepritel8)
    pygame.draw.rect(okno, bila, nepritel9)
    pygame.draw.rect(okno, bila, nepritel10)
    #2. rada nepratel
    pygame.draw.rect(okno, bila, nepritel11)
    pygame.draw.rect(okno, bila, nepritel12)
    pygame.draw.rect(okno, bila, nepritel13)
    pygame.draw.rect(okno, bila, nepritel14)
    pygame.draw.rect(okno, bila, nepritel15)
    pygame.draw.rect(okno, bila, nepritel16)
    pygame.draw.rect(okno, bila, nepritel17)
    pygame.draw.rect(okno, bila, nepritel18)
    pygame.draw.rect(okno, bila, nepritel19)
    pygame.draw.rect(okno, bila, nepritel20)
    #3.rada nepratel
    pygame.draw.rect(okno, bila, nepritel21)
    pygame.draw.rect(okno, bila, nepritel22)
    pygame.draw.rect(okno, bila, nepritel23)
    pygame.draw.rect(okno, bila, nepritel24)
    pygame.draw.rect(okno, bila, nepritel25)
    pygame.draw.rect(okno, bila, nepritel26)
    pygame.draw.rect(okno, bila, nepritel27)
    pygame.draw.rect(okno, bila, nepritel28)
    pygame.draw.rect(okno, bila, nepritel29)
    pygame.draw.rect(okno, bila, nepritel30)
    #zizala
    pygame.draw.rect(okno, barva_zizaly,(zizala_w, zizala_h, zizala_x, zizala_y))
    #hlina
    pygame.draw.rect(okno, barva_spodni_hliny,(spodni_hlina_w, spodni_hlina_h, spodni_hlina_x, spodni_hlina_y))
    pygame.draw.rect(okno, barva_vrchni_hliny,(vrchni_hlina_w, vrchni_hlina_h, vrchni_hlina_x, vrchni_hlina_y))
    pygame.draw.rect(okno, barva_leve_hliny,(leva_hlina_w, leva_hlina_h, leva_hlina_x, leva_hlina_y))
    pygame.draw.rect(okno, barva_prave_hliny,(prava_hlina_w, prava_hlina_h, prava_hlina_x, prava_hlina_y))
    
    
    
    
    pygame.display.update()
    

