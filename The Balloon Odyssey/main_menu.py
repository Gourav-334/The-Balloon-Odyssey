# initialisation
import pygame
from pygame import mixer
pygame.init()

# resolutions
screenx = 800
screeny = 600
screen = pygame.display.set_mode((screenx,screeny))#, pygame.FULLSCREEN)
title = pygame.display.set_caption("The Balloon Odyssey")

# colour codings
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GREY = (127,127,127)
CYAN = (0,255,255)
PINK = (255,0,255)
YELLOW = (255,255,0)

# screen layer 1 -> {colour codings}
screen.fill(WHITE)

# classes

# graphics -> {classes}
class graphics:
    def __init__(self,x0,y0,x,y,x1,y1,a,b,image):
        self.x0 = x0
        self.y0 = y0
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.a = a
        self.b = b
        self.image = image

# rectangle -> {classes}
class rectangle:
    def __init__(self,x0,y0,x,y,x1,y1,a,b,COLOUR,w):
        self.x0 = x0
        self.y0 = y0
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.a = a
        self.b = b
        self.COLOUR = COLOUR
        self.w = w

# object creation

# loading screen -> {object creation}
title_screen = graphics(0,75,0,75,0,75,800,450,pygame.image.load("title_screen.png"))
load_bar = rectangle(240,480,240,480,240,480,0,20,GREEN,None)
load_bar_frame = rectangle(240,480,240,480,240,480,310,20,BLACK,3)

# main menu -> {object creation}
menu_screen = graphics(0,0,0,0,0,0,800,600,pygame.image.load("menu_screen.png"))
title = graphics(-450,0,-450,0,175,0,600,50,pygame.image.load("title.png"))
balloon1 = graphics(200,70,200,70,200,70,200,300,pygame.image.load("balloon1.png"))
balloon2 = graphics(400,120,400,120,400,120,200,300,pygame.image.load("balloon2.png"))
play = graphics(800,420,800,420,100,420,600,50,pygame.image.load("play0.png"))
settings = graphics(730,-70,730,-70,730,530,60,60,pygame.image.load("settings0.png"))
store = graphics(650,-130,650,-130,650,530,60,60,pygame.image.load("store0.png"))
credit = graphics(570,-190,570,-190,570,530,60,60,pygame.image.load("credit0.png"))

# settings -> {object creation}
video = graphics(-213,200,-213,200,310,200,213,50,pygame.image.load("video0.png"))
audio = graphics(-213,270,-213,270,310,270,213,50,pygame.image.load("audio0.png"))
controls = graphics(-213,340,-213,340,263,340,310,50,pygame.image.load("controls0.png"))
back = graphics(-80,100,-80,100,120,100,80,73,pygame.image.load("back0.png"))

# video -> {object creation}
resolution = graphics(0,0,200,200,0,0,357,50,pygame.image.load("resolution0.png"))
quality = graphics(0,0,200,280,0,0,290,50,pygame.image.load("quality0.png"))
back_v = graphics(-80,100,-80,100,120,100,80,73,pygame.image.load("back0.png"))

# audio -> {object creation}
music = graphics(250,-60,250,-60,250,200,216,50,pygame.image.load("music0.png"))
sfx = graphics(250,610,250,610,250,280,134,50,pygame.image.load("sfx0.png"))
back_a = graphics(-80,100,-80,100,120,100,80,73,pygame.image.load("back0.png"))

# credit -> {object creation}
creditto = graphics(800,170,800,170,120,170,550,213,pygame.image.load("credits.png"))
back_c = graphics(-80,100,-80,100,120,100,80,73,pygame.image.load("back0.png"))

# binary dictionaries
enums = {
    "intro":True,
    "main_menu":False,
    "game":False,
    "outro":False,

    "play":False,
    "play_touch":False,
    "settings":False,
    "settings_touch":False,
    "store":False,
    "store_touch":False,
    "credit":False,
    "credit_touch":False,

    "video":False,
    "video_touch":False,
    "audio":False,
    "audio_touch":False,
    "controls":False,
    "controls_touch":False,
    
    "back":False,
    "back_touch":False,
    "back_v":False,
    "back_v_touch":False,
    "back_a":False,
    "back_a_touch":False,
    "back_c":False,
    "back_c_touch":False,

    "resolution":False,
    "resolution_touch":False,
    "quality":False,
    "quality_touch":False
    }

balloon1_animation = {
    "start":False,
    "x0":False,
    "y0":False,
    "x1":False,
    "y1":False
    }

balloon2_animation = {
    "start":False,
    "x0":False,
    "y0":False,
    "x1":False,
    "y1":False
    }

# functions

# intro -> {functions}
def isIntro():

    # screen blits -> {intro -> {functions}}
    screen.blit(title_screen.image,(title_screen.x,title_screen.y))
    pygame.draw.rect(screen,load_bar.COLOUR,((load_bar.x,load_bar.y),(load_bar.a,load_bar.b)))
    pygame.draw.rect(screen,load_bar_frame.COLOUR,((load_bar_frame.x,load_bar_frame.y),(load_bar_frame.a,load_bar_frame.b)),load_bar_frame.w)

    # animations & t/f -> {intro -> {functions}}
    if load_bar.a < 310:
        pygame.time.wait(10)
        load_bar.a += 1

    elif load_bar.a == 310:
        enums["intro"] = False
        enums["main_menu"] = True

# balloon1 -> {functions}
def isBalloon1():

    # t/f -> {balloon1 -> {functions}}
    if balloon1.x == 200 and balloon1.y == 70:
        balloon1_animation["x0"] = False
        balloon1_animation["y0"] = False
        balloon1_animation["x1"] = False
        balloon1_animation["y1"] = False
        balloon1_animation["start"] = True

    if balloon1.x < 90:
        balloon1_animation["y0"] = False
        balloon1_animation["x1"] = False
        balloon1_animation["y1"] = False
        balloon1_animation["start"] = False
        balloon1_animation["x0"] = True

    if balloon1.x > 210:
        balloon1_animation["y0"] = False
        balloon1_animation["y1"] = False
        balloon1_animation["start"] = False
        balloon1_animation["x0"] = False
        balloon1_animation["x1"] = True

    if balloon1.y < 50:
        balloon1_animation["y1"] = False
        balloon1_animation["start"] = False
        balloon1_animation["x0"] = False
        balloon1_animation["x1"] = False
        balloon1_animation["y0"] = True

    if balloon1.y > 170:
        balloon1_animation["y0"] = False
        balloon1_animation["start"] = False
        balloon1_animation["x0"] = False
        balloon1_animation["x1"] = False
        balloon1_animation["y1"] = True
    
    # animation -> {balloon1 -> {functions}}
    if balloon1_animation["start"] == True:
        balloon1.x -= 0.03
        balloon1.y -= 0.03

    if balloon1_animation["x0"] == True:
        balloon1.x += 0.02
        balloon1.y += 0.03

    if balloon1_animation["y0"] == True:
        balloon1.x -= 0.03
        balloon1.y += 0.02

    if balloon1_animation["x1"] == True:
        balloon1.x -= 0.02
        balloon1.y -= 0.03

    if balloon1_animation["y1"] == True:
        balloon1.x += 0.03
        balloon1.y -= 0.02

# balloon2 -> {functions}
def isBalloon2():

    # t/f -> {balloon2 -> {functions}}
    if balloon2.x == 400 and balloon2.y == 120:
        balloon2_animation["x0"] = False
        balloon2_animation["y0"] = False
        balloon2_animation["x1"] = False
        balloon2_animation["y1"] = False
        balloon2_animation["start"] = True

    if balloon2.x < 340:
        balloon2_animation["y0"] = False
        balloon2_animation["x1"] = False
        balloon2_animation["y1"] = False
        balloon2_animation["start"] = False
        balloon2_animation["x0"] = True

    if balloon2.x > 500:
        balloon2_animation["y0"] = False
        balloon2_animation["y1"] = False
        balloon2_animation["start"] = False
        balloon2_animation["x0"] = False
        balloon2_animation["x1"] = True

    if balloon2.y < 60:
        balloon2_animation["y1"] = False
        balloon2_animation["start"] = False
        balloon2_animation["x0"] = False
        balloon2_animation["x1"] = False
        balloon2_animation["y0"] = True

    if balloon2.y > 190:
        balloon2_animation["y0"] = False
        balloon2_animation["start"] = False
        balloon2_animation["x0"] = False
        balloon2_animation["x1"] = False
        balloon2_animation["y1"] = True
    
    # animation -> {balloon1 -> {functions}}
    if balloon2_animation["start"] == True:
        balloon2.x -= 0.03
        balloon2.y -= 0.03

    if balloon2_animation["x0"] == True:
        balloon2.x += 0.02
        balloon2.y += 0.03

    if balloon2_animation["y0"] == True:
        balloon2.x -= 0.03
        balloon2.y += 0.02

    if balloon2_animation["x1"] == True:
        balloon2.x -= 0.02
        balloon2.y -= 0.03

    if balloon2_animation["y1"] == True:
        balloon2.x += 0.03
        balloon2.y -= 0.02

# main menu -> {functions}
def isMain_menu():

    # screen blits -> {main menu -> {functions}}
    screen.blit(menu_screen.image,(menu_screen.x,menu_screen.y))
    screen.blit(balloon1.image,(balloon1.x,balloon1.y))
    screen.blit(balloon2.image,(balloon2.x,balloon2.y))
    screen.blit(title.image,(title.x,title.y))
    screen.blit(settings.image,(settings.x,settings.y))
    screen.blit(store.image,(store.x,store.y))
    screen.blit(credit.image,(credit.x,credit.y))
    screen.blit(play.image,(play.x,play.y))

    # animations & t/f -> {main menu -> {functions}}
    if title.x < title.x1:
        title.x += 1

    if play.x > play.x1:
        play.x -= 1

    if settings.y < settings.y1:
        settings.y += 1

    if store.y < store.y1:
        store.y += 1

    if credit.y < credit.y1:
        credit.y += 1

    isBalloon1()
    isBalloon2()

# settings -> {functions}
def isSettings():

    # screen blits -> {settings -> {functions}}
    screen.blit(menu_screen.image,(menu_screen.x,menu_screen.y))
    screen.blit(balloon1.image,(balloon1.x,balloon1.y))
    screen.blit(balloon2.image,(balloon2.x,balloon2.y))
    screen.blit(title.image,(title.x,title.y))
    screen.blit(video.image,(video.x,video.y))
    screen.blit(audio.image,(audio.x,audio.y))
    screen.blit(controls.image,(controls.x,controls.y))
    screen.blit(settings.image,(settings.x,settings.y))
    screen.blit(back.image,(back.x,back.y))

    # animations & t/f -> {settings -> {functions}}
    if settings.x>((screenx/2)-settings.a) and settings.y>100:
        settings.x -= 2.9
        settings.y -= 3.7

    if video.x < video.x1:
        video.x += 2

    if audio.x < audio.x1:
        audio.x += 2

    if controls.x < controls.x1:
        controls.x += 2

    if back.x < back.x1:
        back.x += 0.5

    isBalloon1()
    isBalloon2()

# video -> {functions}
def isVideo():

    # screen blits -> {video -> {functions}}
    screen.blit(menu_screen.image,(menu_screen.x,menu_screen.y))
    screen.blit(balloon1.image,(balloon1.x,balloon1.y))
    screen.blit(balloon2.image,(balloon2.x,balloon2.y))
    screen.blit(title.image,(title.x,title.y))
    screen.blit(resolution.image,(resolution.x,resolution.y))
    screen.blit(quality.image,(quality.x,quality.y))
    screen.blit(back_v.image,(back_v.x,back_v.y))
    
    # animations & t/f -> {video -> {functions}}
    if back_v.x < back_v.x1:
        back_v.x += 0.5
    
    isBalloon1()
    isBalloon2()

# audio -> {functions}
def isAudio():

    # screen blits -> {audio -> {functions}}
    screen.blit(menu_screen.image,(menu_screen.x,menu_screen.y))
    screen.blit(balloon1.image,(balloon1.x,balloon1.y))
    screen.blit(balloon2.image,(balloon2.x,balloon2.y))
    screen.blit(title.image,(title.x,title.y))
    screen.blit(music.image,(music.x,music.y))
    screen.blit(sfx.image,(sfx.x,sfx.y))
    screen.blit(back_a.image,(back_a.x,back_a.y))

    # animations & t/f -> {audio -> {functions}}
    if back_a.x < back_a.x1:
        back_a.x += 0.5

    if music.y < music.y1:
        music.y += 1

    if sfx.y > sfx.y1:
        sfx.y -= 1

    isBalloon1()
    isBalloon2()

# credit -> {functions}
def isCredit():

    #screen blits -> {credit -> {functions}}
    screen.blit(menu_screen.image,(menu_screen.x,menu_screen.y))
    screen.blit(balloon1.image,(balloon1.x,balloon1.y))
    screen.blit(balloon2.image,(balloon2.x,balloon2.y))
    screen.blit(title.image,(title.x,title.y))
    screen.blit(creditto.image,(creditto.x,creditto.y))
    screen.blit(back_c.image,(back_c.x,back_c.y))

    # animations & t/f -> {credit -> {functions}}
    if back_c.x < back_c.x1:
        back_c.x += 0.5

    if creditto.x > creditto.x1:
        creditto.x -= 1
    
    isBalloon1()
    isBalloon2()

# music & sounds
mixer.music.load("theme.mp3")
mixer.music.play(-1)

click = pygame.mixer.Sound("click.mp3")

# event loop

# running & screen layer 2 -> {event loop}
running = True

while running:
    screen.fill(BLUE)

    # events -> {event loop}
    for event in pygame.event.get():

        # primary quitting -> {events -> {event loop}}
        if event.type == pygame.QUIT:
            running = False

        # mouse motion -> {events -> {event loop}}
        elif event.type == pygame.MOUSEMOTION:

            # event position (x,y) -> {mouse motion -> {events -> {event loop}}}
            x = event.pos[0]
            y = event.pos[1]

            # play region detection -> {mouse motion -> {events -> {event loop}}}
            if x>play.x and x<play.x+play.a and y>play.y and y<play.y+play.b:
                enums["play_touch"] = True
                play.image = pygame.image.load("play.png")

            # settings region detection -> {mouse motion -> {events -> {event loop}}}
            elif x>settings.x and x<settings.x+settings.a and y>settings.y and y<settings.y+settings.b:
                enums["settings_touch"] = True
                settings.image = pygame.image.load("settings.png")

            # store region detection -> {mouse motion -> {events -> {event loop}}}
            elif x>store.x and x<store.x+store.a and y>store.y and y<store.y+store.b:
                enums["store_touch"] = True
                store.image = pygame.image.load("store.png")

            # credit region detection -> {mouse motion -> {events -> {event loop}}}
            elif x>credit.x and x<credit.x+credit.a and y>credit.y and y<credit.y+credit.b:
                enums["credit_touch"] = True
                credit.image = pygame.image.load("credit.png")

            # back region detection -> {mouse motion -> {events -> {event loop}}}
            elif x>back.x and x<back.x+back.a and y>back.y and y<back.y+back.b:
                enums["back_touch"] = True
                back.image = pygame.image.load("back.png")

            # video region detection -> {mouse motion -> {events -> {event loop}}}
            elif x>video.x and x<video.x+video.a and y>video.y and y<video.y+video.b:
                enums["video_touch"] = True
                video.image = pygame.image.load("video.png")

            # audio region detection -> {mouse motion -> {events -> {event loop}}}
            elif x>audio.x and x<audio.x+audio.a and y>audio.y and y<audio.y+audio.b:
                enums["audio_touch"] = True
                audio.image = pygame.image.load("audio.png")

            # controls region detection -> {mouse motion -> {events -> {event loop}}}
            elif x>controls.x and x<controls.x+controls.a and y>controls.y and y<controls.y+controls.b:
                enums["controls_touch"] = True
                controls.image = pygame.image.load("controls.png")

            # resolution region detection -> {mouse motion -> {events -> {event loop}}}
            elif x>resolution.x and x<resolution.x+resolution.a and y>resolution.y and y<resolution.y+resolution.b:
                enums["resolution_touch"] = True
                resolution.image = pygame.image.load("resolution.png")

            # quality region detection -> {mouse motion -> {events -> {event loop}}}
            elif x>quality.x and x<quality.x+quality.a and y>quality.y and y<quality.y+quality.b:
                enums["quality_touch"] = True
                quality.image = pygame.image.load("quality.png")

            # music region detection -> {mouse motion -> {events -> {event loop}}}
            elif x>music.x and x<music.x+music.a and y>music.y and y<music.y+music.b:
                print(1)
                enums["music_touch"] = True
                music.image = pygame.image.load("music.png")

            # sfx region detection -> {mouse motion -> {events -> {event loop}}}
            elif x>sfx.x and x<sfx.x+sfx.a and y>sfx.y and y<sfx.y+sfx.b:
                print(2)
                enums["sfx_touch"] = True
                sfx.image = pygame.image.load("sfx.png")

            # back_v region detection -> {mouse motion -> {events -> {event loop}}}
            elif x>back_v.x and x<back_v.x+back_v.a and y>back_v.y and y<back_v.y+back_v.b:
                enums["back_v_touch"] = True
                back_v.image = pygame.image.load("back.png")

            # back_a region detection -> {mouse motion -> {events -> {event loop}}}
            elif x>back_a.x and x<back_a.x+back_a.a and y>back_a.y and y<back_a.y+back_a.b:
                enums["back_a_touch"] = True
                back_a.image = pygame.image.load("back.png")

            # back_c region detection -> {mouse motion -> {events -> {event loop}}}
            elif x>back_c.x and x<back_c.x+back_c.a and y>back_c.y and y<back_c.y+back_c.b:
                enums["back_c_touch"] = True
                back_c.image = pygame.image.load("back.png")

            # normal region detection -> {mouse motion -> {events -> {event loop}}}
            else:

                # dictionary changes -> {normal region detection -> {mouse motion -> {events -> {event loop}}}}
                enums["play_touch"] = False
                enums["settings_touch"] = False
                enums["store_touch"] = False
                enums["credit_touch"] = False
                enums["back_touch"] = False
                enums["video_touch"] = False
                enums["audio_touch"] = False
                enums["controls_touch"] = False
                enums["resolution_touch"] = False
                enums["quality_touch"] = False
                enums["music_touch"] = False
                enums["sfx_touch"] = False
                enums["back_v_touch"] = False
                enums["back_a_touch"] = False
                enums["back_c_touch"] = False

                # reverting images -> {normal region detection -> {mouse motion -> {events -> {event loop}}}}
                play.image = pygame.image.load("play0.png")
                settings.image = pygame.image.load("settings0.png")
                store.image = pygame.image.load("store0.png")
                credit.image = pygame.image.load("credit0.png")
                back.image = pygame.image.load("back0.png")
                video.image = pygame.image.load("video0.png")
                audio.image = pygame.image.load("audio0.png")
                controls.image = pygame.image.load("controls0.png")
                resolution.image = pygame.image.load("resolution0.png")
                quality.image = pygame.image.load("quality0.png")
                music.image = pygame.image.load("music0.png")
                sfx.image = pygame.image.load("sfx0.png")
                back_v.image = pygame.image.load("back0.png")
                back_a.image = pygame.image.load("back0.png")
                back_c.image = pygame.image.load("back0.png")

        # mouse button down -> {events -> {event loop}}
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # play region clicking -> {mouse button down -> {events -> {event loop}}}
            if enums["play_touch"] == True:
                enums["main_menu"] = False
                enums["play"] = True
                
                pygame.mixer.Sound.play(click)

            # settings region clicking -> {mouse button down -> {events -> {event loop}}}
            elif enums["settings_touch"] == True:
                enums["main_menu"] = False
                enums["settings"] = True
                
                pygame.mixer.Sound.play(click)

            # store region clicking -> {mouse button down -> {events -> {event loop}}}
            elif enums["store_touch"] == True:
                enums["main_menu"] = False
                enums["store"] = True
                
                pygame.mixer.Sound.play(click)
                
            # credit region clicking -> {mouse button down -> {events -> {event loop}}}        
            elif enums["credit_touch"] == True:
                enums["main_menu"] = False
                enums["credit"] = True
                
                pygame.mixer.Sound.play(click)

            # back region clicking -> {mouse button down -> {events -> {event loop}}}
            elif enums["back_touch"] == True:
                enums["settings"] = False
                enums["main_menu"] = True
                
                pygame.mixer.Sound.play(click)

                settings.x,settings.y = settings.x1,settings.y1
                back.x,back.y = back.x0,back.y0
                video.x,video.y = video.x0,video.y0
                audio.x,audio.y = audio.x0,audio.y0
                controls.x,controls.y = controls.x0,controls.y0
                creditto.x,creditto.y = creditto.x0,creditto.y0

            # video region clicking -> {mouse button down -> {events -> {event loop}}}
            elif enums["video_touch"] == True:
                enums["settings"] = False
                enums["video"] = True
                
                pygame.mixer.Sound.play(click)

                back.x,back.y = back.x0,back.y0

            # audio region clicking -> {mouse button down -> {events -> {event loop}}}
            elif enums["audio_touch"] == True:
                enums["settings"] = False
                enums["audio"] = True
                
                pygame.mixer.Sound.play(click)

                back.x,back.y = back.x0,back.y0

            # controls region clicking -> {mouse button down -> {events -> {event loop}}}
            elif enums["controls_touch"] == True:
                enums["settings"] = False
                enums["controls"] = True
                
                pygame.mixer.Sound.play(click)

                back.x,back.y = back.x0,back.y0

            # resolution region clicking -> {mouse button down -> {events -> {event loop}}}
            elif enums["resolution_touch"] == True:
                enums["video"] = False
                enums["resolution"] = True
                
                pygame.mixer.Sound.play(click)

                back.x,back.y = back.x0,back.y0

            # quality region clicking -> {mouse button down -> {events -> {event loop}}}
            elif enums["quality_touch"] == True:
                enums["video"] = False
                enums["quality"] = True
                
                pygame.mixer.Sound.play(click)

                back.x,back.y = back.x0,back.y0

            # music region clicking -> {mouse button down -> {events -> {event loop}}}
            elif enums["music_touch"] == True:
                enums["audio"] = False
                enums["music"] = True
                
                pygame.mixer.Sound.play(click)
                
            # sfx region clicking -> {mouse button down -> {events -> {event loop}}}
            elif enums["sfx_touch"] == True:
                enums["audio"] = False
                enums["sfx"] = True
                
                pygame.mixer.Sound.play(click)
                

            # back_v region clicking -> {mouse button down -> {events -> {event loop}}}
            elif enums["back_v_touch"] == True:
                enums["video"] = False
                enums["settings"] = True
                
                pygame.mixer.Sound.play(click)

                back_v.x,back_v.y = back_v.x0,back_v.y0
                resolution.x,resolution.y = resolution.x0,resolution.y0
                quality.x,quality.y = quality.x0,quality.y0

            # back_a region clicking -> {mouse button down -> {events -> {event loop}}}
            elif enums["back_a_touch"] == True:
                enums["audio"] = False
                enums["settings"] = True
                
                pygame.mixer.Sound.play(click)

                back_a.x,back_a.y = back_a.x0,back_a.y0
                music.x,music.y = music.x0,music.y0
                sfx.x,sfx.y = sfx.x0,sfx.y0

            # back_c region clicking -> {mouse button down -> {events -> {event loop}}}
            elif enums["back_c_touch"] == True:
                enums["credit"] = False
                enums["main_menu"] = True
                
                pygame.mixer.Sound.play(click)

                back_c.x,back_c.y = back_c.x0,back_c.y0
                creditto.x,creditto.y = creditto.x0,creditto.y0

        # keydown -> {events -> {event loop}}
        elif event.type == pygame.KEYDOWN:

            # secondory quitting -> {keydown -> {events -> {event loop}}}
            if event.key == pygame.K_LCTRL:
                running = False

            # return position -> {keydown -> {events -> {event loop}}}
            elif event.key == pygame.K_RCTRL:
                print(balloon2.x,",",balloon2.y)

    # screen blits -> {event loop}
    if enums["intro"] == True:
        isIntro()

    elif enums["main_menu"] == True:
        isMain_menu()

    elif enums["settings"] == True:
        isSettings()

    elif enums["video"] == True:
        isVideo()

    elif enums["audio"] == True:
        isAudio()

    elif enums["credit"] == True:
        isCredit()

    # display update -> {event loop}
    pygame.display.update()

# quitting program
pygame.quit()
