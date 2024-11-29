import pgzrun
import random
from pygame import Rect

# Configurações
screen_width = 800
screen_height = 600
music_enabled = True

# Dimensões da tela
WIDTH = 800
HEIGHT = 600

# Dimensões do herói e dos inimigos
LARGURA_HEROI = 32
ALTURA_HEROI = 32
LARGURA_INIMIGO = 32
ALTURA_INIMIGO = 32

# Posição inicial do herói
heroi_pos = [100, 500]
heroi_velocidade = 5

# Lista de inimigos
inimigos = [{"pos": [random.randint(300, WIDTH - 50), random.randint(100, HEIGHT - 100)]} for _ in range(5)]

# Estados do jogo
game_started = False
game_over = False
menu = True
musica_ligada = True  # Definindo o estado da música

# Botões do menu
button_start = Rect((screen_width // 2 - 100, screen_height // 2 - 100), (200, 50))
button_music = Rect((screen_width // 2 - 100, screen_height // 2), (200, 50))
button_exit = Rect((screen_width // 2 - 100, screen_height // 2 + 100), (200, 50))

# Função para desenhar na tela
def draw():
    global game_started, game_over, musica_ligada, menu

    screen.fill((0, 0, 0))  # Preenche a tela com fundo preto
    
    if menu:
        desenhar_menu()  # Desenha o menu
    elif game_started and not game_over:
        # Desenha o Jogo
        screen.draw.text("Jogo Iniciado!", center=(screen_width // 2, screen_height // 8), fontsize=40, color="white")
        # Desenha o herói
        screen.draw.filled_rect(Rect(heroi_pos[0], heroi_pos[1], LARGURA_HEROI, ALTURA_HEROI), "blue")
        # Desenha os inimigos
        for inimigo in inimigos:
            screen.draw.filled_rect(Rect(inimigo["pos"][0], inimigo["pos"][1], LARGURA_INIMIGO, ALTURA_INIMIGO), "red")
    if game_over:
        # Tela de Game Over
        screen.draw.text("GAME OVER", center=(WIDTH // 2, HEIGHT // 2), fontsize=60, color="red")
        screen.draw.text("Pressione ENTER para reiniciar", center=(WIDTH // 2, HEIGHT // 2 + 60), fontsize=30, color="white")

def desenhar_menu():
    screen.draw.text("MENU PRINCIPAL", center=(WIDTH // 2, 100), fontsize=50, color="white")

    # Botão "Começar o Jogo"
    screen.draw.filled_rect(Rect(WIDTH // 2 - 100, 200, 200, 50), "green")
    screen.draw.text("Começar o Jogo", center=(WIDTH // 2, 225), fontsize=30, color="white")

    # Botão "Música e Sons"
    screen.draw.filled_rect(Rect(WIDTH // 2 - 100, 300, 200, 50), "blue")
    musica_estado = "Ligados" if musica_ligada else "Desligados"
    screen.draw.text(f"Música: {musica_estado}", center=(WIDTH // 2, 325), fontsize=30, color="white")

    # Botão "Saída"
    screen.draw.filled_rect(Rect(WIDTH // 2 - 100, 400, 200, 50), "red")
    screen.draw.text("Saída", center=(WIDTH // 2, 425), fontsize=30, color="white")

def verificar_clique_menu(pos):
    global menu, musica_ligada, game_started

    if mouse.LEFT:
        if Rect(WIDTH // 2 - 100, 200, 200, 50).collidepoint(pos):  # Botão "Começar o Jogo"
            menu = False
            game_started = True  # Começar o jogo
            if musica_ligada:
                music.play("fauxdoor")  # Reproduz música de fundo
                music.set_volume(0.5)  # Ajusta o volume da música
        elif Rect(WIDTH // 2 - 100, 300, 200, 50).collidepoint(pos):  # Botão "Música e Sons"
            musica_ligada = not musica_ligada
            if musica_ligada:
                music.play("fauxdoor")  # Reproduz música de fundo
                music.set_volume(0.5)  # Ajusta o volume da música
            else:
                music.stop()  # Para a música
        elif Rect(WIDTH // 2 - 100, 400, 200, 50).collidepoint(pos):  # Botão "Saída"
            exit()

# Função para atualizar o jogo
def update():
    global game_started, game_over

    if not game_started:
        return  # Não faz nada se o jogo não começou

    if not game_over:
        mover_heroi()
        mover_inimigos()
        verificar_colisoes()
    else:
        if keyboard.RETURN:
            reiniciar_jogo()

# Movimento do herói
def mover_heroi():
    if keyboard.left:
        heroi_pos[0] = max(0, heroi_pos[0] - heroi_velocidade)
    if keyboard.right:
        heroi_pos[0] = min(WIDTH - LARGURA_HEROI, heroi_pos[0] + heroi_velocidade)
    if keyboard.up:
        heroi_pos[1] = max(0, heroi_pos[1] - heroi_velocidade)
    if keyboard.down:
        heroi_pos[1] = min(HEIGHT - ALTURA_HEROI, heroi_pos[1] + heroi_velocidade)

# Movimento dos inimigos
def mover_inimigos():
    for inimigo in inimigos:
        inimigo["pos"][0] += random.choice([-1, 1]) * 3
        inimigo["pos"][1] += random.choice([-1, 1]) * 3

        # Impedir que os inimigos saiam da tela
        inimigo["pos"][0] = max(0, min(WIDTH - LARGURA_INIMIGO, inimigo["pos"][0]))
        inimigo["pos"][1] = max(0, min(HEIGHT - ALTURA_INIMIGO, inimigo["pos"][1]))

# Verificar colisões
def verificar_colisoes():
    global game_over

    heroi_rect = Rect(heroi_pos[0], heroi_pos[1], LARGURA_HEROI, ALTURA_HEROI)
    for inimigo in inimigos:
        inimigo_rect = Rect(inimigo["pos"][0], inimigo["pos"][1], LARGURA_INIMIGO, ALTURA_INIMIGO)
        if heroi_rect.colliderect(inimigo_rect):
            game_over = True

# Reiniciar o jogo
def reiniciar_jogo():
    global heroi_pos, inimigos, game_over, game_started, menu

    heroi_pos = [100, 500]
    inimigos = [{"pos": [random.randint(300, WIDTH - 50), random.randint(100, HEIGHT - 100)]} for _ in range(5)]
    game_over = False
    game_started = False
    menu = True  # Retorna ao menu principal

# Função para verificar os cliques nos botões
def on_mouse_down(pos):
    verificar_clique_menu(pos)

# Inicia o jogo
pgzrun.go()
