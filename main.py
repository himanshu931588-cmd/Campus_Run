import pygame

from item import Item, create_timetable
from player import Player
from room import Room


SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 620
MAP_WIDTH = 15
MAP_HEIGHT = 10
TILE_SIZE = 52
MAP_LEFT = 24
MAP_TOP = 86
GOAL = (13, 1)

BACKGROUND = (16, 25, 38)
PANEL = (25, 38, 55)
FLOOR = (49, 69, 82)
WALL = (15, 19, 27)
PLAYER_COLOR = (255, 214, 102)
GOAL_COLOR = (108, 220, 160)
TEXT = (235, 241, 245)
MUTED_TEXT = (160, 177, 190)


def create_player():
    walls = set()
    for x in range(3, 12):
        if x != 7:
            walls.add((x, 5))

    campus = Room("Campus", width=MAP_WIDTH, height=MAP_HEIGHT, walls=walls)
    id_card = Item("ID Card")
    timetable = create_timetable()
    player = Player(current_room=campus, inventory=[id_card, timetable], x=1, y=8)
    classroom = Room("Classroom 404", room_type="classroom")
    classroom.add_interaction(0, 0, "You open the door to Classroom 404.")
    return player, classroom


def draw_text(screen, font, text, position, color=TEXT):
    image = font.render(text, True, color)
    screen.blit(image, position)


def draw_map(screen, player, font):
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            tile = pygame.Rect(
                MAP_LEFT + x * TILE_SIZE,
                MAP_TOP + y * TILE_SIZE,
                TILE_SIZE - 2,
                TILE_SIZE - 2,
            )
            if (x, y) in player.current_room.walls:
                pygame.draw.rect(screen, WALL, tile)
            else:
                pygame.draw.rect(screen, FLOOR, tile)

    goal_x, goal_y = GOAL
    goal_tile = pygame.Rect(
        MAP_LEFT + goal_x * TILE_SIZE,
        MAP_TOP + goal_y * TILE_SIZE,
        TILE_SIZE - 2,
        TILE_SIZE - 2,
    )
    pygame.draw.rect(screen, GOAL_COLOR, goal_tile)
    draw_text(screen, font, "404", (goal_tile.x + 7, goal_tile.y + 14), BACKGROUND)

    player_x = GOAL[0] if player.is_in_classroom() else player.x
    player_y = GOAL[1] if player.is_in_classroom() else player.y
    player_tile = pygame.Rect(
        MAP_LEFT + player_x * TILE_SIZE + 10,
        MAP_TOP + player_y * TILE_SIZE + 10,
        TILE_SIZE - 22,
        TILE_SIZE - 22,
    )
    pygame.draw.rect(screen, PLAYER_COLOR, player_tile)


def draw_panel(screen, player, font, small_font, message):
    panel_rect = pygame.Rect(820, 0, 280, SCREEN_HEIGHT)
    pygame.draw.rect(screen, PANEL, panel_rect)
    draw_text(screen, font, "CAMPUS RUN", (850, 28))
    draw_text(screen, small_font, "Reach Classroom 404", (850, 70), MUTED_TEXT)
    draw_text(screen, small_font, "LOCATION", (850, 130), MUTED_TEXT)
    draw_text(screen, font, player.current_room.name, (850, 154))
    draw_text(screen, small_font, "TIME", (850, 210), MUTED_TEXT)
    draw_text(screen, font, player.get_current_time(), (850, 234))
    draw_text(screen, small_font, "SECONDS LEFT", (850, 290), MUTED_TEXT)
    draw_text(screen, font, str(player.get_time_left()), (850, 314))
    draw_text(screen, small_font, "INVENTORY", (850, 375), MUTED_TEXT)

    item_y = 400
    for item in player.inventory:
        draw_text(screen, small_font, "- " + item.name, (850, item_y))
        item_y += 24

    draw_text(screen, small_font, "WASD / ARROWS  Move", (850, 510), MUTED_TEXT)
    draw_text(screen, small_font, "E  Interact     ESC  Quit", (850, 540), MUTED_TEXT)
    draw_text(screen, small_font, message, (850, 575), PLAYER_COLOR)


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Campus Run")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 30)
    small_font = pygame.font.Font(None, 22)

    player, classroom = create_player()
    message = "Find Room 404."
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_e:
                    message = player.interact()
                elif not player.is_in_classroom():
                    direction = None
                    if event.key in (pygame.K_w, pygame.K_UP):
                        direction = "W"
                    elif event.key in (pygame.K_a, pygame.K_LEFT):
                        direction = "A"
                    elif event.key in (pygame.K_s, pygame.K_DOWN):
                        direction = "S"
                    elif event.key in (pygame.K_d, pygame.K_RIGHT):
                        direction = "D"

                    if direction is not None:
                        message = player.move(direction)
                        if (player.x, player.y) == GOAL:
                            player.current_room = classroom
                            player.x = 0
                            player.y = 0
                            message = "You reached Classroom 404!"

        screen.fill(BACKGROUND)
        draw_text(screen, font, "COLLEGE CAMPUS", (MAP_LEFT, 30))
        draw_map(screen, player, small_font)
        draw_panel(screen, player, font, small_font, message)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    run_game()