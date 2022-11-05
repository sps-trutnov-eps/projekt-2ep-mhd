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

#obrazky
zizala = pygame.image.load("zizala.gif")
monkey = pygame.image.load("monke.gif")
house = pygame.image.load("mongol_house.gif")
mensi_hlina = pygame.image.load("mensi_hlina.gif")
vetsi_hlina = pygame.image.load("vetsi_hlina.gif")
spodni_hlina = pygame.image.load("spodni_hlina.gif")
pozadi = pygame.image.load("pozadi.gif")
strela_load = pygame.image.load("strela.gif")
strela = strela_load.get_rect()
banan = pygame.image.load("banan.gif")

objekt = pygame.Rect

#rozměry pro nepřátele
class nepritel(objekt):
    def __init__(self, x, y):
        self.rozmer = [50,50]
        self.x = x
        self.y = y
        self.pozice = [self.x,self.y]
        self.image = monkey
        self.rect = pygame.Rect(self.pozice,self.rozmer)
        self.v = 0.5
        self.zije = True
    def prepocitat(self):
        self.rect = pygame.Rect(self.pozice,self.rozmer)
        
    

        
#pohyb nepratel
pohyb_nepratel1 = True
pohyb_nepratel2 = True
pohyb_nepratel3 = True
pohyb_nepratel4 = True
pohyb_nepratel5 = True

#rozmery zizaly
velikost_zizaly = 50
barva_zizaly = (ruzova)
v_zizaly = 2

zizala_w = velikost_zizaly
zizala_h = velikost_zizaly
zizala_x = ROZLISENI_X/2 - velikost_zizaly/2
zizala_y = ROZLISENI_Y + 25 -velikost_zizaly*2

zizala_zije = True

#strela
velikost_strely = 10
barva_strely = (zelena)
v_strely = 2

strela_x = zizala_x + zizala_w - 8
strela_y = zizala_y
strela.topleft = (strela_x, strela_y)
strelba = False
sledovani = True

#spodni_hlina
spodni_hlina_x = 0
spodni_hlina_y = ROZLISENI_Y - 25

spodni_hlina_rect = spodni_hlina.get_rect()
spodni_hlina_rect.topleft = (spodni_hlina_x, spodni_hlina_y)

#vrchni_hlina_parametry
w_hliny = 240
h_hliny = 30
x_hliny = 0
y_hliny = zizala_y - zizala_h - 25

hlina1 = mensi_hlina.get_rect()
hlina1.topleft = (0,y_hliny)

hlina2 = vetsi_hlina.get_rect()
hlina2.topleft = (2*w_hliny, y_hliny)

hlina3 = vetsi_hlina.get_rect()
hlina3.topleft = (3*w_hliny + 80, y_hliny)

hlina4 = vetsi_hlina.get_rect()
hlina4.topleft = (5*w_hliny-80, y_hliny)

hlina5 = mensi_hlina.get_rect()
hlina5.topleft = (0-25 + 7*w_hliny,y_hliny)

#domy
sirka_domu = 100
vyska_domu = 50

dum1_w = sirka_domu
dum1_h = vyska_domu
dum1_x = 50
dum1_y = 805 + 25


dum2_w = sirka_domu
dum2_h = vyska_domu
dum2_x = hlina2.x + hlina2.w - sirka_domu - 100
dum2_y = 805 + 25


dum3_w = sirka_domu
dum3_h = vyska_domu
dum3_x = hlina4.x + 10
dum3_y = 805 + 25


dum4_w = sirka_domu
dum4_h = vyska_domu
dum4_x = 1670
dum4_y = 805 + 25


dum1 = pygame.Rect(dum1_x, dum1_y, dum1_w, dum1_h)
dum2 = pygame.Rect(dum2_x, dum2_y, dum2_w, dum2_h)
dum3 = pygame.Rect(dum3_x, dum3_y, dum3_w, dum3_h)
dum4 = pygame.Rect(dum4_x, dum4_y, dum4_w, dum4_h)
 
#nepratele - 1.rada
rada1 = []
for i in range(11):
    n = nepritel((310 + 125*i),100)
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
random_rada = random.choice(vsechny_rady)
random_vojak_v_rade = random.choice(random_rada)
random_vojak_v_rade_x = random_vojak_v_rade.pozice[0]
random_vojak_v_rade_y = random_vojak_v_rade.pozice[1]
nepratelska_strela = banan.get_rect()
nepratelska_strela.topleft = (random_vojak_v_rade_x - 21, random_vojak_v_rade_y + 50)


pygame.init()

pygame.display.set_caption('Mongol House Defense')
okno = pygame.display.set_mode(ROZLISENI_OKNA)

while True:
    okno.fill(BARVA_POZADI)
    okno.blit(pozadi,(0,0))
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
            strela.x = zizala_x + zizala_w - 16
        if strela.x < zizala_x:
            strela.x = zizala_x + zizala_w - 16
            
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
        strela.x = zizala_x + zizala_w - 16
    
    
    #pohyb_nepratel

    for i in rada1:
        if pohyb_nepratel1:
            i.pozice[0] += i.v
        else:
            i.pozice[0] -= i.v
        i.prepocitat()
        
    for i in rada1:
        if i.pozice[0] + i.rozmer[0] >= ROZLISENI_X:
            pohyb_nepratel1 = False        
        elif i.pozice[0] <= 0:
            pohyb_nepratel1 = True
        i.prepocitat()

    for i in rada2:
        if pohyb_nepratel2:
            i.pozice[0] += i.v
        else:
            i.pozice[0] -= i.v
        i.prepocitat()
    for i in rada2:
        if i.pozice[0] + i.rozmer[0] >= ROZLISENI_X:
            pohyb_nepratel2 = False        
        elif i.pozice[0] <= 0:
            pohyb_nepratel2 = True
        i.prepocitat()

    for i in rada3:
        if pohyb_nepratel3:
            i.pozice[0] += i.v
        else:
            i.pozice[0] -= i.v
        i.prepocitat()
    for i in rada3:
        if i.pozice[0] + i.rozmer[0] >= ROZLISENI_X:
            pohyb_nepratel3 = False        
        elif i.pozice[0] <= 0:
            pohyb_nepratel3 = True
        i.prepocitat()

    for i in rada4:
        if pohyb_nepratel4:
            i.pozice[0] += i.v
        else:
            i.pozice[0] -= i.v
        i.prepocitat()
    for i in rada4:
        if i.pozice[0] + i.rozmer[0] >= ROZLISENI_X:
            pohyb_nepratel4 = False        
        elif i.pozice[0] <= 0:
            pohyb_nepratel4 = True
        i.prepocitat()

    for i in rada5:
        if pohyb_nepratel5:
            i.pozice[0] += i.v
        else:
            i.pozice[0] -= i.v
        i.prepocitat()
    for i in rada5:
        if i.pozice[0] + i.rozmer[0] >= ROZLISENI_X:
            pohyb_nepratel5 = False        
        elif i.pozice[0] <= 0:
            pohyb_nepratel5 = True
        i.prepocitat()
            
            
    #kolize_strely_s_neprately(NON FUNCTIONAL)
    for i in rada1:
        if pygame.Rect.colliderect(i.rect ,strela) and i.zije:
            i.zije = False
            strelba = False

    for i in rada2:
        if pygame.Rect.colliderect(i.rect ,strela) and i.zije:
            i.zije = False
            strelba = False
            
    for i in rada3:
        if pygame.Rect.colliderect(i.rect ,strela) and i.zije:
            i.zije = False
            strelba = False
           
    for i in rada4:
        if pygame.Rect.colliderect(i.rect ,strela) and i.zije:
            i.zije = False
            strelba = False
            
    for i in rada5:
        if pygame.Rect.colliderect(i.rect ,strela) and i.zije:
            i.zije = False
            strelba = False
    
    #pohyb_nepratelske_strely
    nepratelska_strela.y += 1
    if nepratelska_strela.y >= ROZLISENI_Y:
        random_rada = random.choice(vsechny_rady)
        random_vojak_v_rade = random.choice(random_rada)
        nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
        nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
        
    
    #1. rada nepratel
    for i in rada1:
        if i.zije == True:
            okno.blit(i.image, i.pozice)
            
    #2. rada nepratel
    for i in rada2:
        if i.zije == True:
            okno.blit(i.image, i.pozice)

    #3. rada nepratel
    for i in rada3:
        if i.zije == True:
            okno.blit(i.image, i.pozice)

    #4. rada nepratel
    for i in rada4:
        if i.zije == True:
            okno.blit(i.image, i.pozice)

    #5. rada nepratel
    for i in rada5:
        if i.zije == True:
            okno.blit(i.image, i.pozice)

    #zizala
    if zizala_zije == True:
        okno.blit(zizala, (zizala_x, zizala_y))
        
    #strela
    if strelba == True:
        okno.blit(strela_load, strela) 
        
    #spodni_hlina
    okno.blit(spodni_hlina, spodni_hlina_rect)
    #domy
    okno.blit(house, (dum1_x, dum1_y))
    okno.blit(house, (dum2_x, dum2_y))
    okno.blit(house, (dum3_x, dum3_y))
    okno.blit(house, (dum4_x, dum4_y))
    #hlina
    okno.blit(mensi_hlina, hlina1)
    okno.blit(vetsi_hlina, hlina2)
    okno.blit(vetsi_hlina, hlina3)    
    okno.blit(vetsi_hlina, hlina4)
    okno.blit(mensi_hlina, hlina5)
    #nepratelska_strela
    okno.blit(banan, nepratelska_strela)

    
    
    pygame.display.update()
    