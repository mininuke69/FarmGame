import pygame

#images
IMG_PATH = "assets/images/"
player_img = pygame.image.load(IMG_PATH + "player.png")
map_img = pygame.image.load(IMG_PATH + "grass_texture.png")


stick_img = pygame.image.load(IMG_PATH + "stick.png")
stone_img = pygame.image.load(IMG_PATH + "stone.png")

#engine variables
w_key, a_key, s_key, d_key = False, False, False, False
delta_time = 0
cam_x, cam_y, map_x, map_y = 0, 0, 0, 0
ground_items = [(stick_img, 50, 50), (stone_img, 100, -400)]

#game variables
inv = [] #[("rock", 10), ("stick", 3)]; to get item + amount --> inv[1] gets second item in inv; inv[1][1] gets amount of the second item in inv; inv[1][0] gets name of second item in inv
hp = 100
x, y = 0, 0
speed_modifier = 1


#constants
GAME_NAME = "FarmGame"
STACK_SIZE = 10
ALL_ITEMS = ["apple", "carrot", "wheat", "potato", "berry",
                        "baked_apple", "soup", "bread", "baked_potato", "juice",
                        "iron", "gold", "diamont", 
                        "stone", "stick", "grass",
                        "stone_pick", "iron_pick", "diamont_pick",
                        "stone_shovel", "iron_shovel", "diamont_shovel",
                        "stone_axe", "iron_axe", "diamont_axe"]
SPEED = 200
PLAYER_WIDTH, PLAYER_HEIGHT = 256, 256
PLAYER_WIDTH_OFFSET, PLAYER_HEIGHT_OFFSET = PLAYER_WIDTH / 2, PLAYER_HEIGHT / 2
CAM_SPEED_DIVIDER = 10
MAP_OFFSET_X, MAP_OFFSET_Y = 0, 0
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
SCREEN_WIDTH_OFFSET, SCREEN_HEIGHT_OFFSET = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2


#pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running_mainloop = True
pygame.display.set_caption(GAME_NAME)






def UpdateCam():
    global cam_x
    global cam_y

    cam_x += (x - cam_x) / CAM_SPEED_DIVIDER
    cam_y += (y - cam_y) / CAM_SPEED_DIVIDER

def Render():
    screen.fill("white")

    map_x = MAP_OFFSET_X - cam_x + SCREEN_WIDTH_OFFSET
    map_y = MAP_OFFSET_Y - cam_y + SCREEN_HEIGHT_OFFSET
    screen.blit(map_img, (map_x, map_y))

    for item in ground_items:
        item_x = item[1] - cam_x
        item_y = item[2] - cam_y
        item_texture = item[0]
        screen.blit(item_texture, (item_x, item_y))

    player_x = x - cam_x + SCREEN_WIDTH_OFFSET - PLAYER_WIDTH_OFFSET
    player_y = y - cam_y + SCREEN_HEIGHT_OFFSET - PLAYER_HEIGHT_OFFSET
    screen.blit(player_img, (player_x, player_y))

    pygame.display.update()

def Move():
    global x, y
    global w_key, a_key, s_key, d_key
    global speed_modifier, delta_time, SPEED

    if w_key or a_key or s_key or d_key:
        if w_key:
            y -= SPEED * speed_modifier * delta_time
        if s_key:
            y += SPEED * speed_modifier * delta_time
        if a_key:
            x -= SPEED * speed_modifier * delta_time
        if d_key:
            x += SPEED * speed_modifier * delta_time
    


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



    
    Move()
    UpdateCam()
    Render()
    
    delta_time = clock.tick(60) / 1000 #limit to 60 fps
    fps = 1 / delta_time


print("exiting pygame")
pygame.quit()