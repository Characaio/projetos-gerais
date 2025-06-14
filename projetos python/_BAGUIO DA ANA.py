import pygame
import random
import sys
import time

pygame.init()
pygame.mixer.init()

info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Sistema em invasão crítica")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
DARK_RED = (150, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 150, 0)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 150)

# Fonts
font = pygame.font.SysFont("Consolas", 18, bold=True)
big_font = pygame.font.SysFont("Consolas", 28, bold=True)
huge_font = pygame.font.SysFont("Consolas", 64, bold=True)

clock = pygame.time.Clock()

button_pos = (WIDTH // 2, HEIGHT // 2)
button_radius = 120
button_text = "mães solteiras"

glitch_mode = False
format_progress = 0.0
popups = []

# Sons de interferência e beeps (coloque seus .wav)
try:
    noise_sounds = [pygame.mixer.Sound(f"interference{i}.wav") for i in range(3)]
    beep_sound = pygame.mixer.Sound("beep.wav")
except Exception:
    noise_sounds = []
    beep_sound = None

def play_noise():
    if noise_sounds:
        snd = random.choice(noise_sounds)
        snd.set_volume(random.uniform(0.4, 0.7))
        snd.play()

def play_beep():
    if beep_sound:
        beep_sound.set_volume(random.uniform(0.6, 1.0))
        beep_sound.play()

# Popups com textos “hackers”
class Popup:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 250)
        self.y = random.randint(0, HEIGHT - 120)
        self.color = [random.randint(50, 255) for _ in range(3)]
        self.text = random.choice([
            "ACCESS GRANTED",
            "ROOTKIT INSTALLED",
            "SYSTEM BREACH DETECTED",
            "DATA LEAK IN PROGRESS",
            "IP TRACKED AND LOGGED",
            "ENCRYPTION DISABLED",
            "ADMIN RIGHTS ACQUIRED",
            "WORM SPREADING",
            "BACKDOOR OPENED",
            "FIREWALL BREACHED",
            "MALWARE ACTIVE",
            "SECURITY OVERRIDDEN",
            "USER DATA EXFILTRATED",
        ])
        self.dx = random.choice([-3, -2, -1, 1, 2, 3])
        self.dy = random.choice([-3, -2, -1, 1, 2, 3])
        self.font = pygame.font.SysFont("Consolas", random.choice([18, 20, 22]), bold=True)
        self.blink = random.randint(0, 30)

    def update(self):
        self.x += self.dx
        self.y += self.dy
        if self.x < 0 or self.x > WIDTH - 250:
            self.dx *= -1
        if self.y < 0 or self.y > HEIGHT - 120:
            self.dy *= -1
        self.blink = (self.blink + 1) % 60

    def draw(self, surface):
        # Piscar aleatório para efeito “bug”
        if (self.blink // 10) % 2 == 0:
            pygame.draw.rect(surface, self.color, (self.x, self.y, 250, 120))
            pygame.draw.rect(surface, BLACK, (self.x, self.y, 250, 120), 4)
            txt = self.font.render(self.text, True, BLACK)
            surface.blit(txt, (self.x + 15, self.y + 50))

# Strings estilo “Matrix”
class MatrixChar:
    def __init__(self, x):
        self.x = x
        self.y = random.randint(-1000, 0)
        self.speed = random.uniform(3, 10)
        self.value = chr(random.randint(33, 126))

    def update(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = random.randint(-1000, 0)
            self.value = chr(random.randint(33, 126))

    def draw(self, surface):
        color = (0, random.randint(150, 255), 0)
        text = font.render(self.value, True, color)
        surface.blit(text, (self.x, int(self.y)))

matrix_chars = [MatrixChar(x) for x in range(0, WIDTH, 15)]

def draw_matrix(surface):
    for char in matrix_chars:
        char.update()
        char.draw(surface)



def draw_progress_bar(surface, progress):
    bar_width = 600
    bar_height = 40
    bar_x = WIDTH // 2 - bar_width // 2
    bar_y = HEIGHT - 100

    pygame.draw.rect(surface, WHITE, (bar_x, bar_y, bar_width, bar_height), 3)
    inner_width = int(bar_width * (progress / 100))
    pygame.draw.rect(surface, RED, (bar_x + 3, bar_y + 3, inner_width - 6 if inner_width > 6 else 0, bar_height - 6))

    progress_text = big_font.render(f"FORMATANDO HD: {int(progress)}%", True, RED)
    surface.blit(progress_text, (bar_x, bar_y - 50))

def draw_warning_text(surface, tick):
    if (tick // 20) % 2 == 0:
        text = huge_font.render("SISTEMA COMPROMETIDO!", True, RED)
        surface.blit(text, (WIDTH // 2 - text.get_width() // 2, 50))

def draw_random_lines(surface):
    for _ in range(10):
        x1 = random.randint(0, WIDTH)
        y1 = random.randint(0, HEIGHT)
        x2 = x1 + random.randint(-100, 100)
        y2 = y1 + random.randint(-100, 100)
        pygame.draw.line(surface, RED, (x1, y1), (x2, y2), 2)

def draw_blue_screen(surface, alpha):
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.fill((0, 0, 128))
    overlay.set_alpha(alpha)
    surface.blit(overlay, (0, 0))
    bs_text = huge_font.render("CRITICAL SYSTEM FAILURE", True, WHITE)
    surface.blit(bs_text, (WIDTH // 2 - bs_text.get_width() // 2, HEIGHT // 3))

# Variáveis para efeito travamento
freeze_frames = 0
freeze_duration = 20
last_frame = None

# Cursor controle fake
cursor_visible = True
cursor_jump_tick = 0

# Cores do botão
BUTTON_COLOR = (200, 0, 0)
BUTTON_HOVER = (255, 50, 50)

running = True
tick = 0

while running:
    mouse_pos = pygame.mouse.get_pos()
    
    # Manipular congelamento (freeze)
    if glitch_mode and freeze_frames > 0:
        # Repete o último frame congelado para simular travamento
        if last_frame:
            screen.blit(last_frame, (0, 0))
        freeze_frames -= 1
        pygame.display.flip()
        clock.tick(15)  # FPS reduzido no travamento
        tick += 1
        continue

    # Normal update
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pass  # Ignorar fechar 'X'
        elif event.type == pygame.KEYDOWN:
            # Só fecha com Alt+F4
            if event.key == pygame.K_F4 and (pygame.key.get_mods() & pygame.KMOD_ALT):
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            dist = ((mouse_pos[0] - button_pos[0]) ** 2 + (mouse_pos[1] - button_pos[1]) ** 2) ** 0.5
            if dist <= button_radius and not glitch_mode:
                glitch_mode = True

    if glitch_mode:
        # Piscar frenético branco/vermelho
        if tick % 15 == 0:
            if random.random() < 0.5:
                flash_color = WHITE
            else:
                flash_color = RED
            flash_surface = pygame.Surface((WIDTH, HEIGHT))
            flash_surface.fill(flash_color)
            flash_surface.set_alpha(100)
            screen.blit(flash_surface, (0, 0))

        draw_matrix(screen)
        draw_random_lines(screen)

        # Popups bugados
        if random.random() < 0.35 and len(popups) < 35:
            popups.append(Popup())

        for popup in popups:
            popup.update()
            popup.draw(screen)

        # Barra de formatação
        if format_progress < 100:
            format_progress += random.uniform(0.3, 0.7)
        draw_progress_bar(screen, format_progress)

        draw_warning_text(screen, tick)

        # Tela azul piscando tipo crash
        if (tick // 60) % 2 == 0:
            alpha = random.randint(50, 180)
            draw_blue_screen(screen, alpha)

        # Sons: interferência aleatória e beeps irritantes
        if random.random() < 0.05:
            play_noise()
        if random.random() < 0.02:
            play_beep()

        # Chance aleatória de travar (congelar frame por um tempo)
        if random.random() < 0.015:
            freeze_frames = freeze_duration
            last_frame = screen.copy()

        # Cursor sumindo/pulando
        cursor_jump_tick += 1
        if cursor_jump_tick % 10 == 0:
            cursor_visible = not cursor_visible
        if not cursor_visible:
            pygame.mouse.set_visible(False)
            # Move cursor randomicamente
            new_x = random.randint(0, WIDTH)
            new_y = random.randint(0, HEIGHT)
            pygame.mouse.set_pos((new_x, new_y))
        else:
            pygame.mouse.set_visible(True)

    
    # Botão aparece SEMPRE
    dist = ((mouse_pos[0] - button_pos[0]) ** 2 + (mouse_pos[1] - button_pos[1]) ** 2) ** 0.5
    color = BUTTON_HOVER if dist <= button_radius else BUTTON_COLOR
    if glitch_mode:
        escolha1 = WIDTH/4
        escolha2 = HEIGHT/3
        inicio_da_escolha1 = int(escolha1)
        fim_da_escolha1 = int(WIDTH - escolha1)
        inicio_da_escolha2 = int(escolha2)
        fim_da_escolha2 = int(HEIGHT - escolha2)
        pontos = [(random.randint(0,WIDTH),random.randint(0,HEIGHT)),
                (random.randint(0,WIDTH),random.randint(0,HEIGHT)),
                (random.randint(0,WIDTH),random.randint(0,HEIGHT)),
                (random.randint(0,WIDTH),random.randint(0,HEIGHT)),
                (random.randint(0,WIDTH),random.randint(0,HEIGHT)),
                (random.randint(0,WIDTH),random.randint(0,HEIGHT)),
                (random.randint(0,WIDTH),random.randint(0,HEIGHT))
                ]
        #pontos = [(random.randint(0,WIDTH),random.randint(0,HEIGHT)),
                #(random.randint(0,WIDTH),random.randint(0,HEIGHT)),
                #(random.randint(0,WIDTH),random.randint(0,HEIGHT)),
                #(random.randint(0,WIDTH),random.randint(0,HEIGHT)),
                #(random.randint(0,WIDTH),random.randint(0,HEIGHT)),
                #(random.randint(0,WIDTH),random.randint(0,HEIGHT)),
                #(random.randint(0,WIDTH),random.randint(0,HEIGHT))
                #]
        print(pontos)
        pygame.draw.polygon(screen,color,pontos)
    else:
        pygame.draw.circle(screen, color, button_pos, button_radius)
    text_surf = font.render(button_text, True, WHITE)
    text_rect = text_surf.get_rect(center=button_pos)
    screen.blit(text_surf, text_rect)

    pygame.display.flip()
    clock.tick(60)
    tick += 1

pygame.quit()
sys.exit()
