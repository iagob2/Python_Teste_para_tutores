import pgzrun
import random
from pgzero.rect import Rect

# Configurations
WIDTH = 800
HEIGHT = 600
music_enabled = True

# Hero settings
HERO_WIDTH = 64
HERO_HEIGHT = 64
hero_pos = [100, 500]
hero_speed = 5
NUM_HERO_FRAMES = 11
time_between_hero_frames = 0.1
current_hero_frame = 0
hero_elapsed_time = 0
hero_sprite = Actor('hero')

# Enemy settings
NUM_ENEMIES = 5
ENEMY_FRAME_WIDTH = 64
ENEMY_FRAME_HEIGHT = 64
NUM_ENEMY_FRAMES = 8
time_between_enemy_frames = 0.15
current_enemy_frame = 0
enemy_elapsed_time = 0
enemy_sprite = Actor('enemy')
enemies = [{"pos": [random.randint(300, WIDTH - 50), random.randint(100, HEIGHT - 100)]} for _ in range(NUM_ENEMIES)]

# Game states
game_started = False
game_over = False
menu = True
music_enabled = True

# Play music function
def play_music():
    if music_enabled:
        music.play("jango")
        music.set_volume(0.5)

# Main menu function
def draw_menu():
    screen.draw.text("MAIN MENU", center=(WIDTH // 2, 100), fontsize=50, color="white")
    screen.draw.filled_rect(Rect(WIDTH // 2 - 100, 200, 200, 50), "green")
    screen.draw.text("Start Game", center=(WIDTH // 2, 225), fontsize=30, color="white")
    screen.draw.filled_rect(Rect(WIDTH // 2 - 100, 300, 200, 50), "blue")
    screen.draw.text("Music: On" if music_enabled else "Music: Off", center=(WIDTH // 2, 325), fontsize=30, color="white")
    screen.draw.filled_rect(Rect(WIDTH // 2 - 100, 400, 200, 50), "red")
    screen.draw.text("Exit", center=(WIDTH // 2, 425), fontsize=30, color="white")

# Check button clicks in the menu
def check_menu_click(pos):
    global menu, music_enabled, game_started
    if Rect(WIDTH // 2 - 100, 200, 200, 50).collidepoint(pos):  # "Start Game" button
        menu = False
        game_started = True
        play_music()
    elif Rect(WIDTH // 2 - 100, 300, 200, 50).collidepoint(pos):  # "Music" button
        music_enabled = not music_enabled
        if music_enabled:
            play_music()
        else:
            music.stop()
    elif Rect(WIDTH // 2 - 100, 400, 200, 50).collidepoint(pos):  # "Exit" button
        exit()

# Mouse click event
def on_mouse_down(pos):
    if menu:
        check_menu_click(pos)

# Animate hero
def animate_hero(dt):
    global current_hero_frame, hero_elapsed_time
    hero_elapsed_time += dt
    if hero_elapsed_time >= time_between_hero_frames:
        current_hero_frame = (current_hero_frame + 1) % NUM_HERO_FRAMES
        hero_elapsed_time = 0

# Animate enemies
def animate_enemies(dt):
    global current_enemy_frame, enemy_elapsed_time
    enemy_elapsed_time += dt
    if enemy_elapsed_time >= time_between_enemy_frames:
        current_enemy_frame = (current_enemy_frame + 1) % NUM_ENEMY_FRAMES
        enemy_elapsed_time = 0

# Move hero
def move_hero():
    if keyboard.left:
        hero_pos[0] = max(0, hero_pos[0] - hero_speed)
    if keyboard.right:
        hero_pos[0] = min(WIDTH - HERO_WIDTH, hero_pos[0] + hero_speed)
    if keyboard.up:
        hero_pos[1] = max(0, hero_pos[1] - hero_speed)
    if keyboard.down:
        hero_pos[1] = min(HEIGHT - HERO_HEIGHT, hero_pos[1] + hero_speed)

# Move enemies
def move_enemies():
    for enemy in enemies:
        enemy["pos"][0] += random.choice([-1, 1]) * 3
        enemy["pos"][1] += random.choice([-1, 1]) * 3
        enemy["pos"][0] = max(0, min(WIDTH - ENEMY_FRAME_WIDTH, enemy["pos"][0]))
        enemy["pos"][1] = max(0, min(HEIGHT - ENEMY_FRAME_HEIGHT, enemy["pos"][1]))

# Check for collisions
def check_collisions():
    global game_over
    hero_rect = Rect(hero_pos[0], hero_pos[1], HERO_WIDTH, HERO_HEIGHT)
    for enemy in enemies:
        enemy_rect = Rect(enemy["pos"][0], enemy["pos"][1], ENEMY_FRAME_WIDTH, ENEMY_FRAME_HEIGHT)
        if hero_rect.colliderect(enemy_rect):
            game_over = True
            if music_enabled:
                music.play("death")

# Restart game
def restart_game():
    global hero_pos, enemies, game_over, game_started, menu
    hero_pos = [100, 500]
    enemies = [{"pos": [random.randint(300, WIDTH - 50), random.randint(100, HEIGHT - 100)]} for _ in range(NUM_ENEMIES)]
    game_over = False
    game_started = False
    menu = True

# Update game
def update(dt):
    if menu or not game_started:
        return
    if game_over:
        if keyboard.RETURN:
            restart_game()
    else:
        animate_hero(dt)
        animate_enemies(dt)
        move_hero()
        move_enemies()
        check_collisions()

# Draw to the screen
def draw():
    screen.fill((0, 0, 0))  # Clears the screen with black background
    
    if menu:
        draw_menu()  # Draw the menu
    
    elif game_started and not game_over:
        # Hero animation
        hero_frame_x = (current_hero_frame % NUM_HERO_FRAMES) * HERO_WIDTH
        hero_sprite.clip = Rect(hero_frame_x, 0, HERO_WIDTH, HERO_HEIGHT)  # Define sprite clipping
        hero_sprite.pos = hero_pos  # Update hero position
        hero_sprite.draw()  # Draw the animated hero
        
        # Enemies animation
        for enemy in enemies:
            enemy_frame_x = (current_enemy_frame % NUM_ENEMY_FRAMES) * ENEMY_FRAME_WIDTH
            enemy_sprite.clip = Rect(enemy_frame_x, 0, ENEMY_FRAME_WIDTH, ENEMY_FRAME_HEIGHT)
            enemy_sprite.pos = enemy["pos"]
            enemy_sprite.draw()  # Draw the animated enemy
    
    if game_over:
        screen.draw.text("GAME OVER", center=(WIDTH // 2, HEIGHT // 2), fontsize=50, color="red")
        screen.draw.text("Press ENTER to Restart", center=(WIDTH // 2, HEIGHT // 2 + 50), fontsize=30, color="white")

pgzrun.go()
