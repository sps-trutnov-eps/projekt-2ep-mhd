import sys
import pygame
import random
pygame.init()

ROZLISENI_OKNA = ROZLISENI_X, ROZLISENI_Y = 1920, 1080
cas = pygame.time.Clock()

program_bezi = True
game_over_TF = True
hrajem = True
winner = False

#barvy
cerna = (0,0,0)
bila = (255,255,255)
ruzova = (199,21,133)
hneda = (139,69,19)
seda = (128,128,128)
zelena = (0,255,0)
cervena = (255,0,0)
BARVA_POZADI = cerna

#Game over text
game_over = pygame.image.load("game_over.png")
winner_ = pygame.image.load("winner.png")

#obrazky
zizala_load = pygame.image.load("zizala.gif")
monkey = pygame.image.load("monke.gif")
house1_vykres = pygame.image.load("mongol_house.gif")
house2_vykres = pygame.image.load("mongol_house.gif")
house3_vykres = pygame.image.load("mongol_house.gif")
house4_vykres = pygame.image.load("mongol_house.gif")
hlina1_vykres = pygame.image.load("mensi_hlina.gif")
hlina2_vykres = pygame.image.load("vetsi_hlina.gif")
hlina3_vykres = pygame.image.load("vetsi_hlina.gif")
hlina4_vykres = pygame.image.load("vetsi_hlina.gif")
hlina5_vykres = pygame.image.load("mensi_hlina.gif") 
spodni_hlina = pygame.image.load("spodni_hlina.gif")
pozadi = pygame.image.load("pozadi.gif")
strela_load = pygame.image.load("strela.gif")
banan = pygame.image.load("banan.gif")
objekt = pygame.Rect

#zvuky
zvuk_strelby = pygame.mixer.Sound("BFG1.wav")
zvuk_nepratelske_strelby = pygame.mixer.Sound("banan.wav")

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
v_zizaly = 3

zizala_w = velikost_zizaly
zizala_h = velikost_zizaly
zizala_x = ROZLISENI_X/2 - velikost_zizaly/2
zizala_y = ROZLISENI_Y + 25 -velikost_zizaly*2
zizala = zizala_load.get_rect()

zizala_zije = True

#strela
velikost_strely = 10
barva_strely = (zelena)
v_strely = 13

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

hlina2 = hlina2_vykres.get_rect()
hlina2.topleft = (2*w_hliny, y_hliny)

hlina3 = hlina3_vykres.get_rect()
hlina3.topleft = (3*w_hliny + 80, y_hliny)

hlina4 = hlina4_vykres.get_rect()
hlina4.topleft = (5*w_hliny-80, y_hliny)

hlina5 = hlina5_vykres.get_rect() 
hlina5.topleft = (0-25 + 7*w_hliny,y_hliny) 

vykreslovani_hliny1 = True
vykreslovani_hliny2 = True
vykreslovani_hliny3 = True
vykreslovani_hliny4 = True
vykreslovani_hliny5 = True

vykreslovani_domu1 = True
vykreslovani_domu2 = True
vykreslovani_domu3 = True
vykreslovani_domu4 = True

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
demolice_domu0_house2 = True
demolice_domu1_house2 = False
demolice_domu2_house2 = False
demolice_domu3_house2 = False
demolice_hliny0_hlina2 = False
demolice_hliny1_hlina2 = False


dum3_w = sirka_domu
dum3_h = vyska_domu
dum3_x = hlina4.x + 10
dum3_y = 805 + 25
house3 = house3_vykres.get_rect()
house3.topleft = (dum1_x, dum1_y)
demolice_domu0_house3 = True
demolice_domu1_house3 = False
demolice_domu2_house3 = False
demolice_domu3_house3 = False
demolice_hliny0_hlina3 = True
demolice_hliny1_hlina3 = False


dum4_w = sirka_domu
dum4_h = vyska_domu
dum4_x = 1670
dum4_y = 805 + 25
house4 = house4_vykres.get_rect()
house4.topleft = (dum1_x, dum1_y)
demolice_domu0_house4 = True
demolice_domu1_house4 = False
demolice_domu2_house4 = False
demolice_domu3_house4 = False
demolice_hliny0_hlina4 = False
demolice_hliny1_hlina4 = False


demolice_hliny0_hlina5 = False
demolice_hliny1_hlina5 = False

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
    
vsechny_rady = [rada1, rada2, rada3, rada4, rada5]


#nepratelska strela
random_rada = random.choice(vsechny_rady)
random_vojak_v_rade = random.choice(random_rada)
random_vojak_v_rade_x = random_vojak_v_rade.pozice[0]
random_vojak_v_rade_y = random_vojak_v_rade.pozice[1]
zvuk_nepratelske_strelby.play()
nepratelska_strela = banan.get_rect()
nepratelska_strela.topleft = (random_vojak_v_rade_x - 21, random_vojak_v_rade_y + 50)

vsechny_domy = []
vsechny_domy.append(house1)
vsechny_domy.append(house2)
vsechny_domy.append(house3)
vsechny_domy.append(house4)

#random výběr
random_vyber = True
random_vojak = True

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
    if hrajem == True:    
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
            
        if strela.y == 990:
            zvuk_strelby.play()
        
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
            hrajem = False
            game_over_TF = False
            
                           
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
            if i == []:
                vsechny_rady.remove(i)
                
        if vsechny_rady == []:
            hrajem = False
            winner = True
            random_vyber = False
            
        
        #pohyb_nepratelske_strely
        nepratelska_strela.y += 5
        if random_vyber:
            if nepratelska_strela.y >= ROZLISENI_Y:
                random_rada = random.choice(vsechny_rady)
                random_vojak_v_rade = random.choice(random_rada)
                nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
                nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
                zvuk_nepratelske_strelby.play()
                
                
        #demolice domu1
        if demolice_domu0_house1 == True:
            if pygame.Rect.colliderect(house1, nepratelska_strela) or pygame.Rect.colliderect(hlina1, nepratelska_strela):
                house1_vykres = pygame.image.load("house_boom1.gif")
                demolice_domu0_house1 = False
                demolice_domu1_house1 = True
                random_rada = random.choice(vsechny_rady)
                random_vojak_v_rade = random.choice(random_rada)
                nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
                nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
                zvuk_nepratelske_strelby.play()
            
        if demolice_domu1_house1 == True:
            if pygame.Rect.colliderect(house1, nepratelska_strela) or pygame.Rect.colliderect(hlina1, nepratelska_strela):
                house1_vykres = pygame.image.load("house_boom2.gif")
                demolice_domu1_house1 = False
                demolice_domu2_house1 = True
                random_rada = random.choice(vsechny_rady)
                random_vojak_v_rade = random.choice(random_rada)
                nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
                nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
                zvuk_nepratelske_strelby.play()
                
        if demolice_domu2_house1 == True:
            if pygame.Rect.colliderect(house1, nepratelska_strela) or pygame.Rect.colliderect(hlina1, nepratelska_strela):
                house1_vykres = pygame.image.load("house_boom3.gif")
                demolice_domu2_house1 = False
                demolice_domu3_house1 = True
                random_rada = random.choice(vsechny_rady)
                random_vojak_v_rade = random.choice(random_rada)
                nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
                nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
                zvuk_nepratelske_strelby.play()
                
        if demolice_domu3_house1 == True:
            if pygame.Rect.colliderect(house1, nepratelska_strela) or pygame.Rect.colliderect(hlina1, nepratelska_strela):
                if vykreslovani_domu1:
                    vsechny_domy.remove(house1)
                    demolice_domu3_house1 = False
                    demolice_hliny0_hlina1 = True
                    random_rada = random.choice(vsechny_rady)
                    random_vojak_v_rade = random.choice(random_rada)
                    nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
                    nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
                    zvuk_nepratelske_strelby.play()
                vykreslovani_domu1 = False
        
        if demolice_hliny0_hlina1:
            if pygame.Rect.colliderect(hlina1,nepratelska_strela):
                hlina1_vykres = pygame.image.load("mensi_hlina_znicena.gif")
                demolice_hliny0_hlina1 = False
                demolice_hliny1_hlina1 = True
                random_rada = random.choice(vsechny_rady)
                random_vojak_v_rade = random.choice(random_rada)
                nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
                nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
                zvuk_nepratelske_strelby.play()
        
        if demolice_hliny1_hlina1:
            if pygame.Rect.colliderect(hlina1,nepratelska_strela):
                if vykreslovani_hliny1:
                    random_rada = random.choice(vsechny_rady)
                    random_vojak_v_rade = random.choice(random_rada)
                    nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
                    nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
                    zvuk_nepratelske_strelby.play()
                vykreslovani_hliny1 = False
                
        #demolice domu2
        if demolice_domu0_house2 == True:
            if pygame.Rect.colliderect(house2, nepratelska_strela) or pygame.Rect.colliderect(hlina2, nepratelska_strela):
                house2_vykres = pygame.image.load("house_boom1.gif")
                demolice_domu0_house2 = False
                demolice_domu1_house2 = True
                random_rada = random.choice(vsechny_rady)
                random_vojak_v_rade = random.choice(random_rada)
                nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
                nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
                zvuk_nepratelske_strelby.play()
            
            
        if demolice_domu1_house2 == True:
            if pygame.Rect.colliderect(house2, nepratelska_strela) or pygame.Rect.colliderect(hlina2, nepratelska_strela):
                house2_vykres = pygame.image.load("house_boom2.gif")
                demolice_domu1_house2 = False
                demolice_domu2_house2 = True
                random_rada = random.choice(vsechny_rady)
                random_vojak_v_rade = random.choice(random_rada)
                nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
                nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
                zvuk_nepratelske_strelby.play()
                
        if demolice_domu2_house2 == True:
            if pygame.Rect.colliderect(house2, nepratelska_strela) or pygame.Rect.colliderect(hlina2, nepratelska_strela):
                house2_vykres = pygame.image.load("house_boom3.gif")
                demolice_domu2_house2 = False
                demolice_domu3_house2 = True
                random_rada = random.choice(vsechny_rady)
                random_vojak_v_rade = random.choice(random_rada)
                nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
                nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
                zvuk_nepratelske_strelby.play()
                
        if demolice_domu3_house2 == True:
            if pygame.Rect.colliderect(house2, nepratelska_strela) or pygame.Rect.colliderect(hlina2, nepratelska_strela):
                if vykreslovani_domu2:
                    vsechny_domy.remove(house2)
                    demolice_domu3_house2 = False
                    demolice_hliny0_hlina2 = True
                    random_rada = random.choice(vsechny_rady)
                    random_vojak_v_rade = random.choice(random_rada)
                    nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
                    nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
                    zvuk_nepratelske_strelby.play()
                vykreslovani_domu2 = False
        
        if demolice_hliny0_hlina2:
            if pygame.Rect.colliderect(hlina2,nepratelska_strela):
                hlina2_vykres = pygame.image.load("vetsi_hlina_znicena.gif")
                demolice_hliny0_hlina2 = False
                demolice_hliny1_hlina2 = True
                random_rada = random.choice(vsechny_rady)
                random_vojak_v_rade = random.choice(random_rada)
                nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
                nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
                zvuk_nepratelske_strelby.play()
        
        if demolice_hliny1_hlina2:
            if  pygame.Rect.colliderect(hlina2,nepratelska_strela):
                if vykreslovani_hliny2:
                    random_rada = random.choice(vsechny_rady)
                    random_vojak_v_rade = random.choice(random_rada)
                    nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
                    nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
                    zvuk_nepratelske_strelby.play()
                vykreslovani_hliny2 = False

                
        #demolice_domu3
        if demolice_domu0_house3 == True:
            if pygame.Rect.colliderect(house3, nepratelska_strela) or pygame.Rect.colliderect(hlina4, nepratelska_strela):
                house3_vykres = pygame.image.load("house_boom1.gif")
                demolice_domu0_house3 = False
                demolice_domu1_house3 = True
                random_rada = random.choice(vsechny_rady)
                random_vojak_v_rade = random.choice(random_rada)
                nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
                nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
                zvuk_nepratelske_strelby.play()
            
            
        if demolice_domu1_house3 == True:
            if pygame.Rect.colliderect(house3, nepratelska_strela) or pygame.Rect.colliderect(hlina4, nepratelska_strela):
                house3_vykres = pygame.image.load("house_boom2.gif")
                demolice_domu1_house3 = False
                demolice_domu2_house3 = True
                random_rada = random.choice(vsechny_rady)
                random_vojak_v_rade = random.choice(random_rada)
                nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
                nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
                zvuk_nepratelske_strelby.play()
                
        if demolice_domu2_house3 == True:
            if pygame.Rect.colliderect(house3, nepratelska_strela) or pygame.Rect.colliderect(hlina4, nepratelska_strela):
                house3_vykres = pygame.image.load("house_boom3.gif")
                demolice_domu2_house3 = False
                demolice_domu3_house3 = True
                random_rada = random.choice(vsechny_rady)
                random_vojak_v_rade = random.choice(random_rada)
                nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
                nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
                zvuk_nepratelske_strelby.play()
                
        if demolice_domu3_house3 == True:
            if pygame.Rect.colliderect(house3, nepratelska_strela) or pygame.Rect.colliderect(hlina4, nepratelska_strela):
                if vykreslovani_domu3:
                    vsechny_domy.remove(house3)
                    demolice_domu3_house3 = False
                    demolice_hliny0_hlina4 = True
                    random_rada = random.choice(vsechny_rady)
                    random_vojak_v_rade = random.choice(random_rada)
                    nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
                    nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
                    zvuk_nepratelske_strelby.play()
                vykreslovani_domu3 = False
        
        if demolice_hliny0_hlina4:
            if pygame.Rect.colliderect(hlina4,nepratelska_strela):
                hlina4_vykres = pygame.image.load("vetsi_hlina_znicena.gif")
                demolice_hliny0_hlina4 = False
                demolice_hliny1_hlina4 = True
                random_rada = random.choice(vsechny_rady)
                random_vojak_v_rade = random.choice(random_rada)
                nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
                nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
                zvuk_nepratelske_strelby.play()
        
        if demolice_hliny1_hlina4:
            if  pygame.Rect.colliderect(hlina4,nepratelska_strela):
                if vykreslovani_hliny4:
                    random_rada = random.choice(vsechny_rady)
                    random_vojak_v_rade = random.choice(random_rada)
                    nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
                    nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
                    zvuk_nepratelske_strelby.play()
                vykreslovani_hliny4 = False
                
        #demolice_domu4
        if demolice_domu0_house4 == True:
            if pygame.Rect.colliderect(house4, nepratelska_strela) or pygame.Rect.colliderect(hlina5, nepratelska_strela):
                house4_vykres = pygame.image.load("house_boom1.gif")
                demolice_domu0_house4 = False
                demolice_domu1_house4 = True
                random_rada = random.choice(vsechny_rady)
                random_vojak_v_rade = random.choice(random_rada)
                nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
                nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
                zvuk_nepratelske_strelby.play()
            
            
        if demolice_domu1_house4 == True:
            if pygame.Rect.colliderect(house4, nepratelska_strela) or pygame.Rect.colliderect(hlina5, nepratelska_strela):
                house4_vykres = pygame.image.load("house_boom2.gif")
                demolice_domu1_house4 = False
                demolice_domu2_house4= True
                random_rada = random.choice(vsechny_rady)
                random_vojak_v_rade = random.choice(random_rada)
                nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
                nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
                zvuk_nepratelske_strelby.play()
                
        if demolice_domu2_house4 == True:
            if pygame.Rect.colliderect(house4, nepratelska_strela) or pygame.Rect.colliderect(hlina5, nepratelska_strela):
                house4_vykres = pygame.image.load("house_boom3.gif")
                demolice_domu2_house4 = False
                demolice_domu3_house4 = True
                random_rada = random.choice(vsechny_rady)
                random_vojak_v_rade = random.choice(random_rada)
                nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
                nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
                zvuk_nepratelske_strelby.play()
                
        if demolice_domu3_house4 == True:
            if pygame.Rect.colliderect(house4, nepratelska_strela) or pygame.Rect.colliderect(hlina5, nepratelska_strela):
                if vykreslovani_domu4:
                    vsechny_domy.remove(house4)
                    demolice_domu3_house4 = False
                    demolice_hliny0_hlina5 = True
                    random_rada = random.choice(vsechny_rady)
                    random_vojak_v_rade = random.choice(random_rada)
                    nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
                    nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
                    zvuk_nepratelske_strelby.play()
                vykreslovani_domu4 = False
        
        if demolice_hliny0_hlina5:
            if pygame.Rect.colliderect(hlina5,nepratelska_strela):
                hlina5_vykres = pygame.image.load("mensi_hlina_znicena.gif")
                demolice_hliny0_hlina5 = False
                demolice_hliny1_hlina5 = True
                random_rada = random.choice(vsechny_rady)
                random_vojak_v_rade = random.choice(random_rada)
                nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
                nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
                zvuk_nepratelske_strelby.play()
        
        if demolice_hliny1_hlina5:
            if  pygame.Rect.colliderect(hlina5,nepratelska_strela):
                if vykreslovani_hliny5:
                    random_rada = random.choice(vsechny_rady)
                    random_vojak_v_rade = random.choice(random_rada)
                    nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
                    nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
                    zvuk_nepratelske_strelby.play()
                vykreslovani_hliny5 = False

                
        #prostredni_hlina
        if demolice_hliny0_hlina3:
            if pygame.Rect.colliderect(hlina3,nepratelska_strela):
                hlina3_vykres = pygame.image.load("vetsi_hlina_znicena.gif")
                demolice_hliny0_hlina3 = False
                demolice_hliny1_hlina3 = True
                random_rada = random.choice(vsechny_rady)
                random_vojak_v_rade = random.choice(random_rada)
                nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
                nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
                zvuk_nepratelske_strelby.play()
        
        if demolice_hliny1_hlina3:
            if  pygame.Rect.colliderect(hlina3,nepratelska_strela):
                if vykreslovani_hliny3:
                    random_rada = random.choice(vsechny_rady)
                    random_vojak_v_rade = random.choice(random_rada)
                    nepratelska_strela.x = random_vojak_v_rade.pozice[0] - 21
                    nepratelska_strela.y = random_vojak_v_rade.pozice[1] + 50
                    zvuk_nepratelske_strelby.play()
                vykreslovani_hliny3 = False

        #kolize_strely_zizaly_s_hlinou
        if pygame.Rect.colliderect(strela, hlina1) and vykreslovani_hliny1:
            zizala_zije = False
            hrajem = False
            game_over_TF = False
            
        if pygame.Rect.colliderect(strela, hlina2) and vykreslovani_hliny2:
            zizala_zije = False
            hrajem = False
            game_over_TF = False
            
        if pygame.Rect.colliderect(strela, hlina3) and vykreslovani_hliny3:
            zizala_zije = False
            hrajem = False
            game_over_TF = False
            
        if pygame.Rect.colliderect(strela, hlina4) and vykreslovani_hliny4:
            zizala_zije = False
            hrajem = False
            game_over_TF = False
            
        if pygame.Rect.colliderect(strela, hlina5) and vykreslovani_hliny5:
            zizala_zije = False
            hrajem = False
            game_over_TF = False
                
    if vsechny_domy == []:
        game_over_TF = False
        hrajem = False
        
        
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
    if vykreslovani_domu1:
        okno.blit(house1_vykres, (dum1_x, dum1_y))
    if vykreslovani_domu2:
        okno.blit(house2_vykres, (dum2_x, dum2_y))
    if vykreslovani_domu3:
        okno.blit(house3_vykres, (dum3_x, dum3_y))
    if vykreslovani_domu4:
        okno.blit(house4_vykres, (dum4_x, dum4_y))
    #hlina
    if vykreslovani_hliny1:
        okno.blit(hlina1_vykres, hlina1)
    if vykreslovani_hliny2:
        okno.blit(hlina2_vykres, hlina2)
    if vykreslovani_hliny3:
        okno.blit(hlina3_vykres, hlina3)
    if vykreslovani_hliny4:
        okno.blit(hlina4_vykres, hlina4)
    if vykreslovani_hliny5:
        okno.blit(hlina5_vykres, hlina5) 
    #nepratelska_strela
    okno.blit(banan, nepratelska_strela)
    #Game over
    if game_over_TF == False:
        okno.blit(game_over, (ROZLISENI_X/2 - 576/2, ROZLISENI_Y/2 - 470/2))
    if winner == True:
        okno.blit(winner_, (ROZLISENI_X/2 - 690/2, ROZLISENI_Y/2 - 250/2))
        

        
        
    pygame.display.update()
        
