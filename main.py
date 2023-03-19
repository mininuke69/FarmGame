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
raw_diamont_img = pygame.image.load(IMG_PATH + ITEMS_INV_PATH + "raw_diamont.png")
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
cam_x, cam_y = 0, 0
fps = 0

#game variables
collisions = []
inv = [] #[("rock", 10), ("stick", 3)]
inv_size = 4 * 5
ground_items = [(stick_img, 50, 50), (stone_img, 100, -400)]
hp = 100
x, y = 0, 0
speed_modifier = 1
inv_open = False


#constants
GAME_NAME = "FarmGame"
STACK_SIZE = 10

ALL_ITEMS = {"apple": apple_img, "carrot": carrot_img, "wheat": wheat_img, "potato": potato_img, "berry": berry_img,
                  "baked_apple": baked_apple_img, "soup": soup_img, "bread": bread_img, "baked_potato": baked_potato_img, "juice": juice_img,
                  "iron_ore": iron_ore_img, "gold_ore": gold_ore_img, "raw_diamont": raw_diamont_img,
                  "iron": iron_img, "gold": gold_img, "diamont": diamont_img,
                  "stone": stone_img, "stick": stick_img, "grass": grass_img,
                  "stone_pick": stone_pick_img, "iron_pick": iron_pick_img, "diamont_pick": diamont_pick_img,
                  "stone_shovel": stone_shovel_img, "iron_shovel": iron_shovel_img, "diamont_shovel": diamont_shovel_img,
                  "stone_axe": stone_axe_img, "iron_axe": iron_axe_img, "diamont_axe": diamont_axe_img}
SPEED = 200
PLAYER_WIDTH, PLAYER_HEIGHT = 64, 64
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
SIMSUN = pygame.font.SysFont("simsun", 30)
DESART = pygame.font.Font("assets/fonts/desard.otf", 30)
MISSIGAUGA = pygame.font.Font("assets/fonts/Mississauga.otf", 30)


def RenderText(content: str, font: pygame.font.Font, coords: tuple, col = "black"):
    txt_img = font.render(content, True, col)
    screen.blit(txt_img, coords)

def UpdateCam():
    global cam_x
    global cam_y

    cam_x += (x - cam_x) / CAM_SPEED_DIVIDER
    cam_y += (y - cam_y) / CAM_SPEED_DIVIDER

def Render():
    global player_x, player_y

    screen.fill("white")

    map_x = MAP_OFFSET_X - cam_x + SCREEN_WIDTH_OFFSET
    map_y = MAP_OFFSET_Y - cam_y + SCREEN_HEIGHT_OFFSET
    screen.blit(map_img, (map_x, map_y))

    for item in ground_items:
        item_x = item[1] - cam_x + SCREEN_WIDTH_OFFSET - (item[0].get_width() / 2)
        item_y = item[2] - cam_y + SCREEN_HEIGHT_OFFSET - (item[0].get_height() / 2)
        item_texture = item[0]
        screen.blit(item_texture, (item_x, item_y))

    player_x = x - cam_x + SCREEN_WIDTH_OFFSET - PLAYER_WIDTH_OFFSET
    player_y = y - cam_y + SCREEN_HEIGHT_OFFSET - PLAYER_HEIGHT_OFFSET
    screen.blit(player_img, (player_x, player_y))

    if len(collisions) > 0:
        RenderText(f"Press F to pick up", MISSIGAUGA, (SCREEN_WIDTH_OFFSET, SCREEN_HEIGHT_OFFSET), "black")

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
    
def CheckCollisions():
    global collisions
    collisions = []

    player_rect = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
    for item in ground_items:
        item_x = item[1]
        item_y = item[2]
        item_height = item[0].get_height()
        item_width = item[0].get_width()
        ground_item_rect = pygame.Rect(item_x, item_y, item_width, item_height)
        if player_rect.colliderect(ground_item_rect):
            collisions.append(item)

def Pickup():
    if len(inv) < inv_size:
        

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
            if key_unicode == "f":
                pass
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


    Move()
    UpdateCam()
    CheckCollisions()
    Render()
    
    delta_time = clock.tick(60) / 1000 #limit to 40 fps
    fps = round(1 / delta_time)


print("exiting pygame")
pygame.quit()