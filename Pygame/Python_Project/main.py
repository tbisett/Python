import pygame
import os
from pathlib import Path
pygame.font.init()
pygame.mixer.init()
# below sets the size of the display window the game will appear in
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# below sets the name that shows up on the main window
pygame.display.set_caption("Cyberpsycho")

# Below imports various audio from assets folder
BULLET_IMPACT_AUDIO = pygame.mixer.Sound(os.path.join('Pygame\Python_Project', 'Assets/bullet_collision.mp3'))
BULLET_FIRED_AUDIO =  pygame.mixer.Sound(os.path.join('Pygame\Python_Project', 'Assets/blaster_sound_2.mp3'))
BULLET_FIRED_AUDIO_2 = pygame.mixer.Sound(os.path.join('Pygame\Python_Project', 'Assets/blaster_sound_1.mp3'))
GAME_MUSIC = pygame.mixer.Sound(os.path.join('Pygame\Python_Project', 'Assets/cyberpunk_music_2.ogg'))
GAME_MUSIC_2 = pygame.mixer.Sound(os.path.join('Pygame\Python_Project', 'Assets/cyberpunk_music.MP3'))
# below starts music(parameter of -1 so it loops) and sets volume(between 0.1 and 1)
GAME_MUSIC.play(-1)
GAME_MUSIC.set_volume(0.3)

# below sets the background color of the window, all values are in rgb(variable defined at the top)
WHITE = (255, 255, 255)
BACKGROUND = pygame.image.load(os.path.join('Pygame\Python_Project', 'Assets/cyberpunk_background.png'))
BACKGROUND_SCALED = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

# below sets the refresh rate to 60 frames per second so the game performs consistently despite the users hardware
FPS = 60
# below sets player AND ammo velocity(movement speed)
PLAYER_VEL = 5
BULLET_VEL = 8
MAX_BULLETS = 5
CHARACTER_HEIGHT = 155 
CHARACTER_WIDTH = 140
YELLOW = (255, 255, 0)
BULLET_IMG = pygame.image.load(os.path.join('Pygame\Python_Project', 'Assets/shot-2.png'))
# below creates a user event in pygame so we can call on the bullet collision function later 
# +1 and +2 is used to "give an id" to/ differentiate each event
P1_HIT = pygame.USEREVENT + 1
P2_HIT = pygame.USEREVENT + 2

HEALTH_FONT = pygame.font.Font('Pygame\Python_Project/Assets/PunkDemo.ttf', 40)
# WINNING_FONT = pygame.font.SysFont('Georgia' , 100)
WINNING_FONT = pygame.font.Font('Pygame\Python_Project/Assets/PunkDemo.ttf', 100)

# Below is function to draw the window so we don't cludder the main function
# !!!!!!!!download a picture to use as character and pass the asset file name as an argument below
CHARACTER_IMAGE_1 = pygame.image.load(os.path.join('Pygame\Python_Project','Assets/shoot.png')) 
CHARACTER_1 = pygame.transform.scale(CHARACTER_IMAGE_1, (CHARACTER_WIDTH, CHARACTER_HEIGHT))
CHARACTER_IMAGE_2 = pygame.image.load(os.path.join('Pygame\Python_Project','Assets/shoot.png')) 
CHARACTER_2 = pygame.transform.flip(pygame.transform.scale(CHARACTER_IMAGE_2, (CHARACTER_WIDTH, CHARACTER_HEIGHT)), True, False)

# coordinate system in pygame has 0,0 as the top-left corner of the window or surface instead of the center. x-axis = horizontal,  y-axis vertical
# below is drawing all objects onto the screen
def draw_window(player_1, player_2, p1_bullets, p2_bullets, p1_health, p2_health):
    # WIN.fill((WHITE))
    WIN.blit(BACKGROUND_SCALED, (0,0))
    p1_health_text = HEALTH_FONT.render("Health: " + str(p1_health), 1, WHITE)
    p2_health_text = HEALTH_FONT.render("Health: " + str(p2_health), 1, WHITE)
    WIN.blit(p1_health_text, (10, 10))
    WIN.blit(p2_health_text, (WIDTH - p2_health_text.get_width() - 10, 10))
    WIN.blit(CHARACTER_1, (player_1.x, player_1.y))
    WIN.blit(CHARACTER_2, (player_2.x, player_2.y))
    
    for bullet in p1_bullets:
        # WIN.blit(BULLET_IMG, (player_1.x + player_1.width, player_1.y + player_1.height//2 ))
        pygame.draw.rect(WIN, YELLOW, bullet)
    
    for bullet in p2_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    
    pygame.display.update()
# below defines player movement. Had to add or subtract from some values to make the character reach the edge of the screen instead of having an invisible wall between the character and edge
def player_1_movement(keys_pressed, player_1):
    if keys_pressed[pygame.K_a] and player_1.x > -30 : 
            player_1.x -= PLAYER_VEL
    if keys_pressed[pygame.K_d] and player_1.x + player_1.width < WIDTH + 30:
        player_1.x += PLAYER_VEL
    if keys_pressed[pygame.K_w] and player_1.y > -25:
        player_1.y -= PLAYER_VEL
    if keys_pressed[pygame.K_s] and player_1.y + player_1.height < HEIGHT:
        player_1.y += PLAYER_VEL

def player_2_movement(keys_pressed, player_2):
    if keys_pressed[pygame.K_LEFT] and player_2.x > -30: 
            player_2.x -= PLAYER_VEL
    if keys_pressed[pygame.K_RIGHT] and player_2.x + player_2.width < WIDTH + 30:
        player_2.x += PLAYER_VEL
    if keys_pressed[pygame.K_UP] and player_2.y > -25:
        player_2.y -= PLAYER_VEL
    if keys_pressed[pygame.K_DOWN] and player_2.y + player_2.height < HEIGHT:
        player_2.y += PLAYER_VEL

# below function controls bullet movement, collision, and removal
def control_bullets(p1_bullets, p2_bullets, player_1, player_2):
    for bullet in p1_bullets:
        bullet.x += BULLET_VEL
        if player_2.colliderect(bullet):
            pygame.event.post(pygame.event.Event(P2_HIT))
            p1_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            p1_bullets.remove(bullet)
    
    for bullet in p2_bullets:
        bullet.x -= BULLET_VEL
        if player_1.colliderect(bullet):
            pygame.event.post(pygame.event.Event(P1_HIT))
            p2_bullets.remove(bullet)
        elif bullet.x < 0:
            p2_bullets.remove(bullet)

def draw_winner(text):
    draw_text = WINNING_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()/2, HEIGHT//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)

    
# Below is the main game loop that will infinitely run until the quit or restart function is activated.
def main():
    # below is creating the rectancgles needed for the player images to move as well as for hit detection. Passingin the starting coordinates and the player height and width
    player_1 = pygame.Rect(10, 300, CHARACTER_WIDTH, CHARACTER_HEIGHT )
    player_2 = pygame.Rect(700, 300, CHARACTER_WIDTH, CHARACTER_HEIGHT)
    # below are the arrays that will store bullet count
    p1_bullets = []
    p2_bullets = []
    # below sets player health
    p1_health = 100
    p2_health = 100
    # below background position variable for starting postition point
    BACKGROUND_POS = 0
    # below defines a frame rate/loop refresh clock
    clock = pygame.time.Clock()
    run = True
    while run:
        # below controls the speed of the while loop. Set to the fps variable defined at the top
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
# Below creates the button press needed to fire bullets. It also creates a rectangle for the bullet w/ the parameters of 
# player height / 2 and player width so the bullet appears directly in front of the player
# it also passes the width and height(in px) of the bullet
                if event.key == pygame.K_LCTRL and len(p1_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(player_1.x + player_1.width, player_1.y + player_1.height//2 - 17 , 10, 5)
                    p1_bullets.append (bullet)
                    BULLET_FIRED_AUDIO.set_volume(0.3)
                    BULLET_FIRED_AUDIO.play()
                
                if event.key == pygame.K_RCTRL and len(p2_bullets) < MAX_BULLETS: 
                    bullet = pygame.Rect(player_2.x, player_2.y + player_2.height//2 - 17 , 10, 5)
                    p2_bullets.append (bullet)
                    BULLET_FIRED_AUDIO_2.set_volume(0.3)
                    BULLET_FIRED_AUDIO_2.play()
            
            if event.type == P1_HIT:
                p1_health -= 10
                BULLET_IMPACT_AUDIO.set_volume(0.4)
                BULLET_IMPACT_AUDIO.play()
            
            if event.type == P2_HIT:
                p2_health -= 10
                BULLET_IMPACT_AUDIO.set_volume(0.4)
                BULLET_IMPACT_AUDIO.play()
        
        winner_text = ""
        
        if p2_health <= 0:
            winner_text = "Player 1 Wins!"
        
        if p1_health <= 0:
            winner_text = "Player 2 Wins!"
        
        if winner_text != "":
            draw_winner(winner_text)
            break
        
        keys_pressed = pygame.key.get_pressed()
        player_1_movement(keys_pressed, player_1)
        player_2_movement(keys_pressed, player_2)
        control_bullets(p1_bullets, p2_bullets, player_1, player_2)
        draw_window(player_1, player_2, p1_bullets, p2_bullets, p1_health, p2_health)
        
    
    main()


if __name__ == "__main__":
    main()
