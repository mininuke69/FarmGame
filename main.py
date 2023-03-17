import pygame

#system variables
screen_width, screen_height = 1280, 720
w_key, a_key, s_key, d_key = False, False, False, False
delta_time =0

#game variables
inv = [] #[("rock", 10), ("stick", 3)]; to get item + amount --> inv[1] gets second item in inv; inv[1][1] gets amount of the second item in inv; inv[1][0] gets name of second item in inv
hp = 100
x, y = 0, 0
area = ""
speed_modifier = 1

#game constants
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


#pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running_mainloop = True



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
            y += SPEED * speed_modifier * delta_time
        if s_key:
            y -= SPEED * speed_modifier * delta_time
        if a_key:
            x -= SPEED * speed_modifier * delta_time
        if d_key:
            x += SPEED * speed_modifier * delta_time
        print(x, SPEED, speed_modifier, delta_time)

    screen.fill("white") #clear screen from previous frame
    
    r = pygame.Rect(x, -y, 100, 100)
    pygame.draw.rect(screen, "red", r, 1)
    

    pygame.display.flip() #render to display

    delta_time = clock.tick(60) / 1000 #limit to 60 fps


print("exiting pygame")
pygame.quit()