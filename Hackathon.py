import pygame
import sys
import math
from elements import ELEMENTS

pygame.init()
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Visual Chemistry Lab")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

CENTER = (WIDTH // 2, HEIGHT // 2)
BG_COLOR = (20, 20, 20)
FONT_COLOR = (255, 255, 255)

PARTICLE_COLORS = {
    "proton": (220, 50, 50),
    "neutron": (50, 220, 50),
    "electron": (50, 100, 255)
}

SHELLS = [2, 8, 18]

counts = {"proton": 0, "neutron": 0, "electron": 0}
proton_positions = []
neutron_positions = []
electron_positions = []
last_atom_info = None

start_positions = {
    "proton": (100, 100),
    "neutron": (100, 200),
    "electron": (100, 300)
}


def identify_atom(p, n, e):
    if e != p:
        return None
    element = ELEMENTS.get(p)
    if not element:
        return None
    isotope = element["isotopes"].get(n)
    if not isotope:
        return None
    return {
        "name": element["name"],
        "symbol": element["symbol"],
        "atomic_number": p,
        "mass_number": p + n,
        "isotope": isotope,
        "fact": element["fact"]
    }


class Particle(pygame.sprite.Sprite):
    RADIUS = 20
    def __init__(self, kind, pos):
        super().__init__()
        self.kind = kind
        self.image = pygame.Surface((self.RADIUS * 2, self.RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, PARTICLE_COLORS[kind], (self.RADIUS, self.RADIUS), self.RADIUS)
        self.rect = self.image.get_rect(center=pos)
        self.dragging = False

    def update(self):
        if self.dragging:
            self.rect.center = pygame.mouse.get_pos()


particles = pygame.sprite.Group()
for kind, pos in start_positions.items():
    particles.add(Particle(kind, pos))



def layout_ring(center, radius, count):
    if count == 0:
        return []
    angle_step = 360 / count
    return [
        (
            int(center[0] + radius * math.cos(math.radians(i * angle_step))),
            int(center[1] + radius * math.sin(math.radians(i * angle_step)))
        )
        for i in range(count)
    ]


def calculate_nucleus_positions(count, layers=[6, 12, 18]):
    positions = []
    total = 0
    for layer_index, max_in_layer in enumerate(layers):
        if count <= total:
            break
        remaining = min(count - total, max_in_layer)
        radius = 15 + layer_index * 15
        positions.extend(layout_ring(CENTER, radius, remaining))
        total += remaining
    return positions


def calculate_electron_positions(electron_count):
    positions = []
    left = electron_count
    radius_start = 80
    for shell_index, max_e in enumerate(SHELLS):
        e_in_shell = min(left, max_e)
        positions.extend(layout_ring(CENTER, radius_start + shell_index * 40, e_in_shell))
        left -= e_in_shell
        if left <= 0:
            break
    return positions


def update_positions():
    global proton_positions, neutron_positions, electron_positions
    proton_positions = calculate_nucleus_positions(counts["proton"])
    neutron_positions = calculate_nucleus_positions(counts["neutron"])
    electron_positions = calculate_electron_positions(counts["electron"])


def handle_drop(particle):
    kind = particle.kind
    if particle.rect.centerx > 300:
        counts[kind] += 1
        update_positions()
        global last_atom_info
        last_atom_info = identify_atom(counts["proton"], counts["neutron"], counts["electron"])
    particle.rect.center = start_positions[kind]


def reset():
    global counts, proton_positions, neutron_positions, electron_positions, last_atom_info
    counts = {k: 0 for k in counts}
    proton_positions.clear()
    neutron_positions.clear()
    electron_positions.clear()
    last_atom_info = None
    update_positions()


def draw_particles():
    for pos in proton_positions:
        pygame.draw.circle(screen, PARTICLE_COLORS["proton"], pos, 7)
    for pos in neutron_positions:
        pygame.draw.circle(screen, PARTICLE_COLORS["neutron"], pos, 7)
    for pos in electron_positions:
        pygame.draw.circle(screen, PARTICLE_COLORS["electron"], pos, 5)


def draw_structure():
    pygame.draw.circle(screen, (100, 100, 150), CENTER, 50, 1)
    for i in range(len(SHELLS)):
        pygame.draw.circle(screen, (60, 60, 60), CENTER, 80 + i * 40, 1)


def draw_counts():
    y = 10
    for k, v in counts.items():
        txt = font.render(f"{k.capitalize()}: {v}", True, FONT_COLOR)
        screen.blit(txt, (10, y))
        y += 25


def draw_atom_info():
    if last_atom_info:
        lines = [
            f"Atom: {last_atom_info['name']} ({last_atom_info['symbol']})",
            f"Isotope: {last_atom_info['isotope']}",
            f"Atomic Number: {last_atom_info['atomic_number']}",
            f"Mass Number: {last_atom_info['mass_number']}",
            f"Fact: {last_atom_info['fact']}"
        ]
        y = 500
        for line in lines:
            txt = font.render(line, True, FONT_COLOR)
            screen.blit(txt, (10, y))
            y += 25


# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            reset()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for p in particles:
                if p.rect.collidepoint(event.pos):
                    p.dragging = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p and event.key == pygame.KEYUP:
                counts["proton"] += 1
                update_positions()
            elif event.key == pygame.K_n and event.key == pygame.KEYUP:
                counts["neutron"] += 1
                update_positions()
            elif  event.key == pygame.K_e and event.key == pygame.KEYUP:
                counts["electron"] += 1
                update_positions()
            elif event.key == pygame.K_e:
                counts["electron"] -= 1
                update_positions()
            elif event.key == pygame.K_n:
                counts["neutron"] -= 1
                update_positions()
            elif event.key == pygame.K_p:
                counts["proton"] -=1
                update_positions()
        elif event.type == pygame.MOUSEBUTTONUP:
            for p in particles:
                if p.dragging:
                    p.dragging = False
                    handle_drop(p)

    particles.update()
    screen.fill(BG_COLOR)
    draw_structure()
    draw_particles()
    particles.draw(screen)
    draw_counts()
    draw_atom_info()

    instructions = font.render("Drag particles → to build atoms. Press R to reset.", True, FONT_COLOR)
    screen.blit(instructions, (250, 660))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
