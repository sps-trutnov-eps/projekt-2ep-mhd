import sys
import pygame
import random

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 1920, 1080
cas = pygame.time.Clock()

#barvy
cerna = (0,0,0)
bila = (255,255,255)
ruzova = (199,21,133)
hneda = (139,69,19)
seda = (128,128,128)
zelena = (0,255,0)
BARVA_POZADI = cerna


#rozměry pro nepřátele
class nepritel():
    def __init__(self,x,y):
        self.rozmer = [50,50]
        self.x = x
        self.y = y
        self.pozice = [self.x,self.y]
        self.v = 1.5
        self.zije = True
        self.rada_nepratel1 = pygame.Rect
        
#pohyb nepratel
pohyb_nepratel1 = True
pohyb_nepratel2 = True
pohyb_nepratel3 = True
pohyb_nepratel4 = True
pohyb_nepratel5 = True
                
                
#kolize_strely_s_neprateli 
zije1 = True
zije2 = True
zije3 = True
zije4 = True
zije5 = True

#rozmery zizaly
velikost_zizaly = 50
barva_zizaly = (ruzova)
v_zizaly = 2

zizala_w = velikost_zizaly
zizala_h = velikost_zizaly
zizala_x = ROZLISENI_X/2 - velikost_zizaly/2
zizala_y = ROZLISENI_Y - velikost_zizaly*2

zizala_zije = True

#strela
velikost_strely = 10
barva_strely = (hneda)
v_strely = 2

strela_w = velikost_strely
strela_h = velikost_strely
strela_x = zizala_x + zizala_w - strela_w
strela_y = zizala_y
strela = pygame.Rect(strela_x, strela_y, strela_w, strela_h)
strelba = False
sledovani = True

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
rada1 = []
for i in range(11):
    n = nepritel(310 + 125*i,100)
    rada1.append(n)

#nepratele - 2.rada
rada2 = []
for i in range(11):
    n = nepritel((310 + 125*i),200)
    rada2.append(n)
    
#nepratele - 3.rada
rada3 = []
for i in range(11):
    n = nepritel((310 + 125*i),300)
    rada3.append(n)
    
#nepratele - 4.rada
rada4 = []
for i in range(11):
    n = nepritel((310 + 125*i),400)
    rada4.append(n)
    
#nepratele - 5.rada
rada5 = []
for i in range(11):
    n = nepritel((310 + 125*i),500)
    rada5.append(n)
    
vsechny_rady = []
vsechny_rady.append(rada1)
vsechny_rady.append(rada2)
vsechny_rady.append(rada3)
vsechny_rady.append(rada4)
vsechny_rady.append(rada5)

#nepratelska strela
nepratelska_strela_w = 10
nepratelska_strela_h = 10
random_rada = random.choice(vsechny_rady)
random_vojak_v_rade = random.choice(random_rada)
random_vojak_v_rade_x = random_vojak_v_rade.pozice[0]
random_vojak_v_rade_y = random_vojak_v_rade.pozice[1]
nepratelska_strela = pygame.Rect(random_vojak_v_rade_x, random_vojak_v_rade_y, nepratelska_strela_w, nepratelska_strela_h)




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
    if sledovani:
        if strela.x > zizala_x: 
            strela.x = zizala_x + zizala_w - strela.w  
        if strela.x < zizala_x:
            strela.x = zizala_x + zizala_w - strela.w
            
    #strelba
    if stisknuto[pygame.K_SPACE]:
        strelba = True

    if strelba == True:
        strela.y -= v_strely
        sledovani = False
    
    
    #kontinualni_strelba
    if strela.y < 0:
        strelba = False
    if strelba == False:
        strela.y = zizala_y
        strela.x = zizala_x + zizala_w - strela.w
    
    
    #pohyb_nepratel

    for i in rada1:
        if pohyb_nepratel1:
            i.pozice[0] += i.v
        else:
            i.pozice[0] -= i.v
    for i in rada1:
        if i.pozice[0] + i.rozmer[0] >= ROZLISENI_X:
            pohyb_nepratel1 = False        
        elif i.pozice[0] <= 0:
            pohyb_nepratel1 = True

    for i in rada2:
        if pohyb_nepratel2:
            i.pozice[0] += i.v
        else:
            i.pozice[0] -= i.v
    for i in rada2:
        if i.pozice[0] + i.rozmer[0] >= ROZLISENI_X:
            pohyb_nepratel2 = False        
        elif i.pozice[0] <= 0:
            pohyb_nepratel2 = True

    for i in rada3:
        if pohyb_nepratel3:
            i.pozice[0] += i.v
        else:
            i.pozice[0] -= i.v
    for i in rada3:
        if i.pozice[0] + i.rozmer[0] >= ROZLISENI_X:
            pohyb_nepratel3 = False        
        elif i.pozice[0] <= 0:
            pohyb_nepratel3 = True

    for i in rada4:
        if pohyb_nepratel4:
            i.pozice[0] += i.v
        else:
            i.pozice[0] -= i.v
    for i in rada4:
        if i.pozice[0] + i.rozmer[0] >= ROZLISENI_X:
            pohyb_nepratel4 = False        
        elif i.pozice[0] <= 0:
            pohyb_nepratel4 = True

    for i in rada5:
        if pohyb_nepratel5:
            i.pozice[0] += i.v
        else:
            i.pozice[0] -= i.v
    for i in rada5:
        if i.pozice[0] + i.rozmer[0] >= ROZLISENI_X:
            pohyb_nepratel5 = False        
        elif i.pozice[0] <= 0:
            pohyb_nepratel5 = True
            
            
    #kolize_strely_s_neprately(NON FUNCTIONAL)
    for i in rada1:
        if i.pozice[1] == strela_y and strela_x:
            i.zije = False
            strelba = False

    for i in rada2:
        if i.pozice[1] == strela_y and strela_x:
            i.zije = False
            strelba = False
            
    for i in rada3:
        if i.pozice[1] == strela_y and strela_x:
            i.zije = False
            strelba = False
           
    for i in rada4:
        if i.pozice[1] == strela_y and strela_x:
            i.zije = False
            strelba = False
            
    for i in rada5:
        if i.pozice[1] == strela_y and strela_x:
            i.zije = False
            strelba = False
    
    #pohyb_nepratelske_strely
    nepratelska_strela.y += 1
    if nepratelska_strela.y >= ROZLISENI_Y:
        random_rada = random.choice(vsechny_rady)
        random_vojak_v_rade = random.choice(random_rada)
        nepratelska_strela.x = random_vojak_v_rade.pozice[0]
        nepratelska_strela.y = random_vojak_v_rade.pozice[1]
        
    
    okno.fill(BARVA_POZADI)
    #1. rada nepratel
    if zije1 == True:
        for i in rada1:
            pygame.draw.rect(okno,bila,(i.pozice,i.rozmer))
    #2. rada nepratel
    if zije2 == True:
        for i in rada2:
            pygame.draw.rect(okno,bila,(i.pozice,i.rozmer))

    #3.rada nepratel
    if zije3 == True:
        for i in rada3:
            pygame.draw.rect(okno,bila,(i.pozice,i.rozmer))
    
    #4. rada neprartel
    if zije4 == True:
        for i in rada4:
            pygame.draw.rect(okno,bila,(i.pozice,i.rozmer))
    #5. rada nepratel
    if zije5 == True:
        for i in rada5:
            pygame.draw.rect(okno,bila,(i.pozice,i.rozmer))

    #zizala
    if zizala_zije == True:
        pygame.draw.rect(okno, barva_zizaly,(zizala_x, zizala_y, zizala_w, zizala_h))
    #strela
    if strelba == True:
        pygame.draw.rect(okno, (0,255,0), strela)
        
    #spodni_hlina
    pygame.draw.rect(okno, barva_spodni_hliny,(spodni_hlina_w, spodni_hlina_h, spodni_hlina_x, spodni_hlina_y))
    #domy
    pygame.draw.rect(okno, barva_domu1,(dum1_x, dum1_y, dum1_w, dum1_h))
    pygame.draw.rect(okno, barva_domu2,(dum2_x, dum2_y, dum2_w, dum2_h))
    pygame.draw.rect(okno, barva_domu3,(dum3_x, dum3_y, dum3_w, dum3_h))
    #vrchni_hlina
    pygame.draw.rect(okno, hneda, hlina1)
    pygame.draw.rect(okno, hneda, hlina2)
    pygame.draw.rect(okno, hneda, hlina3)
    pygame.draw.rect(okno, hneda, hlina4)
    pygame.draw.rect(okno, hneda, hlina5)
    pygame.draw.rect(okno, hneda, hlina6)
    pygame.draw.rect(okno, hneda, hlina7)
    pygame.draw.rect(okno, hneda, hlina8)
    #nepratelska_strela
    pygame.draw.rect(okno, zelena, nepratelska_strela)

    
    
    pygame.display.update()
    