import pygame

#system variables
w_key, a_key, s_key, d_key = False, False, False, False
delta_time = 0

#game variables
inv = [] #[("rock", 10), ("stick", 3)]; to get item + amount --> inv[1] gets second item in inv; inv[1][1] gets amount of the second item in inv; inv[1][0] gets name of second item in inv
hp = 100
x, y = 0, 0
area = ""
speed_modifier = 1
cam_x, cam_y, map_x, map_y = 0, 0, 0, 0

#constants
GAME_NAME = "FarmGame"
ALL_AREAS = ["beach", "ruins", "forest"]
STACK_SIZE = 10
ALL_ITEMS = ["apple", "carrot", "wheat", "potato", "berry",
                        "baked_apple", "soup", "bread", "baked_potato", "juice",
                        "iron", "gold", "diamont", 
                        "stone", "stick", "grass",
                        "stone_pick", "iron_pick", "diamont_pick",
                        "stone_shovel", "iron_shovel", "diamont_shovel",
                        "stone_axe", "iron_axe", "diamont_axe"]
SPEED = 200
PLAYER_RECT_WIDTH, PLAYER_RECT_HEIGHT = 256, 256
CAM_SPEED_DIVIDER = 10
MAP_OFFSET_X, MAP_OFFSET_Y = 0, 0
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720


#pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running_mainloop = True
pygame.display.set_caption(GAME_NAME)

player_img = pygame.image.load("assets/images/player.png")
map_img = pygame.image.load("assets/images/grass_texture.png")




def UpdateCam():
    global cam_x
    global cam_y

    cam_x += (x - cam_x) / CAM_SPEED_DIVIDER
    cam_y += (y - cam_y) / CAM_SPEED_DIVIDER

while running_mainloop:
    for event in pygame.event.get(): #loop trough events
        if event.type == pygame.QUIT:
            running_mainloop = False
        if event.type == pygame.KEYDOWN:
            key_unicode = event.dict["unicode"]
            if key_unicode == "w":
                w_key = True
            if key_unicode == "a":
                a_key = True
            if key_unicode == "s":
                s_key = True
            if key_unicode == "d":
                d_key = True
        if event.type == pygame.KEYUP:
            key_unicode = event.dict["unicode"]
            if key_unicode == "w":
                w_key = False
            if key_unicode == "a":
                a_key = False
            if key_unicode == "s":
                s_key = False
            if key_unicode == "d":
                d_key = False

    
    if w_key or a_key or s_key or d_key:
        if w_key:
            y -= SPEED * speed_modifier * delta_time
        if s_key:
            y += SPEED * speed_modifier * delta_time
        if a_key:
            x -= SPEED * speed_modifier * delta_time
        if d_key:
            x += SPEED * speed_modifier * delta_time

    screen.fill("white") #clear screen from previous frame

    UpdateCam()

    screen.blit(map_img, (MAP_OFFSET_X - cam_x, MAP_OFFSET_Y - cam_y))
    screen.blit(player_img, (x - cam_x, y - cam_y))

    
    

    pygame.display.update() #render to display
    delta_time = clock.tick(60) / 1000 #limit to 60 fps
    fps = 1 / delta_time


print("exiting pygame")
pygame.quit()