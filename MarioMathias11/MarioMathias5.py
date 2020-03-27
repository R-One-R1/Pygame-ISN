#############################PYGAME INITIALISATION##############################
import pygame, sys, time, os, random
from pygame.locals import *
from images import *
from engine import *

clock = pygame.time.Clock()

pygame.mixer.pre_init(44100, -16, 2, 512) #(frequency, quality, stereo, buffer)
pygame.init() # initiates pygame

############################DETECT SCREEN RESOLUTION############################

infoObject = pygame.display.Info()
MonitorRes_w_init = infoObject.current_w
MonitorRes_h_init = infoObject.current_h

MonitorRes_w = round((MonitorRes_w_init / 4) * 3)
MonitorRes_h = round((MonitorRes_h_init / 4) * 3)

############################DETECT SCREEN RESOLUTION############################

pygame.display.set_caption('Sarda Notter Hoareau Dalleau gang')

WINDOW_SIZE = (MonitorRes_w, MonitorRes_h) #(150,90)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate the window

display = pygame.Surface((300,200)) # used as the surface for rendering, which is scaled


def update_fps():
	fps = str(int(clock.get_fps()))
	fps_text = fps
	return fps_text


#############################PYGAME INITIALISATION##############################


#################################IMAGE SCALING##################################

mattis = pygame.transform.scale(mattis, (WINDOW_SIZE[0], WINDOW_SIZE[1]))
mathias = pygame.transform.scale(mathias, (WINDOW_SIZE[0], WINDOW_SIZE[1]))
thomas = pygame.transform.scale(thomas, (WINDOW_SIZE[0], WINDOW_SIZE[1]))
Iaccueil = pygame.transform.scale(Iaccueil, (WINDOW_SIZE[0], WINDOW_SIZE[1]))
ideath = pygame.transform.scale(ideath, (WINDOW_SIZE[0], WINDOW_SIZE[1]))
ilose = pygame.transform.scale(ilose, (WINDOW_SIZE[0], WINDOW_SIZE[1]))
iwin  = pygame.transform.scale(iwin, (WINDOW_SIZE[0], WINDOW_SIZE[1]))
imenu = pygame.transform.scale(imenu, (WINDOW_SIZE[0], WINDOW_SIZE[1]))
imenu2 = pygame.transform.scale(imenu2, (WINDOW_SIZE[0], WINDOW_SIZE[1]))
iloading = pygame.transform.scale(iloading, (WINDOW_SIZE[0], WINDOW_SIZE[1]))
#lvl3_background = pygame.transform.scale(lvl3_background, (WINDOW_SIZE[0], WINDOW_SIZE[1]))

#################################IMAGE SCALING##################################


###############################GAME PREPARATION 1###############################

moving_right = False
moving_left = False
moving_up = False
moving_down = False

vertical_momentum = 0
air_timer = 0

true_scroll = [0,0]

player1 = pygame.image.load('player.png').convert()
player2 = pygame.image.load('player2.png').convert()
player3 = pygame.image.load('player3.png').convert()
player4 = pygame.image.load('player4.png').convert()

player_img = player1
player_img.set_colorkey((255,255,255))
player_rect = pygame.Rect(26*16,31*16,8,13)

globalgame = 1

accueil = 1
game1 = 0
game2 = 0
game3 = 0
game4 = 0

gametimer = 0

nuit = 0

objet = 0
objetscreen = objet0

vie = 3
lifescreen = vie3

loadtime = 0

has_coin = False

click = False
full = 0

done2 = False
done3 = False
done4 = False

#sounds initialisation
jump_sound = pygame.mixer.Sound('music/FX/jump.wav')
land_sound = pygame.mixer.Sound('music/FX/land.wav')
coin_sound = pygame.mixer.Sound('music/FX/coin.wav')
grass_sounds = [pygame.mixer.Sound('music/FX/grass_0.wav'),pygame.mixer.Sound('music/FX/grass_1.wav')]
grass_sounds[0].set_volume(0.7)
grass_sounds[1].set_volume(0.7)
jump_sound.set_volume(0.7)
land_sound.set_volume(0.7)

grass_sound_timer = 0
#sounds initialisation end

god = True

###############################GAME PREPARATION 1###############################

###############################GLOBAL GAME LOOP#################################

while globalgame: #Initialise Game loop

    if vie == 0: #Verify if player is dead 3 times
        screen.blit(ilose, (0,0))
        pygame.display.flip()
        print("tu as perdu tes 3 vies dommage")
        time.sleep(2)
        accueil = 1
        game1 = 1
        game2 = 0
        game3 = 0
        game4 = 0
        gametimer = 0
        nuit = 0
        objet = 0
        objetscreen = objet0
        vie = 3
        lifescreen = vie3
        loadtime = 0
        has_coin = False
        click = False
        done2 = False
        done3 = False
        done4 = False
        
        
    if done2 == True and done3 == True and done4 == True: #Verify if player has won
        screen.blit(iwin, (0,0))
        pygame.mixer.music.load("music/win.ogg")
        pygame.mixer.music.play()
        pygame.display.flip()
        time.sleep(10)
        accueil = 1
        game1 = 1
        game2 = 0
        game3 = 0
        game4 = 0
        gametimer = 0
        nuit = 0
        objet = 0
        objetscreen = objet0
        vie = 3
        lifescreen = vie3
        loadtime = 0
        has_coin = False
        click = False
        done2 = False
        done3 = False
        done4 = False

    if accueil == True:
        pygame.mixer.music.load("music/whereyourheartis.ogg")
        pygame.mixer.music.play(-1, 0)
        has_coin = False


#####################################ACCUEIL####################################

    while accueil:
        #print("acccueil fps:", update_fps())
        screen.blit(imenu2, (0,0))
        #screen.blit(imenu2, (0, 0))
        #screen.fill((0, 0, 0))
        screen.blit(imenu,(0, 0))
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(0.3326*WINDOW_SIZE[0], 0.4722*WINDOW_SIZE[1], 0.3446*WINDOW_SIZE[0], 0.1133*WINDOW_SIZE[1])
        button_2 = pygame.Rect(0.36*WINDOW_SIZE[0], 0.6211*WINDOW_SIZE[1], 0.2866*WINDOW_SIZE[0], 0.1133*WINDOW_SIZE[1])
        button_3 = pygame.Rect(0.404*WINDOW_SIZE[0], 0.7666*WINDOW_SIZE[1], 0.2*WINDOW_SIZE[0], 0.1377*WINDOW_SIZE[1])

        if button_1.collidepoint((mx, my)):
            if click:
                game1 = 1
                game2 = 0
                game3 = 0
                game4 = 0
                loadtime = 0
                accueil = 0

        if button_2.collidepoint((mx, my)):
            if click:
                if full == 0:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    full = 1
                else:
                    screen = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]))
                    full = 0
        if button_3.collidepoint((mx, my)):
            if click:
                screen.fill((0,0,0))
                pygame.display.flip()
                pygame.mixer.music.load("music/wiii2.wav")
                pygame.mixer.music.play()
                time.sleep(4)
                screen.blit(mattis, (0,0))
                pygame.display.flip()
                pygame.time.Clock().tick(60)
                time.sleep(5)
                screen.blit(mathias, (0,0))
                pygame.display.flip()
                time.sleep(5)
                screen.blit(thomas, (0,0))
                pygame.display.flip()
                time.sleep(5)
                pygame.mixer.music.load("music/whereyourheartis.ogg")
                pygame.mixer.music.play(-1, 0)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_f:
                    if full == 0:
                        #screen = pygame.display.set_mode((infoObject))
                        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                        full = 1
                    else:
                        screen = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]))
                        full = 0
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        #pygame.draw.rect(screen, (255, 0, 0), button_1)
        #pygame.draw.rect(screen, (255, 0, 0), button_2)
        #pygame.draw.rect(screen, (255, 0, 0), button_3)
        pygame.display.update()
        clock.tick(60)
        screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
        
#####################################ACCUEIL####################################

    if game1 == True:
        has_coin = False
        pygame.mixer.music.load("music/FX/load.wav")
        pygame.mixer.music.play()
        while loadtime < 95:
                screen.blit(iloading, (0, 0))
                loadtime += 1
                pygame.display.update()
        loadtime = 0
        player_img = player1
        player_img.set_colorkey((255,255,255))
        #or pygame.mixer.music.load("music/lobbyloop.ogg") #je l'ai personellement crée pendant des jours de galère
        pygame.mixer.music.load("music/thefirststep.ogg")
        #or pygame.mixer.music.load("music/timetomove.ogg")
        pygame.mixer.music.play(-1, 0)
        game_map = load_map('map')
        player_rect[0] = 29.75*16
        player_rect[1] = 20*16
        
######################################LOBBY#####################################

    while game1:

        if grass_sound_timer > 0:
            grass_sound_timer -= 1

        if player_rect[1] > 40*16:
            #vie -= 1
            #print(vie)
            pygame.mixer.music.load('music/FX/deathsound.wav')
            pygame.mixer.music.play()
            screen.blit(ideath, (0,0))
            pygame.display.flip()
            time.sleep(5)
            player_rect[0] = 29.75*16
            player_rect[1] = 20*16
            pygame.mixer.music.load("music/thefirststep.ogg")
            pygame.mixer.music.play(-1, 0)
            
        if nuit == True:
            display.fill((3,34,76)) # screen blue night
        else:
            display.fill((146, 244, 255)) #screen blue day

        true_scroll[0] += (player_rect.x-true_scroll[0]-152)/20
        true_scroll[1] += (player_rect.y-true_scroll[1]-106)/20
        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])
    
        tile_rects = []
        y = 0
        for layer in game_map:
            x = 0
            for tile in layer:
                if tile == 'b':
                    display.blit(brick,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'q':
                    display.blit(Ddirt,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 's':
                    display.blit(Ldirt, (x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'd':
                    display.blit(DLdirt,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'o':
                    display.blit(DRdirt,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'u':
                    display.blit(Rdirt, (x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'f':
                    display.blit(Mdirt,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'w':
                    display.blit(Lgrass,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == '=':
                    display.blit(Mgrass, (x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'c':
                    display.blit(Rgrass,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'n':
                    display.blit(water,(x*16-scroll[0],y*16-scroll[1]))
                if tile == 'g':
                    display.blit(grotte, (x*16-scroll[0],y*16-scroll[1]))
                    grottetile = pygame.Rect(x*16,y*16,16,16)
                if tile == '^':
                    display.blit(trampoline, (x*16-scroll[0],y*16-scroll[1]))
                    trampolinetile = pygame.Rect(x*16,y*16,16,16)
                if tile == 'h':
                       display.blit(little_rock, (x*16-scroll[0],y*16-scroll[1]))
                if tile == '<':
                    display.blit(rock,(x*16-scroll[0],y*16-scroll[1]))
                if tile == 'm':
                    display.blit(flower,(x*16-scroll[0],y*16-scroll[1]))
                if tile == 'p':
                    display.blit(bottom_tree, (x*16-scroll[0],y*16-scroll[1]))
                if tile == 'z':
                    display.blit(middle_tree,(x*16-scroll[0],y*16-scroll[1]))
                if tile == 'v':
                    display.blit(top_tree,(x*16-scroll[0],y*16-scroll[1]))
                if tile == 'e':
                    display.blit(rock_plat, (x*16-scroll[0],y*16-scroll[1]))
                if tile == '°':
                    display.blit(box_type_1, (x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == ']':
                    display.blit(doormathias, (x*16-scroll[0],y*16-scroll[1]-7))
                    doortile = pygame.Rect(x*16,(y*16)-7,46,56)
                if tile == '!':
                    display.blit(open_door, (x*16-scroll[0],y*16-scroll[1]-7))
                    open_doortile = pygame.Rect(x*16,(y*16)-7,46,56)
                    
                if tile == 'i':
                    display.blit(box_type_2, (x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'a':
                    display.blit(buisson_fleurs, (x*16-scroll[0],y*16-scroll[1]))
                if tile == '}':
                    display.blit(cloud, (x*16-scroll[0],y*16-scroll[1]))
                if tile == '{':
                    display.blit(lvl3_house,(x*16-scroll[0], y*16-scroll[1]-96))
                    lobby_house_rect = pygame.Rect(x*16,(y*16)-96,144,112)
                if tile == '#':
                    display.blit(bottom_echelle,(x*16-scroll[0],y*16-scroll[1]))
                if tile == '@':
                    display.blit(echelle,(x*16-scroll[0],y*16-scroll[1]))                    
                if tile == 'ç':
                    display.blit(top_echelle,(x*16-scroll[0],y*16-scroll[1]))

                    
                if tile == '?':
                    display.blit(terrain_center_left,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == '%':
                    display.blit(terrain_center,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == '$':
                    display.blit(terrain_center_right,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == '£':
                    display.blit(tliane,(x*16-scroll[0],y*16-scroll[1]))
                if tile == '*':
                    display.blit(mliane,(x*16-scroll[0],y*16-scroll[1]))
                if tile == 'µ':
                    display.blit(bliane,(x*16-scroll[0],y*16-scroll[1]))
                if tile == 'z':
                    display.blit(middle_tree,(x*16-scroll[0],y*16-scroll[1]))
                if tile == '~':
                    display.blit(jewel_blue,(x*16-scroll[0],y*16-scroll[1]))
                if tile == 'é':
                    display.blit(jewel_yellow,(x*16-scroll[0],y*16-scroll[1]))
                if tile == '&':
                    display.blit(jewel_green,(x*16-scroll[0],y*16-scroll[1]))
                if tile == 'à':
                    display.blit(lvl3_sign,(x*16-scroll[0],y*16-scroll[1]))
                if tile == '#':
                    display.blit(bottom_echelle,(x*16-scroll[0],y*16-scroll[1]))
                if tile == '@':
                    display.blit(echelle,(x*16-scroll[0],y*16-scroll[1]))
                if tile == 'ç':
                    display.blit(top_echelle,(x*16-scroll[0],y*16-scroll[1]))
                if tile == '!':
                    display.blit(open_door,(x*16-scroll[0],y*16-scroll[1]))
                if tile == '+':
                    if nuit == True:
                        display.blit(mariostar,(x*16-scroll[0],y*16-scroll[1]))
                        mariostar.set_colorkey((255,255,255))
                        
                if tile == '2':
                    display.blit(objetscreen,(x*16-scroll[0],y*16-scroll[1]))
                if tile == '3':
                    display.blit(lifescreen,(x*16-scroll[0],y*16-scroll[1]))
                if done2 == True:
                    display.blit(check,(47*16-scroll[0],25*16-scroll[1]))
                if done3 == True:
                    display.blit(check,(55*16-scroll[0],17*16-scroll[1]))
                if done4 == True:
                    display.blit(check,(12*16-scroll[0],29*16-scroll[1]))

                x += 1
            y += 1
        #echelle et lianes
        lobby_grimpe1 = pygame.Rect(7*16, 17*16, 1*16, 9*16)
        lobby_grimpe2 = pygame.Rect(5*16, 3*16, 1*16, 13*16)
        #fin echelle et lianes

        player_movement = [0,0]
        if moving_right == True:
                player_movement[0] += 2
        if moving_left == True:
                player_movement[0] -= 2
        
        if player_rect.colliderect(lobby_grimpe1) or player_rect.colliderect(lobby_grimpe2):
                air_timer = 0
                vertical_momentum = 0
                if moving_up == True:
                        player_movement[1] -= 2
                if moving_down == True:
                        player_movement[1] += 2
        else:
                player_movement[1] += vertical_momentum
                vertical_momentum += 0.2
                if vertical_momentum > 3.5:
                        vertical_momentum = 3.5
                if vertical_momentum < -5:
                        vertical_momentum = -5

        player_rect,collisions = move(player_rect,player_movement,tile_rects)

        if collisions['bottom'] == True:
                if air_timer > 15:
                        land_sound.play()
                air_timer = 0
                vertical_momentum = 0
                if player_movement[0] != 0:
                        if collisions['right'] == False and collisions['left'] == False:
                                if grass_sound_timer == 0:
                                        grass_sound_timer = 30
                                        random.choice(grass_sounds).play()
        else:
                air_timer += 1

        display.blit(player_img,(player_rect.x-scroll[0],player_rect.y-scroll[1]))

        if vie == 3:
            lifescreen = vie3
        if vie == 2:
            lifescreen = vie2
        if vie == 1:
            lifescreen = vie1

        if objet == 0:
            objetscreen = objet0
        if objet == 1:
            objetscreen = objet1
        if objet == 2:
            objetscreen = objet2
        if objet == 3:
            objetscreen = objet3
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                #warp start
                if event.key == K_x:
                        if player_rect.colliderect(lobby_house_rect) and done2 == False:
                                game2 = 1
                                game1 = 0
                                gametimer = 0
                        if player_rect.colliderect(doortile) and done3 == False:
                                game3 = 1
                                game1 = 0
                                gametimer = 0
                        if player_rect.colliderect(grottetile) and done4 == False:
                                game4 = 1
                                game1 = 0
                                gametimer = 0
                #warp ends
                if event.key == K_f:
                    if full == 0:
                        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                        full = 1

                    else:
                        screen = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]))
                        full = 0

                if event.key == K_n:
                        if nuit == True:
                                nuit = False
                        else:
                                nuit = True

                if event.key == K_ESCAPE:
                    game1 = 0
                    game2 = 0
                    game3 = 0
                    game4 = 0
                    accueil = 1

                if event.key == K_RIGHT or event.key == K_d:
                        moving_right = True

                if event.key == K_LEFT or event.key == K_q:
                        moving_left = True

                if event.key == K_UP or event.key == K_z:
                        if player_rect.colliderect(lobby_grimpe1) or player_rect.colliderect(lobby_grimpe2):
                                moving_up = True
                        elif air_timer < 6 or god == 1:
                                jump_sound.play()
                                vertical_momentum = -5

                if event.key == K_DOWN or event.key == K_s:
                        if player_rect.colliderect(lobby_grimpe1) or player_rect.colliderect(lobby_grimpe2):
                                moving_down = True
        if event.type == KEYUP:
                if event.key == K_RIGHT or event.key == K_d:
                        moving_right = False

                if event.key == K_LEFT or event.key == K_q:
                        moving_left = False

                if event.key == K_UP or event.key == K_z:
                        moving_up = False

                if event.key == K_DOWN or event.key == K_s:
                        moving_down = False

        print(player_rect[0]/16, player_rect[1]/16)
        screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
        pygame.display.update()
        clock.tick(60)
        #print("lobby fps:", update_fps())
        

######################################LOBBY#####################################

    
###############################GAME PREPARATION 2###############################

    moving_right = False
    moving_left = False
    speed = False
    vertical_momentum = 0
    air_timer = 0

    if game2 == True:
        player_rect[1] = 16.25*16
        player_rect[0] = 14*16
        pygame.mixer.music.load("music/FX/load.wav")
        pygame.mixer.music.play()
        while loadtime < 95:
                screen.blit(iloading, (0, 0))
                loadtime += 1
                pygame.display.update()
        loadtime = 0
        player_img = player2
        player_img.set_colorkey((255,255,255))
        pygame.mixer.music.load("music/mystified.ogg")
        pygame.mixer.music.play(-1, 0)
        game_map2 = load_map('map2')
        has_coin = False

###############################GAME PREPARATION 2###############################


##################################MATTIS MAP####################################

    while game2:

        if grass_sound_timer > 0:
            grass_sound_timer -= 1

        if player_rect[1] > 400:
            vie -= 1
            #print(vie)
            pygame.mixer.music.load('music/FX/deathsound.wav')
            pygame.mixer.music.play()
            screen.blit(ideath, (0,0))
            pygame.display.flip()
            time.sleep(5)
            player_rect[0] = 416
            player_rect[1] = 496          
            game2 = 0
            game1 = 1
            #gametimer = 0
            
        display.fill((146,244,255)) # clear screen by filling it with blue
        true_scroll[0] += (player_rect.x-true_scroll[0]-152)/20
        true_scroll[1] += (player_rect.y-true_scroll[1]-106)/20
        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])
        #display.blit(lvl3_background, (player_rect[0], player_rect[1]))
    
        tile_rects = []
        y = 0
        for layer in game_map2:
            x = 0
            for tile in layer:
                if tile == 'a':
                    display.blit(lvl3_face_block,(x*16-scroll[0],y*16-scroll[1]-16))
                    tile_rects.append(pygame.Rect(x*16,(y*16)-16,32,32))
                if tile == 'b':
                    display.blit(lvl3_grass,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'c':
                    display.blit(lvl3_rock2,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'd':
                    display.blit(lvl3_rock3,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'e':
                    display.blit(lvl3_rock1_R,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'f':
                    display.blit(lvl3_rock1_L,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'g':
                    display.blit(lvl3_tree,(x*16-scroll[0],y*16-scroll[1]-140))
                if tile == 'h':
                    display.blit(lvl3_herb2,(x*16-scroll[0],y*16-scroll[1]))
                if tile == 'i':
                    display.blit(lvl3_crate,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'j':
                    display.blit(lvl3_platform,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,64,16))
                if tile == 'k':
                    display.blit(lvl3_rock6,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'l':
                    display.blit(lvl3_rock4,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'm':
                    display.blit(lvl3_rock5,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'n':
                    display.blit(lvl3_spikes,(x*16-scroll[0],y*16-scroll[1]))
                if tile == 'o':
                    display.blit(lvl3_house,(x*16-scroll[0],y*16-scroll[1]-96))
                    lvl3_house_rect = pygame.Rect(x*16,(y*16)-96,144,112)
                if tile == 'p':
                    display.blit(lvl3_block,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'q':
                    display.blit(lvl3_big_block,(x*16-scroll[0],y*16-scroll[1]-14))
                    tile_rects.append(pygame.Rect(x*16,(y*16)-14,32,32))
                if tile == 'r':
                    display.blit(lvl3_sign,(x*16-scroll[0],y*16-scroll[1]))
                if has_coin == False:
                        if tile == 's':
                                display.blit(coin, (x*16-scroll[0], y*16 - scroll[1]))
                                coin_rect = pygame.Rect(x*16, y*16, 16, 16)
                x += 1
            y += 1


    #objects start
        if player_rect.colliderect(coin_rect):
                if has_coin == False:
                        coin_sound.play()
                has_coin = True
                
    #spikes collisions
        spikes_rect1 = pygame.Rect(15*16, 12*16, 16*5, 16)
        spikes_rect2 = pygame.Rect(24*16, 11*16, 16*4, 16)
        spikes_rect3 = pygame.Rect(30*16, 11*16, 16*5, 16)
        spikes_rect4 = pygame.Rect(49*16, 15*16, 16, 16)
        spikes_rect5 = pygame.Rect(53*16, 15*16, 16*23, 16)
        spikes_rect6 = pygame.Rect(77*16, 15*16, 16*2, 16)
        spikes_rect7 = pygame.Rect(80*16, 15*16, 16*2, 16)
    #end spikes collisions

        if player_rect.colliderect(spikes_rect1) or player_rect.colliderect(spikes_rect2) or player_rect.colliderect(spikes_rect3) or player_rect.colliderect(spikes_rect4) or player_rect.colliderect(spikes_rect5) or player_rect.colliderect(spikes_rect6) or player_rect.colliderect(spikes_rect7):
            vie -= 1
            #print(vie)
            pygame.mixer.music.load('music/FX/deathsound.wav')
            pygame.mixer.music.play()
            screen.blit(ideath, (0,0))
            pygame.display.flip()
            time.sleep(5)
            player_rect[0] = 416
            player_rect[1] = 496          
            game2 = 0
            game1 = 1
#            gametimer = 0

#        if gametimer > 1000:
 #           mort += 1
  #          print(mort)
   #         death_sound.play()
    #        screen.blit(ideath, (0,0))
     #       pygame.display.flip()
      #      time.sleep(5)
       #     player_rect[0] = 416
        #    player_rect[1] = 496          
         #   game2 = 0
          #  game1 = 1
           # gametimer = 0

    #objects end

        player_movement = [0,0]
        if moving_right == True:
            if speed == True:
                player_movement[0] += 3
            else:
                player_movement[0] += 2
        if moving_left == True:
            if speed == True:
                player_movement[0] -= 3
            else:
                player_movement[0] -= 2
            
        player_movement[1] += vertical_momentum
        vertical_momentum += 0.2
        if vertical_momentum > 3:
            vertical_momentum = 3
        if vertical_momentum < -5:
            vertical_momentum = -5

        player_rect,collisions = move(player_rect,player_movement,tile_rects)

        if collisions['bottom'] == True:
            if air_timer > 15:
                land_sound.play()
            air_timer = 0
            vertical_momentum = 0
            if player_movement[0] != 0:
                if collisions['right'] == False and collisions['left'] == False:
                        if grass_sound_timer == 0:
                                grass_sound_timer = 30
                                random.choice(grass_sounds).play()
        else:
            air_timer += 1

        display.blit(player_img,(player_rect.x-scroll[0],player_rect.y-scroll[1]))


        for event in pygame.event.get(): # event loop
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:    
                if event.key == K_x:
                    if player_rect.colliderect(lvl3_house_rect):
                        if has_coin == True:
                                objet += 1
                                done2 = True
                        game2 = 0
                        game1 = 1
                        

                if event.key == K_ESCAPE:          
                    game2 = 0
                    game1 = 1
#                   gametimer = 0

                if event.key == K_f:
                    if full == 0:
                        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                        full = 1
                    else:
                        screen = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]))
                        full = 0

                if event.key == K_SPACE:
                    speed = True
                if event.key == K_RIGHT or event.key == K_d:
                    moving_right = True
                if event.key == K_LEFT or event.key == K_q:
                    moving_left = True
                if event.key == K_UP or event.key == K_z:
                    if air_timer < 6 or god == 1:
                        jump_sound.play()
                        vertical_momentum = -3.5

            if event.type == KEYUP:
                if event.key == K_SPACE:
                    speed = False
                if event.key == K_RIGHT or event.key == K_d:
                    moving_right = False
                if event.key == K_LEFT or event.key == K_q:
                    moving_left = False
                    
        screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
        pygame.display.update()
        clock.tick(60)
#       print(player_rect[0]/16, player_rect[1]/16)
#       print("game2:", update_fps())
#       gametimer += 1

##################################MATTIS MAP####################################


###############################GAME PREPARATION 3###############################
    
    d_jump = 0
    moving_right = False
    moving_left = False
    vertical_momentum = 0
    air_timer = 0

    true_scroll = [0,0]

    if game3 ==  True:
        pygame.mixer.music.load("music/FX/load.wav")
        pygame.mixer.music.play()
        while loadtime < 95:
                screen.blit(iloading, (0, 0))
                loadtime += 1
                pygame.display.update()
        loadtime = 0
        player_img = player3
        player_img.set_colorkey((255,255,255))
        pygame.mixer.music.load("music/submerged.ogg")
        pygame.mixer.music.play(-1, 0)
        game_map3 = load_map('map3')
        player_rect[1] = 1200
        player_rect[0] = 100
        has_coin = False

###############################GAME PREPARATION 3###############################

##################################MATHIAS MAP##################################

    
    while game3:

        if grass_sound_timer > 0:
            grass_sound_timer -= 1

        if player_rect[1] > 1500:
            vie -= 1
            #print(vie)
            pygame.mixer.music.load('music/FX/deathsound.wav')
            pygame.mixer.music.play()
            screen.blit(ideath, (0,0))
            pygame.display.flip()
            time.sleep(5)        
            game3 = 0
            game1 = 1
            
        display.fill((146,244,255)) # clear screen by filling it with blue

        true_scroll[0] += (player_rect.x-true_scroll[0]-152)/20
        true_scroll[1] += (player_rect.y-true_scroll[1]-106)/20
        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])
    
        tile_rects = []
        y = 0
        for layer in game_map3:
            x = 0
            for tile in layer:

                if tile == 'c':
                    display.blit(terrain_slope_floor_A,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'j':
                    display.blit(terrain_center, (x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'b':
                    display.blit(terrain_slope_floor_B,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'a':
                    display.blit(terrain_top_center,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'e':
                    display.blit(terrain_slope_ceiling_A, (x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'd':
                    display.blit(terrain_slope_ceiling_B,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'g':
                    display.blit(terrain_corner_inner_bottom_left,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'f':
                    display.blit(terrain_corner_inner_bottom_right, (x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'i':
                    display.blit(terrain_center_left,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'h':
                    display.blit(terrain_center_right, (x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'z':
                    display.blit(doormathias, (x*16-scroll[0],y*16-scroll[1]-7))
                    doortile = pygame.Rect(x*16,(y*16)-7,46,56)
                if tile == '3':
                    display.blit(jewel_yellow, (x*16-scroll[0],y*16-scroll[1]))
                    jewel_yellow_rect = pygame.Rect(x*16,y*16,16,16)
                if tile == '4':
                    display.blit(jewel_blue, (x*16-scroll[0],y*16-scroll[1]))
                    jewel_blue_rect = pygame.Rect(x*16,y*16,16,16)
                if tile == '1':
                    #display.blit(terrain_center_left,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))


                    
                if tile == '2':
                    display.blit(terrain_center2,(x*16-scroll[0],y*16-scroll[1]))     
                if tile == 't':
                    display.blit(midground_center,(x*16-scroll[0],y*16-scroll[1]))                
                if tile == 'y':
                    display.blit(cloud1,(x*16-scroll[0],y*16-scroll[1]))
                if tile == 'x':
                    display.blit(cloud2,(x*16-scroll[0],y*16-scroll[1]))
                if tile == 'u':
                    display.blit(cloud4, (x*16-scroll[0],y*16-scroll[1]))
                if tile == 'v':
                    display.blit(cloud3, (x*16-scroll[0],y*16-scroll[1]))
                if tile == 'k':
                    display.blit(midground_right_C_shadowed,(x*16-scroll[0],y*16-scroll[1]))
                if tile == 'l':
                    display.blit(midground_right_C,(x*16-scroll[0],y*16-scroll[1]))
                if tile == 'm':
                    display.blit(midground_right_B, (x*16-scroll[0],y*16-scroll[1]))
                if tile == 'n':
                    display.blit(midground_right_A_shadowed,(x*16-scroll[0],y*16-scroll[1]))
                if tile == 'o':
                    display.blit(midground_right_A,(x*16-scroll[0],y*16-scroll[1]))
                if tile == 'p':
                    display.blit(midground_left_C, (x*16-scroll[0],y*16-scroll[1]))
                if tile == 'q':
                    display.blit(midground_left_B,(x*16-scroll[0],y*16-scroll[1]))
                if tile == 'r':
                    display.blit(midground_left_A_shadowed, (x*16-scroll[0],y*16-scroll[1]))
                if tile == 's':
                    display.blit(midground_left_A, (x*16-scroll[0],y*16-scroll[1]))
                if tile == 'w':
                    display.blit(midground_left_C_shadowed, (x*16-scroll[0],y*16-scroll[1]))
                if has_coin == False:
                        if tile == '5':
                                display.blit(coin, (x*16-scroll[0],y*16-scroll[1]))
                                coin_rect = pygame.Rect(x*16, y*16, 16, 16)

                x += 1
            y += 1


    #objects start
        if player_rect.colliderect(coin_rect):
                if has_coin == False:
                        coin_sound.play()
                has_coin = True
                
        if player_rect.colliderect(jewel_yellow_rect):
            player_rect[1] = 0
            player_rect[0] = 70*16
        if player_rect.colliderect(jewel_blue_rect):
            player_rect[1] = 62*16
            player_rect[0] = 4*16


        if gametimer > 2100:
            vie -= 1
            #print(vie)
            pygame.mixer.music.load('music/FX/deathsound.wav')
            pygame.mixer.music.play()
            screen.blit(ideath, (0,0))
            pygame.display.flip()
            time.sleep(5)
            player_rect[0] = 416
            player_rect[1] = 496          
            game3 = 0
            game1 = 1
            gametimer = 0

    #objects end

        player_movement = [0,0]
        if moving_right == True:
            player_movement[0] += 2
        if moving_left == True:
            player_movement[0] -= 2
        player_movement[1] += vertical_momentum
        vertical_momentum += 0.2
        if vertical_momentum > 3:
            vertical_momentum = 3
        if vertical_momentum < -5:
            vertical_momentum = -5

        player_rect,collisions = move(player_rect,player_movement,tile_rects)

        if collisions['bottom'] == True:
            if air_timer > 15:
                land_sound.play()
            air_timer = 0
            vertical_momentum = 0
            d_jump = 0
            if player_movement[0] != 0:
                if collisions['right'] == False and collisions['left'] == False:
                        if grass_sound_timer == 0:
                                grass_sound_timer = 30
                                random.choice(grass_sounds).play()
        else:
            air_timer += 1

        display.blit(player_img,(player_rect.x-scroll[0],player_rect.y-scroll[1]))


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:         
                    game3 = 0
                    game1 = 1
                    loadtime = 0
                if event.key == K_x:
                    if player_rect.colliderect(doortile):
                        if has_coin == True:
                                done3 = True
                                objet += 1
                        game1 = 1
                        game3 = 0
                        loadtime = 0
#                        win2 = 1
                if event.key == K_RIGHT or event.key == K_d:
                    moving_right = True
                if event.key == K_LEFT or event.key == K_q:
                    moving_left = True
                if event.key == K_UP or event.key == K_z:
                    if air_timer < 6 or d_jump < 2 or god == 1:
                        jump_sound.play()
                        vertical_momentum = -5
                        d_jump += 1

                if event.key == K_f:
                    if full == 0:
                        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                        full = 1
                    else:
                        screen = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]))
                        full = 0

            if event.type == KEYUP:
                if event.key == K_RIGHT or event.key == K_d:
                    moving_right = False
                if event.key == K_LEFT or event.key == K_q:
                    moving_left = False
                    
        screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
        pygame.display.update()
        clock.tick(60)
        gametimer += 1
#       print("game3:", update_fps())
#       print(player_rect[0]/16, player_rect[1]/16)

#################################MATHIAS MAP###################################


###############################GAME PREPARATION 4###############################
    
    moving_right = False
    moving_left = False
    vertical_momentum = 0
    air_timer = 0

    if game4 == True:
        pygame.mixer.music.load("music/FX/load.wav")
        pygame.mixer.music.play()
        while loadtime < 95:
                screen.blit(iloading, (0, 0))
                loadtime += 1
                pygame.display.update()
        loadtime = 0
        player_img = player4
        player_img.set_colorkey((255,255,255))
        pygame.mixer.music.load("music/ancestors.ogg")
        pygame.mixer.music.play(-1, 0)
        game_map4 = load_map('map4')
        player_rect[1] = 25*16
        player_rect[0] = 8*16
        has_coin = False

###############################GAME PREPARATION 4###############################

###################################THOMAS MAP###################################
    
    while game4:

        if grass_sound_timer > 0:
            grass_sound_timer -= 1

        if player_rect[1] > 1280:
            vie -= 1
            #print(vie)
            pygame.mixer.music.load('music/FX/deathsound.wav')
            pygame.mixer.music.play()
            screen.blit(ideath, (0,0))
            pygame.display.flip()
            time.sleep(5)         
            game4 = 0
            game1 = 1

            
        display.fill((3,34,76)) # clear screen by filling it with blue
        true_scroll[0] += (player_rect.x-true_scroll[0]-152)/20
        true_scroll[1] += (player_rect.y-true_scroll[1]-106)/20
        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])

        tile_rects = []
        y = 0
        for layer in game_map4:
            x = 0
            for tile in layer:
                if tile == 'a':
                    display.blit(flechegauche,(x*16-scroll[0],y*16-scroll[1]-16))
                    flechegauche.set_colorkey((255,255,255))
                if tile == 'b':
                    display.blit(flechedroite,(x*16-scroll[0],y*16-scroll[1]))
                    flechedroite.set_colorkey((255,255,255))
                if tile == 'c':
                    display.blit(flechebas,(x*16-scroll[0],y*16-scroll[1]))
                    flechebas.set_colorkey((255,255,255))
                if tile == 'd':
                    display.blit(terrain_center,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'e':
                    display.blit(doormathias,(x*16-scroll[0],y*16-scroll[1]-7))
                    doortile = pygame.Rect(x*16,(y*16)-7,46,56)
                if tile == 'f':
                    display.blit(trampoline,(x*16-scroll[0],y*16-scroll[1]))
                    #tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'g':
                    display.blit(rock_plat,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'h':
                    display.blit(lvl3_spikes,(x*16-scroll[0],y*16-scroll[1]))
                    #tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'i':
                    display.blit(mliane,(x*16-scroll[0],y*16-scroll[1]))
                    #tile_rects4.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'j':
                    display.blit(Mgrass,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'k':
                    display.blit(jewel_yellow,(x*16-scroll[0],y*16-scroll[1]))
                    #tile_rects4.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'l':
                    display.blit(jewel_blue,(x*16-scroll[0],y*16-scroll[1]))
                    #tile_rects4.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'm':
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'n':
                    display.blit(brick,(x*16-scroll[0],y*16-scroll[1]))
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'o':
                    display.blit(bliane,(x*16-scroll[0],y*16-scroll[1]))
                    #tile_rects4.append(pygame.Rect(x*16,y*16,16,16))
                if tile == 'p':
                    display.blit(rock_plat,(x*16-scroll[0],y*16-scroll[1]))
                if has_coin == False:
                        if tile == 'q':
                                display.blit(coin, (x*16-scroll[0], y*16 - scroll[1]))
                                coin_rect = pygame.Rect(x*16, y*16, 16, 16)
                x += 1
            y += 1


    #objects start

    #spikes collisions + trampo
        lvl4_trampo_rect = pygame.Rect(72*16, 72*16, 16*2, 16)
        lvl4_spikes_rect1 = pygame.Rect(21*16, 31*16, 19*16, 16)
        lvl4_spikes_rect2 = pygame.Rect(72*16, 32*16, 16*2, 16)
        lvl4_spikes_rect3 = pygame.Rect(51*16, 179, 16*5, 16)
        lvl4_spikes_rect4 = pygame.Rect(809, 179, 16*2, 25*16)
        lvl4_spikes_rect5 = pygame.Rect(872, 179, 16*2, 25*16)
        lvl4_spikes_rect6 = pygame.Rect(79*16, 44*16, 3*16, 16)
        lvl4_spikes_rect7 = pygame.Rect(86*16, 44*16, 3*16, 16)
        lvl4_spikes_rect8 = pygame.Rect(92*16, 41*16, 3*16, 16)
        lvl4_spikes_rect9 = pygame.Rect(96*16, 44*16, 3*16, 16)
        lvl4_spikes_rect10 = pygame.Rect(93*16, 47*16, 3*16, 16)
        lvl4_spikes_rect11 = pygame.Rect(80*16, 47*16, 3*16, 16)
        lvl4_spikes_rect12 = pygame.Rect(99*16, 48*16, 2*16, 16)
        lvl4_spikes_rect13 = pygame.Rect(89*16, 49*16, 3*16, 16)
        lvl4_spikes_rect14 = pygame.Rect(78*16, 50*16, 3*16, 16)
        lvl4_spikes_rect15 = pygame.Rect(84*16, 52*16, 3*16, 16)
        lvl4_spikes_rect16 = pygame.Rect(94*16, 52*16, 3*16, 16)
        lvl4_spikes_rect17 = pygame.Rect(79*16, 54*16, 3*16, 16)
        lvl4_spikes_rect18 = pygame.Rect(97*16, 55*16, 3*16, 16)
        lvl4_spikes_rect19 = pygame.Rect(94*16, 57*16, 2*16, 16)
        lvl4_spikes_rect20 = pygame.Rect(96*16, 60*16, 3*16, 16)
        lvl4_spikes_rect21 = pygame.Rect(91*16, 62*16, 3*16, 16)
        lvl4_spikes_rect22 = pygame.Rect(84*16, 60*16, 3*16, 16)
        lvl4_spikes_rect23 = pygame.Rect(80*16, 58*16, 3*16, 16)
        lvl4_spikes_rect24 = pygame.Rect(99*16, 64*16, 2*16, 16)
        lvl4_spikes_rect25 = pygame.Rect(80*16, 63*16, 4*16, 16)
        lvl4_spikes_rect26 = pygame.Rect(86*16, 66*16, 3*16, 16)
        lvl4_spikes_rect27 = pygame.Rect(91*16, 67*16, 3*16, 16)
        lvl4_spikes_rect28 = pygame.Rect(96*16, 66*16, 3*16, 16)
        lvl4_spikes_rect29 = pygame.Rect(80*16, 68*16, 3*16, 16)
        lvl4_spikes_rect30 = pygame.Rect(87*16, 70*16, 3*16, 16)
        lvl4_spikes_rect31 = pygame.Rect(80*16, 72*16, 3*16, 16)
        lvl4_spikes_rect32 = pygame.Rect(97*16, 70*16, 3*16, 16)
        lvl4_spikes_rect33 = pygame.Rect(88*16, 57*16, 3*16, 16)
        lvl4_spikes_rect34 = pygame.Rect(78*16, 76*16, 13*16, 16)
        lvl4_spikes_rect35 = pygame.Rect(96*16, 76*16, 5*16, 16)
        lvl4_spikes_rect36 = pygame.Rect(91*16, 72*16, 2*16, 16)
        lvl4_spikes_rect37 = pygame.Rect(94*16, 72*16, 2*16, 16)
        lvl4_spikes_rect38 = pygame.Rect(91*16, 75*16, 2*16, 16)
        lvl4_spikes_rect39 = pygame.Rect(94*16, 75*16, 2*16, 16)
        lvl4_spikes_rect40 = pygame.Rect(38*16, 41*16, 16, 2*16)
        lvl4_spikes_rect41 = pygame.Rect(37*16, 43*16, 16, 4*16)
        lvl4_spikes_rect42 = pygame.Rect(36*16, 47*16, 16, 2*16)
        lvl4_spikes_rect43 = pygame.Rect(35*16, 46*16, 16, 16)
        lvl4_spikes_rect44 = pygame.Rect(34*16, 45*16, 16, 16)
        lvl4_spikes_rect45 = pygame.Rect(33*16, 43*16, 16, 2*16)
        lvl4_spikes_rect46 = pygame.Rect(32*16, 41*16, 16, 2*16)
        lvl4_spikes_rect47 = pygame.Rect(26*16, 42*16, 16, 5*16)
        lvl4_spikes_rect48 = pygame.Rect(38*16, 41*16, 16, 2*16)
        lvl4_spikes_rect49 = pygame.Rect(35*16, 49*16, 16, 3*16)
        lvl4_spikes_rect50 = pygame.Rect(34*16, 52*16, 16, 16)
        lvl4_spikes_rect51 = pygame.Rect(33*16, 53*16, 16, 16)
        lvl4_spikes_rect52 = pygame.Rect(32*16, 52*16, 16, 16)
        lvl4_spikes_rect53 = pygame.Rect(31*16, 51*16, 16, 16)
        lvl4_spikes_rect54 = pygame.Rect(30*16, 50*16, 16, 16)
        lvl4_spikes_rect55 = pygame.Rect(29*16, 49*16, 16, 16)
        
    #end spikes collisions

        if player_rect.colliderect(coin_rect):
                if has_coin == False:
                        coin_sound.play()
                has_coin = True

        if player_rect.colliderect(lvl4_trampo_rect):
                vertical_momentum -= 20

        if player_rect.colliderect(lvl4_spikes_rect1) or player_rect.colliderect(lvl4_spikes_rect2) or player_rect.colliderect(lvl4_spikes_rect3) or player_rect.colliderect(lvl4_spikes_rect4) or player_rect.colliderect(lvl4_spikes_rect5) or player_rect.colliderect(lvl4_spikes_rect6) or player_rect.colliderect(lvl4_spikes_rect7) or player_rect.colliderect(lvl4_spikes_rect8) or player_rect.colliderect(lvl4_spikes_rect9) or player_rect.colliderect(lvl4_spikes_rect10) or player_rect.colliderect(lvl4_spikes_rect11) or player_rect.colliderect(lvl4_spikes_rect12) or player_rect.colliderect(lvl4_spikes_rect13) or player_rect.colliderect(lvl4_spikes_rect14) or player_rect.colliderect(lvl4_spikes_rect15) or player_rect.colliderect(lvl4_spikes_rect16) or player_rect.colliderect(lvl4_spikes_rect17) or player_rect.colliderect(lvl4_spikes_rect18) or player_rect.colliderect(lvl4_spikes_rect19) or player_rect.colliderect(lvl4_spikes_rect20) or player_rect.colliderect(lvl4_spikes_rect21) or player_rect.colliderect(lvl4_spikes_rect22) or player_rect.colliderect(lvl4_spikes_rect23) or player_rect.colliderect(lvl4_spikes_rect24) or player_rect.colliderect(lvl4_spikes_rect25) or player_rect.colliderect(lvl4_spikes_rect26) or player_rect.colliderect(lvl4_spikes_rect27) or player_rect.colliderect(lvl4_spikes_rect28) or player_rect.colliderect(lvl4_spikes_rect29) or player_rect.colliderect(lvl4_spikes_rect30) or player_rect.colliderect(lvl4_spikes_rect31) or player_rect.colliderect(lvl4_spikes_rect32) or player_rect.colliderect(lvl4_spikes_rect33) or player_rect.colliderect(lvl4_spikes_rect34) or player_rect.colliderect(lvl4_spikes_rect35) or player_rect.colliderect(lvl4_spikes_rect36) or player_rect.colliderect(lvl4_spikes_rect37) or player_rect.colliderect(lvl4_spikes_rect38) or player_rect.colliderect(lvl4_spikes_rect39) or player_rect.colliderect(lvl4_spikes_rect40) or player_rect.colliderect(lvl4_spikes_rect41) or player_rect.colliderect(lvl4_spikes_rect42) or player_rect.colliderect(lvl4_spikes_rect43) or player_rect.colliderect(lvl4_spikes_rect44) or player_rect.colliderect(lvl4_spikes_rect45) or player_rect.colliderect(lvl4_spikes_rect46) or player_rect.colliderect(lvl4_spikes_rect47) or player_rect.colliderect(lvl4_spikes_rect48) or player_rect.colliderect(lvl4_spikes_rect49) or player_rect.colliderect(lvl4_spikes_rect50) or player_rect.colliderect(lvl4_spikes_rect51) or player_rect.colliderect(lvl4_spikes_rect52) or player_rect.colliderect(lvl4_spikes_rect53) or player_rect.colliderect(lvl4_spikes_rect54) or player_rect.colliderect(lvl4_spikes_rect55):
            print('touché')
            #vie -= 1
            #print(vie)
            #pygame.mixer.music.load('music/FX/deathsound.wav')
            #pygame.mixer.music.play()
            #screen.blit(ideath, (0,0))
            #pygame.display.flip()
            #time.sleep(5)
            #game4 = 0
            #game1 = 1

        #jewels warp
        if player_rect.colliderect(pygame.Rect(11*16,70*16,16,16)):
            player_rect[1] = 29*16
            player_rect[0] = 14*16
        if player_rect.colliderect(pygame.Rect(42*16,31*16,16,16)):
            player_rect[1] = 72*16
            player_rect[0] = 48*16
        if player_rect.colliderect(pygame.Rect(93*16,75*16,16,16)):
            player_rect[1] = 13*16
            player_rect[0] = 53*16
        if player_rect.colliderect(pygame.Rect(58*16,39*16,16,16)):
            player_rect[1] = 32*16
            player_rect[0] = 8*16
        #end jewels warp
            
        player_movement = [0,0]
        if moving_right == True:
            player_movement[0] += 2
        if moving_left == True:
            player_movement[0] -= 2
        player_movement[1] += vertical_momentum
        vertical_momentum += 0.15
        if vertical_momentum > 1.5:
            vertical_momentum = 1.5

        player_rect,collisions = move(player_rect,player_movement,tile_rects)

        if collisions['bottom'] == True:
            if air_timer > 15:
                land_sound.play()
            air_timer = 0
            vertical_momentum = 0
            if player_movement[0] != 0:
                if collisions['right'] == False and collisions['left'] == False:
                        if grass_sound_timer == 0:
                                grass_sound_timer = 30
                                random.choice(grass_sounds).play()
        else:
            air_timer += 1

        display.blit(player_img,(player_rect.x-scroll[0],player_rect.y-scroll[1]))


        for event in pygame.event.get(): # event loop
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_x:
                    if player_rect.colliderect(doortile):
                        if has_coin == True:
                                done4 = True
                                objet += 1
                        game4 = 0
                        game1 = 1
                        loadtime = 0

                if event.key == K_ESCAPE:
                    game4 = 0
                    game1 = 1
                    gametimer = 0
                    loadtime = 0

                if event.key == K_f:
                    if full == 0:
                        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                        full = 1
                    else:
                        screen = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]))
                        full = 0

                if event.key == K_RIGHT or event.key == K_d:
                    moving_right = True
                if event.key == K_LEFT or event.key == K_q:
                    moving_left = True
                if event.key == K_UP or event.key == K_z:
                    if air_timer < 6 or god == 1:
                        jump_sound.play()
                        vertical_momentum = -5

            if event.type == KEYUP:
                if event.key == K_RIGHT or event.key == K_d:
                    moving_right = False
                if event.key == K_LEFT or event.key == K_q:
                    moving_left = False
        screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
        pygame.display.update()
        clock.tick(60)
        #print("game4 fps:", update_fps())
        #print(player_rect[0]/16, player_rect[1]/16)

###################################THOMAS MAP###################################

###############################GLOBAL GAME LOOP#################################
