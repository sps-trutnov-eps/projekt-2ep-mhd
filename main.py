import sys
import pygame
import random

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 1920, 1080
cas = pygame.time.Clock()

program_bezi = True

#barvy
cerna = (0,0,0)
bila = (255,255,255)
ruzova = (199,21,133)
hneda = (139,69,19)
seda = (128,128,128)
zelena = (0,255,0)
BARVA_POZADI = cerna

#obrazky
zizala_load = pygame.image.load("zizala.gif")
monkey = pygame.image.load("monke.gif")
house1_vykres = pygame.image.load("mongol_house.gif")
house2_vykres = pygame.image.load("mongol_house.gif")
house3_vykres = pygame.image.load("mongol_house.gif")
house4_vykres = pygame.image.load("mongol_house.gif")
hlina1_vykres = pygame.image.load("mensi_hlina.gif")
hlina5_vykres = pygame.image.load("mensi_hlina.gif")
vetsi_hlina = pygame.image.load("vetsi_hlina.gif")
spodni_hlina = pygame.image.load("spodni_hlina.gif")
pozadi = pygame.image.load("pozadi.gif")
strela_load = pygame.image.load("strela.gif")
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
zizala = zizala_load.get_rect()

zizala_zije = True

#strela
velikost_strely = 10
barva_strely = (zelena)
v_strely = 15

strela_x = zizala_x + zizala_w - 8
strela_y = zizala_y
strela = strela_load.get_rect()
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

hlina1 = hlina1_vykres.get_rect()
hlina1.topleft = (0,y_hliny)
demolice_hliny1 = False

hlina2 = vetsi_hlina.get_rect()
hlina2.topleft = (2*w_hliny, y_hliny)

hlina3 = vetsi_hlina.get_rect()
hlina3.topleft = (3*w_hliny + 80, y_hliny)

hlina4 = vetsi_hlina.get_rect()
hlina4.topleft = (5*w_hliny-80, y_hliny)

hlina5 = hlina5_vykres.get_rect()
hlina5.topleft = (0-25 + 7*w_hliny,y_hliny)

#domy
sirka_domu = 100
vyska_domu = 50

dum1_w = sirka_domu
dum1_h = vyska_domu
dum1_x = 50
dum1_y = 805 + 25
house1 = house1_vykres.get_rect()
house1.topleft = (dum1_x, dum1_y)
demolice_domu0_house1 = True
demolice_domu1_house1 = False
demolice_domu2_house1 = False
demolice_domu3_house1 = False
demolice_hliny0_hlina1 = False
demolice_hliny1_hlina1 = False

dum2_w = sirka_domu
dum2_h = vyska_domu
dum2_x = hlina2.x + hlina2.w - sirka_domu - 100
dum2_y = 805 + 25
house2 = house2_vykres.get_rect()
house2.topleft = (dum1_x, dum1_y)


dum3_w = sirka_domu
dum3_h = vyska_domu
dum3_x = hlina4.x + 10
dum3_y = 805 + 25
house3 = house3_vykres.get_rect()
house3.topleft = (dum1_x, dum1_y)


dum4_w = sirka_domu
dum4_h = vyska_domu
dum4_x = 1670
dum4_y = 805 + 25
house4 = house4_vykres.get_rect()
house4.topleft = (dum1_x, dum1_y)



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

#random výběr
random_vyber = True
random_vojak = True

pygame.init()

pygame.display.set_caption('Mongol House Defense')
okno = pygame.display.set_mode(ROZLISENI_OKNA)

while program_bezi:
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
    elif stisknuto[pygame.K_LEFT]:
        zizala_x -= v_zizaly
    if zizala_x < 0:
        zizala_x = 0
    if zizala_x > ROZLISENI_X - velikost_zizaly:
        zizala_x = ROZLISENI_X - velikost_zizaly
    zizala.topleft = (zizala_x, zizala_y)

    #sledovani_strely
    if sledovani:
        if strela.x > zizala_x: 
            strela.x = zizala_x + zizala_w - 16
        if strela.x < zizala_x:
            strela.x = zizala_x + zizala_w - 16
            
    #strelba
    if strelba == True:
        strela.y -= v_strely
        sledovani = False
    
    #kontinualni_strelba
    if strela.y < 0:
        strelba = False
    if strelba == False:
        strela.y = zizala_y
        strela.x = zizala_x + zizala_w - 16

    #strelba
    if stisknuto[pygame.K_SPACE]:
        strelba = True
    
    
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
        
    #kolize_zizaly_s_nepratelskou_strelou
    if pygame.Rect.colliderect(nepratelska_strela, zizala):
        zizala_zije = False

                       
    #kolize strely s neprately
    for i in rada1:
        if pygame.Rect.colliderect(i.rect ,strela):
            strelba = False
            rada1.remove(i)

    for i in rada2:
        if pygame.Rect.colliderect(i.rect ,strela):
            strelba = False
            rada2.remove(i)
            
    for i in rada3:
        if pygame.Rect.colliderect(i.rect ,strela):
            strelba = False
            rada3.remove(i)
           
    for i in rada4:
        if pygame.Rect.colliderect(i.rect ,strela):
            strelba = False
            rada4.remove(i)
            
    for i in rada5:
        if pygame.Rect.colliderect(i.rect ,strela):
            strelba = False
            rada5.remove(i)
            
    for i in vsechny_rady:
        if i == [0]:
            vsechny_rady.remove(i)
        
    if vsechny_rady == [0]:
        pygame.quit()
        sys.exit()
        random_vyber = False
    
    #pohyb_nepratelske_strely
    nepratelska_strela.y += 3
    if random_vyber:
        if nepratelska_strela.y >= ROZLISENI_Y:        
            random_rada = random.choice(vsechny_rady)
            random_vojak_v_rade = random.choice(random_rada)
            nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
            nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
            
    #demolice domu
    if demolice_domu0_house1 == True:
        if pygame.Rect.colliderect(house1, nepratelska_strela) or pygame.Rect.colliderect(hlina1, nepratelska_strela):
            house1_vykres = pygame.image.load("house_boom1.gif")
            demolice_domu0_house1 = False
            demolice_domu1_house1 = True
            random_rada = random.choice(vsechny_rady)
            random_vojak_v_rade = random.choice(random_rada)
            nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
            nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
        
        
    if demolice_domu1_house1 == True:
        if pygame.Rect.colliderect(house1, nepratelska_strela) or pygame.Rect.colliderect(hlina1, nepratelska_strela):
            house1_vykres = pygame.image.load("house_boom2.gif")
            demolice_domu1_house1 = False
            demolice_domu2_house1 = True
            random_rada = random.choice(vsechny_rady)
            random_vojak_v_rade = random.choice(random_rada)
            nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
            nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
            
    if demolice_domu2_house1 == True:
        if pygame.Rect.colliderect(house1, nepratelska_strela) or pygame.Rect.colliderect(hlina1, nepratelska_strela):
            house1_vykres = pygame.image.load("house_boom3.gif")
            demolice_domu2_house1 = False
            demolice_domu3_house1 = True
            random_rada = random.choice(vsechny_rady)
            random_vojak_v_rade = random.choice(random_rada)
            nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
            nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
            
    if demolice_domu3_house1 == True:
        if pygame.Rect.colliderect(house1, nepratelska_strela) or pygame.Rect.colliderect(hlina1, nepratelska_strela):
            house1_vykres = pygame.image.load("house_boom4.gif")
            demolice_domu3_house1 = False
            demolice_hliny0_hlina1 = True
            random_rada = random.choice(vsechny_rady)
            random_vojak_v_rade = random.choice(random_rada)
            nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
            nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
    
    if demolice_hliny0_hlina1:
        if pygame.Rect.colliderect(hlina1,nepratelska_strela) and demolice_hliny1 == False:
            hlina1_vykres = pygame.image.load("mensi_hlina_znicena.gif")
            demolice_hliny0_hlina1 = False
            demolice_hliny1_hlina1 = True
            random_rada = random.choice(vsechny_rady)
            random_vojak_v_rade = random.choice(random_rada)
            nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
            nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
    
    if demolice_hliny1_hlina1:
        if  pygame.Rect.colliderect(hlina1,nepratelska_strela):
            hlina1_vykres = pygame.image.load("mensi_hlina_slus.gif")
            demolice_hliny1_hlina1 = False
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
        okno.blit(zizala_load, zizala)
        
    #strela
    if strelba == True:
        okno.blit(strela_load, strela) 
        
    #spodni_hlina
    okno.blit(spodni_hlina, spodni_hlina_rect)
    #domy
    okno.blit(house1_vykres, (dum1_x, dum1_y))
    okno.blit(house2_vykres, (dum2_x, dum2_y))
    okno.blit(house3_vykres, (dum3_x, dum3_y))
    okno.blit(house4_vykres, (dum4_x, dum4_y))
    #hlina
    okno.blit(hlina1_vykres, hlina1)
    okno.blit(vetsi_hlina, hlina2)
    okno.blit(vetsi_hlina, hlina3)    
    okno.blit(vetsi_hlina, hlina4)
    okno.blit(hlina5_vykres, hlina5)
    #nepratelska_strela
    okno.blit(banan, nepratelska_strela)

    
    
    pygame.display.update()
    