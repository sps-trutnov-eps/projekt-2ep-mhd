import sys
import pygame
import random

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 1920, 1080

#barvy
cerna = (0,0,0)
bila = (255,255,255)
ruzova = (199,21,133)
hneda = (139,69,19)
seda = (128,128,128)
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
v_zizaly = 1.5

zizala_w = velikost_zizaly
zizala_h = velikost_zizaly
zizala_x = ROZLISENI_X/2 - velikost_zizaly/2
zizala_y = ROZLISENI_Y - velikost_zizaly*2

#strela
velikost_strely = 10
barva_strely = (hneda)
v_strely = 0.5

strela_w = velikost_strely
strela_h = velikost_strely
strela_x = zizala_x + zizala_w - strela_w
strela_y = zizala_y
strelba = False
sledovani = True
strela2_w = velikost_strely
strela2_x = zizala_x + zizala_w - strela2_w
strela2_y = zizala_y
strela2_h = velikost_strely
strela2 = pygame.Rect(strela2_x,strela2_y,strela2_w,strela2_h)
strelba2 = False
sledovani2 = True


#domy
velikost_domu1 = 100
barva_domu1 = (seda)

dum1_w = velikost_domu1
dum1_h = velikost_domu1
dum1_x = 150
dum1_y = 805


velikost_domu2 = 100
barva_domu2 = (seda)

dum2_w = velikost_domu2
dum2_h = velikost_domu2
dum2_x = ROZLISENI_X/2 - velikost_domu2/2
dum2_y = 805


velikost_domu3 = 100
barva_domu3 = (seda)

dum3_w = velikost_domu3
dum3_h = velikost_domu3
dum3_x = 1670
dum3_y = 805


#spodni_hlina
sirka_spodni_hliny = 1920
vyska_spodni_hliny = 25
barva_spodni_hliny = (hneda)

spodni_hlina_w = 0
spodni_hlina_h = 1030
spodni_hlina_x = sirka_spodni_hliny
spodni_hlina_y = vyska_spodni_hliny

#vrchni_hlina_parametry
w_vrchni_hliny = 240
h_vrchni_hliny = 50
x_vrchni_hliny = 0
y_vrchni_hliny = zizala_y - zizala_h - 25

hlina1 = pygame.Rect(x_vrchni_hliny, y_vrchni_hliny, w_vrchni_hliny, h_vrchni_hliny)
hlina2 = pygame.Rect(x_vrchni_hliny + w_vrchni_hliny, y_vrchni_hliny, w_vrchni_hliny, h_vrchni_hliny)
hlina3 = pygame.Rect(x_vrchni_hliny + 2*w_vrchni_hliny, y_vrchni_hliny, w_vrchni_hliny, h_vrchni_hliny)
hlina4 = pygame.Rect(x_vrchni_hliny + 3*w_vrchni_hliny, y_vrchni_hliny, w_vrchni_hliny, h_vrchni_hliny)
hlina5 = pygame.Rect(x_vrchni_hliny + 4*w_vrchni_hliny, y_vrchni_hliny, w_vrchni_hliny, h_vrchni_hliny)
hlina6 = pygame.Rect(x_vrchni_hliny + 5*w_vrchni_hliny, y_vrchni_hliny, w_vrchni_hliny, h_vrchni_hliny)
hlina7 = pygame.Rect(x_vrchni_hliny + 6*w_vrchni_hliny, y_vrchni_hliny, w_vrchni_hliny, h_vrchni_hliny)
hlina8 = pygame.Rect(x_vrchni_hliny + 7*w_vrchni_hliny, y_vrchni_hliny, w_vrchni_hliny, h_vrchni_hliny)
 
#nepratele - 1.rada
nepritel1 = pygame.Rect(x_nepritele,y_prvni_rady,w_nepratele,h_nepratele)
nepritel2 = pygame.Rect(x_nepritele + w_nepratele +   mezera_mezi_neprateli,y_prvni_rady,w_nepratele,h_nepratele)
nepritel3 = pygame.Rect(x_nepritele + 2*w_nepratele + 2*mezera_mezi_neprateli,y_prvni_rady,w_nepratele,h_nepratele)
nepritel4 = pygame.Rect(x_nepritele + 3*w_nepratele + 3*mezera_mezi_neprateli,y_prvni_rady,w_nepratele,h_nepratele)
nepritel5 = pygame.Rect(x_nepritele + 4*w_nepratele + 4*mezera_mezi_neprateli,y_prvni_rady,w_nepratele,h_nepratele)
nepritel6 = pygame.Rect(x_nepritele + 5*w_nepratele + 5*mezera_mezi_neprateli,y_prvni_rady,w_nepratele,h_nepratele)
nepritel7 = pygame.Rect(x_nepritele + 6*w_nepratele + 6*mezera_mezi_neprateli,y_prvni_rady,w_nepratele,h_nepratele)
nepritel8 = pygame.Rect(x_nepritele + 7*w_nepratele + 7*mezera_mezi_neprateli,y_prvni_rady,w_nepratele,h_nepratele)
nepritel9 = pygame.Rect(x_nepritele + 8*w_nepratele + 8*mezera_mezi_neprateli,y_prvni_rady,w_nepratele,h_nepratele)
nepritel10 = pygame.Rect(x_nepritele + 9*w_nepratele + 9*mezera_mezi_neprateli,y_prvni_rady,w_nepratele,h_nepratele)

#nepratele - 2.rada
nepritel11 = pygame.Rect(x_nepritele,y_druhe_rady,w_nepratele,h_nepratele)
nepritel12 = pygame.Rect(x_nepritele + w_nepratele + mezera_mezi_neprateli,y_druhe_rady,w_nepratele,h_nepratele)
nepritel13 = pygame.Rect(x_nepritele + 2*w_nepratele + 2*mezera_mezi_neprateli,y_druhe_rady,w_nepratele,h_nepratele)
nepritel14 = pygame.Rect(x_nepritele + 3*w_nepratele + 3*mezera_mezi_neprateli,y_druhe_rady,w_nepratele,h_nepratele)
nepritel15 = pygame.Rect(x_nepritele + 4*w_nepratele + 4*mezera_mezi_neprateli,y_druhe_rady,w_nepratele,h_nepratele)
nepritel16 = pygame.Rect(x_nepritele + 5*w_nepratele + 5*mezera_mezi_neprateli,y_druhe_rady,w_nepratele,h_nepratele)
nepritel17 = pygame.Rect(x_nepritele + 6*w_nepratele + 6*mezera_mezi_neprateli,y_druhe_rady,w_nepratele,h_nepratele)
nepritel18 = pygame.Rect(x_nepritele + 7*w_nepratele + 7*mezera_mezi_neprateli,y_druhe_rady,w_nepratele,h_nepratele)
nepritel19 = pygame.Rect(x_nepritele + 8*w_nepratele + 8*mezera_mezi_neprateli,y_druhe_rady,w_nepratele,h_nepratele)
nepritel20 = pygame.Rect(x_nepritele + 9*w_nepratele + 9*mezera_mezi_neprateli,y_druhe_rady,w_nepratele,h_nepratele)

#nepratele - 3.rada
nepritel21 = pygame.Rect(x_nepritele,y_treti_rady,w_nepratele,h_nepratele)
nepritel22 = pygame.Rect(x_nepritele + w_nepratele + mezera_mezi_neprateli,y_treti_rady,w_nepratele,h_nepratele)
nepritel23 = pygame.Rect(x_nepritele + 2*w_nepratele + 2*mezera_mezi_neprateli,y_treti_rady,w_nepratele,h_nepratele)
nepritel24 = pygame.Rect(x_nepritele + 3*w_nepratele + 3*mezera_mezi_neprateli,y_treti_rady,w_nepratele,h_nepratele)
nepritel25 = pygame.Rect(x_nepritele + 4*w_nepratele + 4*mezera_mezi_neprateli,y_treti_rady,w_nepratele,h_nepratele)
nepritel26 = pygame.Rect(x_nepritele + 5*w_nepratele + 5*mezera_mezi_neprateli,y_treti_rady,w_nepratele,h_nepratele)
nepritel27 = pygame.Rect(x_nepritele + 6*w_nepratele + 6*mezera_mezi_neprateli,y_treti_rady,w_nepratele,h_nepratele)
nepritel28 = pygame.Rect(x_nepritele + 7*w_nepratele + 7*mezera_mezi_neprateli,y_treti_rady,w_nepratele,h_nepratele)
nepritel29 = pygame.Rect(x_nepritele + 8*w_nepratele + 8*mezera_mezi_neprateli,y_treti_rady,w_nepratele,h_nepratele)
nepritel30 = pygame.Rect(x_nepritele + 9*w_nepratele + 9*mezera_mezi_neprateli,y_treti_rady,w_nepratele,h_nepratele)

#rychlost_nepratel
v_nepritele = 50


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
    #ovladani_zizaly
    if stisknuto[pygame.K_RIGHT]:
        zizala_x += v_zizaly
    if stisknuto[pygame.K_LEFT]:
        zizala_x -= v_zizaly
    if zizala_x < 0:
        zizala_x = 0
    if zizala_x > ROZLISENI_X - velikost_zizaly:
        zizala_x = ROZLISENI_X - velikost_zizaly
    #sledovani_strely
    if sledovani == True:
        if strela_x > zizala_x: 
            strela_x = zizala_x + zizala_w - strela_w  
        if strela_x < zizala_x:
            strela_x = zizala_x + zizala_w - strela_w
    if sledovani2 == True:            
        if strela2_x > zizala_x: 
            strela2_x = zizala_x + zizala_w - strela2_w  
        if strela2_x < zizala_x: 
            strela2_x = zizala_x + zizala_w - strela2_w
    #strelba
    if stisknuto[pygame.K_SPACE] and not strelba:
        strelba = True

    if strelba == True:
        strela_y -= v_strely
        sledovani = False
        
    if stisknuto[pygame.K_SPACE] and not strelba2 and strela_y < y_treti_rady + h_nepratele:
        strelba2 = True
        
    if strelba2 == True:
        strela2_y -= v_strely
        sledovani2 = False
    
    #kontinualni_strelba
    if strela_y < 0:
        strelba = False
    if strelba == False:
        strela_y = zizala_y
        strela_x = zizala_x + zizala_w - strela_w
    if strela2_y < 0:
        strelba2 = False
    if strelba2 == False:
        strela2_y = zizala_y
        strela2_x = zizala_x + zizala_w - strela2_w
    
    
    
    #pohyb_nepratel



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
    pygame.draw.rect(okno, barva_zizaly,(zizala_x, zizala_y, zizala_w, zizala_h))
    #strela
    if strelba == True:
        pygame.draw.rect(okno, (0,255,0), (strela_x,strela_y,strela_w,strela_h))
    if strelba2 == True and strela_y < y_treti_rady + h_nepratele:
        pygame.draw.rect(okno, (0,255,0), (strela2_x,strela2_y,strela2_w,strela2_h))
        
    #hlina
    pygame.draw.rect(okno, barva_spodni_hliny,(spodni_hlina_w, spodni_hlina_h, spodni_hlina_x, spodni_hlina_y))
    #domy
    pygame.draw.rect(okno, barva_domu1,(dum1_x, dum1_y, dum1_w, dum1_h))
    pygame.draw.rect(okno, barva_domu2,(dum2_x, dum2_y, dum2_w, dum2_h))
    pygame.draw.rect(okno, barva_domu3,(dum3_x, dum3_y, dum3_w, dum3_h))
    #vrchni hlina
    pygame.draw.rect(okno, hneda, hlina1)
    pygame.draw.rect(okno, hneda, hlina2)
    pygame.draw.rect(okno, hneda, hlina3)
    pygame.draw.rect(okno, hneda, hlina4)
    pygame.draw.rect(okno, hneda, hlina5)
    pygame.draw.rect(okno, hneda, hlina6)
    pygame.draw.rect(okno, hneda, hlina7)
    pygame.draw.rect(okno, hneda, hlina8)

    
    
    pygame.display.update()
    

