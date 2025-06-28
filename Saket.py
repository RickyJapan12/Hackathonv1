import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 400, 250
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Edit Particle Counts")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
input_font = pygame.font.SysFont(None, 28)

# Input boxes data: label, rect, current text, active flag
inputs = {
    "proton": {"rect": pygame.Rect(150, 30, 100, 40), "text": "0", "active": False},
    "neutron": {"rect": pygame.Rect(150, 90, 100, 40), "text": "0", "active": False},
    "electron": {"rect": pygame.Rect(150, 150, 100, 40), "text": "0", "active": False}
}

def draw():
    screen.fill((30, 30, 30))
    y_positions = {"proton": 30, "neutron": 90, "electron": 150}

    for key, data in inputs.items():
        # Draw label
        label_surf = font.render(key.capitalize() + ":", True, (255, 255, 255))
        screen.blit(label_surf, (20, y_positions[key]))

        # Draw input box
        color = (255, 255, 255) if data["active"] else (150, 150, 150)
        pygame.draw.rect(screen, color, data["rect"], 2)

        # Draw text
        txt_surf = input_font.render(data["text"], True, (255, 255, 255))
        screen.blit(txt_surf, (data["rect"].x + 5, data["rect"].y + 8))

    instructions = "Click box and type number. Press Enter to confirm."
    instr_surf = input_font.render(instructions, True, (180, 180, 180))
    screen.blit(instr_surf, (10, HEIGHT - 30))

def clamp_text_to_int(text):
    try:
        val = int(text)
        return max(val, 0)  # no negatives
    except:
        return 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if clicked inside any input box
            for key, data in inputs.items():
                if data["rect"].collidepoint(event.pos):
                    data["active"] = True
                else:
                    data["active"] = False

        elif event.type == pygame.KEYDOWN:
            for key, data in inputs.items():
                if data["active"]:
                    if event.key == pygame.K_RETURN:
                        # Confirm input on Enter: clamp to int
                        data["text"] = str(clamp_text_to_int(data["text"]))
                        data["active"] = False
                    elif event.key == pygame.K_BACKSPACE:
                        data["text"] = data["text"][:-1]
                    elif event.unicode.isdigit():
                        data["text"] += event.unicode

    draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
