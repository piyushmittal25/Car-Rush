import pygame
import random
pygame.init()

crash_sound=pygame.mixer.Sound("crashsound.wav")
pygame.mixer.music.load("MarshmelloAlone.wav")

frame_per_sec=50

window_width=886
window_height=600
game_container_width=window_width-96
game_display=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Car-Rush")
white=(255,255,255)
RED=(240,0,0)
bright_red=(255,0,0)
BLACK=(0,0,0)
clock=pygame.time.Clock()
car_width=77
car_height=126
# carimage= pygame.image.load('car1.png')
car_icon=pygame.image.load("cargame_icon.png")
pygame.display.set_icon(car_icon)
image_width=80

cars=[]
cars.append(pygame.image.load("gamer_car1.png"))
cars.append(pygame.image.load("gamer_car2.png"))
cars.append(pygame.image.load("gamer_car3.png"))
cars.append(pygame.image.load("gamer_car4.png"))
cars.append(pygame.image.load("gamer_car5.png"))
cars.append(pygame.image.load("gamer_car6.png"))
cars.append(pygame.image.load("gamer_car7.png"))
cars.append(pygame.image.load("car2.png"))
cars.append(pygame.image.load("car3.png"))
cars.append(pygame.image.load("car5.png"))
cars.append(pygame.image.load("car6.png"))
cars.append(pygame.image.load("car7.png"))
cars.append(pygame.image.load("car8.png"))
cars.append(pygame.image.load("car9.png"))

road_image=pygame.image.load("final_road 2.jpg")

pause=False

def quitgame():
    pygame.quit()
    quit()

def message_develop(text,text_font,color):
    text_surface=text_font.render(text,True,color)
    textrect=text_surface.get_rect()
    return text_surface,textrect

def message_display(text,x,y,color):
    text_font=pygame.font.Font('NosiferCaps-Regular.ttf',40)
    text_surface,text_rect= message_develop(text,text_font,color)
    text_rect.center=(x,y)
    game_display.blit(text_surface,text_rect)

def button(text,startx,starty,wi,he,ac,ic,action=None):
    mouse = pygame.mouse.get_pos()
    mouse_pressed=pygame.mouse.get_pressed()
    if startx+wi > mouse[0] > startx and starty+he > mouse[1] > starty:
        pygame.draw.rect(game_display,ac, [startx,starty,wi,he])
        if action!=None and mouse_pressed[0]==1:
            action()
    else:
        pygame.draw.rect(game_display, ic, [startx,starty,wi,he])

    textfont=pygame.font.SysFont(None,he-4)
    text_surface,text_rect=message_develop(text,textfont,BLACK)
    text_rect.center=(startx+wi/2,starty+he/2)
    game_display.blit(text_surface,text_rect)

def first_page():
        high_score_file = open("high_score.txt", "r")
        highest_score = int(high_score_file.read())
        high_score_file.close()

        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()

            game_display.fill(white)

            message_display("BEST SCORE:"+str(highest_score),game_container_width//2,window_height*0.7,BLACK)
            text_font = pygame.font.Font('NosiferCaps-Regular.ttf',38)
            text_surface, text_rect = message_develop("Let's Enter The Era of Game", text_font,BLACK)
            text_rect.center = (window_width * 0.5, window_height * 0.4)
            game_display.blit(text_surface, text_rect)

            button("Start",window_width*0.2,window_height*0.5,100,60,bright_red,RED,gameloop)
            button("Quit",window_width * 0.7, window_height * 0.5,100, 60,bright_red,RED,quitgame)

            pygame.display.update()

def crash(doged,highest_score):
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quitgame()
        message_display('Your Score:'+str(doged),game_container_width//2,window_height*0.2,BLACK)
        message_display('You are Smashed!!',game_container_width//2,window_height*0.5,BLACK)
        button("Try Again!!",game_container_width*0.2,window_height*0.6,150,40,bright_red,RED,gameloop)
        button("Quit", game_container_width * 0.7, window_height * 0.6, 100, 40, bright_red, RED, quitgame)
        pygame.display.update()

def set_car(car,x,y):
    game_display.blit(car,(x,y))

# def things(thing_x,thing_y,thing_width,thing_height,thing_color):
#     pygame.draw.rect(game_display,thing_color,[thing_x,thing_y,thing_width,thing_height])

def display_score(doged):
    font_type=pygame.font.SysFont(None,50)
    score_surface=font_type.render("Score:"+str(doged),True,RED)
    game_display.blit(score_surface,(0,0))
    pygame.display.update()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause=False

def paused():
    global pause
    pygame.mixer.music.pause()
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               quit()

        text_font = pygame.font.Font('NosiferCaps-Regular.ttf', 45)
        text_surface, text_rect = message_develop("PAUSED", text_font,RED)
        text_rect.center = (game_container_width * 0.5, window_height * 0.3)
        game_display.blit(text_surface, text_rect)

        button("Continue", game_container_width * 0.3, window_height * 0.4, 150, 40, bright_red, RED, unpause)
        button("Quit", game_container_width * 0.6, window_height * 0.4, 80, 40, bright_red, RED, quitgame)

        pygame.display.update()

def show_high_score_banner():
    font_style=pygame.font.Font('NosiferCaps-Regular.ttf',25)
    text_surface,text_rect=message_develop("New High score!!!!",font_style,RED)
    text_rect.center=(game_container_width//2,window_height//3)
    game_display.blit(text_surface,text_rect)

def gameloop():
    pygame.mixer.music.play(-1)

    x=game_container_width*0.45
    y=window_height*0.79

    image1_y=0
    image2_y=-600
    speed_image=10

    no_of_frames_display_highscore_banner=frame_per_sec*3
    high_score_file=open("high_score.txt","r")
    highest_score=int(high_score_file.read())
    high_score_file.close()

    thing_width=80
    thing_height=70
    # thing_starty=-600
    # thing_startx=random.randrange(0,game_container_width-thing_width)
    # thing_color=(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
    thing_speed=15
    thing_prop=[]
    for i in range(4):
        thingi={}
        thingi["start_y"]= random.randrange(-5000,-1000)
        thingi["car"]=cars[random.randrange(7,13)]
        # thingi["color"]= (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        thing_prop.append(thingi)
    doged=0
    thing_prop[0]["start_x"] = random.randrange(48,219-thing_width)
    thing_prop[1]["start_x"] = random.randrange(247,424-thing_width)
    thing_prop[2]["start_x"] = random.randrange(453,627-thing_width)
    thing_prop[3]["start_x"] = random.randrange(656,835-thing_width)
    #print(thing_prop)

    global pause

    game_exit=False
    changeinx=0
    changeiny=0

    gamer_car=cars[random.randrange(0,7)]

    while not game_exit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
               pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    changeinx=-10
                elif event.key==pygame.K_RIGHT:
                    changeinx=10
                elif event.key==pygame.K_ESCAPE:
                    pause=True
                    paused()
                if event.key==pygame.K_KP1:
                    gamer_car=cars[0]
                elif event.key==pygame.K_KP2:
                    gamer_car=cars[1]
                elif event.key==pygame.K_KP3:
                    gamer_car=cars[2]
                elif event.key==pygame.K_KP4:
                    gamer_car=cars[3]
                elif event.key==pygame.K_KP5:
                    gamer_car=cars[4]
                elif event.key==pygame.K_KP6:
                    gamer_car=cars[5]
                elif event.key==pygame.K_KP7:
                    gamer_car=cars[6]
            if event.type==pygame.KEYUP:
                if event.key in (pygame.K_LEFT,pygame.K_RIGHT):
                    changeinx=0

            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    changeiny=-15
                elif event.key==pygame.K_DOWN:
                    changeiny+=15
            if event.type==pygame.KEYUP:
                if event.key in (pygame.K_UP,pygame.K_DOWN):
                    changeiny=0

        x+=changeinx
        y+=changeiny
        if x<48:
            x=48
        elif x>48+game_container_width-car_width:
            x=48+game_container_width-car_width
        if y < 0:
            y = 0
        elif y > window_height - car_height:
            y = window_height - car_height

        #game_display.fill(white)
        game_display.blit(road_image, (0,image1_y))
        game_display.blit(road_image, (0, image2_y))

        for i in range(4):
            car_type=random.randrange(7,13)
            set_car(thing_prop[i]["car"],thing_prop[i]["start_x"],thing_prop[i]["start_y"])
            # things(thing_prop[i]["start_x"],thing_prop[i]["start_y"],thing_width,thing_height,thing_prop[i]["color"])
        #things(thing_startx,thing_starty,thing_width,thing_height,thing_color)

        set_car(gamer_car,x, y)

        # thing_starty+=thing_speed
        # if x<0 or x>game_container_width-image_width:
        #     crash()

        for i in range(4):
            if thing_prop[i]["start_y"]>window_height:
                thing_prop[i]["start_y"] = random.randrange(-1000,0)
                # thing_prop[i]["color"]=(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
                thing_prop[i]["car"]=cars[random.randrange(7,13)]
                if i==0:
                    thing_prop[i]["start_x"] = random.randrange(48, 219 - thing_width)
                elif i==1:
                    thing_prop[i]["start_x"] = random.randrange(247, 424 - thing_width)
                elif i==2:
                    thing_prop[i]["start_x"] = random.randrange(453,627 - thing_width)
                elif i==3:
                    thing_prop[i]["start_x"] = random.randrange(656, 835 - thing_width)

                doged+=1
                thing_speed+=0.2

        display_score(doged)
        if doged > highest_score:
            high_score_file = open("high_score.txt", "w")
            high_score_file.write(str(doged))
            high_score_file.close()
            if no_of_frames_display_highscore_banner:
                show_high_score_banner()
                no_of_frames_display_highscore_banner-=1

        if image1_y>=600:
            image1_y=-600
        if image2_y>=600:
            image2_y=-600

        image1_y+=speed_image
        image2_y+=speed_image


        # if thing_starty>window_height:
        #     thing_starty=-thing_height
        #     thing_startx = random.randrange(0, game_container_width - thing_width)
        #     thing_color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        #     doged+=1
        #     #thing_width+=5
        #     thing_speed+=0.2

        for i in range(4):
            if (y>thing_prop[i]["start_y"] and y<thing_prop[i]["start_y"]+thing_height) or (y+car_height>thing_prop[i]["start_y"] and y+car_height<thing_prop[i]["start_y"]+thing_height):
                if (x > thing_prop[i]["start_x"] and x < thing_prop[i]["start_x"] + thing_width) or (x + car_width > thing_prop[i]["start_x"] and x + car_width < thing_prop[i]["start_x"] + thing_width):
                      crash(doged,highest_score)


        # if (y>thing_starty and y<thing_starty+thing_height) or (y+car_height>thing_starty and y+car_height<thing_starty+thing_height ):
        #     if (x>thing_startx and x<thing_startx+thing_width) or (x+car_width>thing_startx and x+car_width<thing_startx+thing_width ):
        #         crash()
        for i in range(4):
            thing_prop[i]["start_y"]+=thing_speed
        pygame.display.update()

        clock.tick(frame_per_sec)
first_page()
pygame.quit()
