import pygame

#images
IMG_PATH = "assets/images/"
ITEMS_INV_PATH = "items_inv/"

player_img = pygame.image.load(IMG_PATH + "player.png")
map_img = pygame.image.load(IMG_PATH + "grass_texture.png")

apple_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "apple.png")
carrot_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "carrot.png")
wheat_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "wheat.png")
potato_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "potato.png")
berry_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "berry.png")
baked_apple_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "baked_apple.png")
soup_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "soup.png")
bread_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "bread.png")
baked_potato_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "baked_potato.png")
juice_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "juice.png")
iron_ore_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "iron_ore.png")
gold_ore_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "gold_ore.png")
raw_diamontiron_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "raw_diamont.png")
iron_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "iron.png")
gold_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "gold.png")
diamont_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "diamont.png")
stone_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "stone.png")
stick_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "stick.png")
grass_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "grass.png")
stone_pick_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "stone_pick.png")
iron_pick_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "iron_pick.png")
diamont_pick_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "diamont_pick.png")
stone_shovel_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "stone_shovel.png")
iron_shovel_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "iron_shovel.png")
diamont_shovel_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "diamont_shovel.png")
stone_axe_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "stone_axe.png")
iron_axe_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "iron_axe.png")
diamont_axe_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "diamont_axe.png")



#engine variables
w_key, a_key, s_key, d_key = False, False, False, False
delta_time = 0
cam_x, cam_y, map_x, map_y = 0, 0, 0, 0
ground_items = [(stick_img, 50, 50), (stone_img, 100, -400)]
fps = 0

#game variables
inv = [] #[("rock", 10), ("stick", 3)]
hp = 100
x, y = 0, 0
speed_modifier = 1
inv_open = False


#constants
GAME_NAME = "FarmGame"
STACK_SIZE = 10
ALL_ITEMS = ["apple", "carrot", "wheat", "potato", "berry",
                        "baked_apple", "soup", "bread", "baked_potato", "juice",
                        "iron_ore", "gold_ore", "raw_diamont",
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



#fonts
CONSOLAS = pygame.font.SysFont("consolas", 24)
SIMSUN = pygame.font.SysFont("simsun", 16)
DESART = pygame.font.Font("assets/fonts/desard.otf", 16)
MISSIGAUGA = pygame.font.Font("assets/fonts/Mississauga.otf", 16)


def RenderText(content: str, font: pygame.font.Font, coords: tuple, col: str):
    txt_img = font.render(content, True, col)
    screen.blit(txt_img, coords)

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

    RenderText("FPS: " + str(fps), CONSOLAS, (SCREEN_WIDTH - 100, 20), "black")

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
            key_unicode = event.dict["unicode"].lower()
            if key_unicode == "w":
                w_key = True
            if key_unicode == "a":
                a_key = True
            if key_unicode == "s":
                s_key = True
            if key_unicode == "d":
                d_key = True
            if key_unicode == "e":
                inv_open = not inv_open
        if event.type == pygame.KEYUP:
            key_unicode = event.dict["unicode"].lower()
            if key_unicode == "w":
                w_key = False
            if key_unicode == "a":
                a_key = False
            if key_unicode == "s":
                s_key = False
            if key_unicode == "d":
                d_key = False



    print(inv_open)
    Move()
    UpdateCam()
    Render()
    
    delta_time = clock.tick(60) / 1000 #limit to 40 fps
    fps = round(1 / delta_time)


print("exiting pygame")
pygame.quit()