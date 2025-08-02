# Example file showing a circle moving on screen

import asyncio  # added for pygbag
from dataclasses import dataclass, field
from typing import List

import pygame

# pygame setup
pygame.init()
RESOLUTION_WIDTH = 1280
RESOLUTION_HEIGHT = 720
FONT_SIZE = 16
screen = pygame.display.set_mode((RESOLUTION_WIDTH, RESOLUTION_HEIGHT))
clock = pygame.time.Clock()

# Create a font object
font = pygame.font.Font("freesansbold.ttf", FONT_SIZE)  # None for default font

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (127, 0, 255)
ORANGE = (255, 165, 0)
GREY = (127, 127, 127)

BACKGROUND = BLACK
FRAMERATE = 60

score = 0

# resources = {
#     "metal": {
#         "quantity": 0,
#         "colour": GREY,
#         "increaseby": 1,
#         "draw": False,
#         "length": 0,
#         "speed": 1,
#         "location": 50,
#     },
#     "minerals": {
#         "quantity": 0,
#         "colour": BLUE,
#         "increaseby": 1,
#         "draw": False,
#         "length": 0,
#         "speed": 1,
#         "location": 110,
#     },
#     "energy": {
#         "quantity": 0,
#         "colour": ORANGE,
#         "increaseby": 1,
#         "draw": False,
#         "length": 0,
#         "speed": 1,
#         "location": 170,
#     },
# }

# businesses = [
#     {
#         "business": "Lemonade",
#         "colour": GREEN,
#         "location": 50,
#         "value": 1,
#         "value_increase": 0.15,
#         "draw": False,
#         "length": 0,
#         "speed": 5,
#         "task": None,
#         "cost": 1,
#         "cost_increase": 0.1,
#         "manager_owned": False,
#         "manager_cost": 100,
#         "button_location": 10,
#         "colour_button": False,
#         "manager_button": False,
#     },
#     {
#         "business": "Newspaper",
#         "colour": RED,
#         "location": 110,
#         "value": 2,
#         "value_increase": 0.3,
#         "draw": False,
#         "length": 0,
#         "speed": 4,
#         "task": None,
#         "cost": 2,
#         "cost_increase": 0.2,
#         "manager_owned": False,
#         "manager_cost": 500,
#         "button_location": 60,
#         "colour_button": False,
#         "manager_button": False,
#     },
#     {
#         "business": "Carwash",
#         "colour": ORANGE,
#         "location": 170,
#         "value": 3,
#         "value_increase": 0.45,
#         "draw": False,
#         "length": 0,
#         "speed": 3,
#         "task": None,
#         "cost": 3,
#         "cost_increase": 0.3,
#         "manager_owned": False,
#         "manager_cost": 1000,
#         "button_location": 110,
#         "colour_button": False,
#         "manager_button": False,
#     },
#     {
#         "business": "Pizzeria",
#         "colour": WHITE,
#         "location": 230,
#         "value": 4,
#         "value_increase": 0.6,
#         "draw": False,
#         "length": 0,
#         "speed": 2,
#         "task": None,
#         "cost": 4,
#         "cost_increase": 0.4,
#         "manager_owned": False,
#         "manager_cost": 4000,
#         "button_location": 160,
#         "colour_button": False,
#         "manager_button": False,
#     },
#     {
#         "business": "Doughnuts",
#         "colour": PURPLE,
#         "location": 290,
#         "value": 5,
#         "value_increase": 0.75,
#         "draw": False,
#         "length": 0,
#         "speed": 1,
#         "task": None,
#         "cost": 5,
#         "cost_increase": 0.5,
#         "manager_owned": False,
#         "manager_cost": 10000,
#         "button_location": 210,
#         "colour_button": False,
#         "manager_button": False,
#     },
# ]


class Empire:
    spaceships = 0
    spaceships_build_speed = 0


@dataclass
class Resource:
    colour: str
    location: int
    quantity: int = 0
    increaseby: int = 1
    draw: bool = False
    length: int = 0
    speed: int = 1
    name: str = field(default="")


resources = {
    "metal": Resource(colour=GREY, location=50, speed=1.5),
    "minerals": Resource(colour=BLUE, location=110),
    "energy": Resource(colour=ORANGE, location=170),
}


# TechnologyTree requirements:
# Needs to know what resources a technology requires
# Needs to know what technology it depends on


@dataclass
class ResourceCost:
    metal: int = 0
    minerals: int = 0
    energy: int = 0


@dataclass
class Technology:
    name: str
    cost: ResourceCost
    dependencies: List[str] = field(default_factory=list)
    unlocked: bool = False

    def can_unlock(self, resources, tech_tree):
        if (
            resources["metal"].quantity >= self.metal
            and resources["minerals"].quantity >= self.cost.minerals
            and resources["energy"].quantity >= self.cost.energy
            and all(tech_tree[dep].unlocked for dep in self.dependencies)
        ):
            return True
        return False

    def unlock(self, resources, tech_tree):
        if self.can_unlock(resources, tech_tree):
            resources["metal"].quantity -= self.cost.metal
            resources["minerals"].quantity -= self.cost.minerals
            resources["energy"].quantity -= self.cost.energy
            self.unlocked = True
            return True
        return False


tech_tree = {
    "energy": Technology(
        name="Energy", cost=ResourceCost(metal=10, minerals=10, energy=0)
    ),
    "automators": Technology(
        name="Automators",
        cost=ResourceCost(metal=10, minerals=20, energy=10),
        dependencies=["energy"],
    ),
}


def draw_resource(myresource, name):
    foreground_colour = myresource.colour
    draw = myresource.draw
    speed = myresource.speed
    value = myresource.increaseby
    length = myresource.length
    y_coord = myresource.location
    if draw and length < 200:
        length += speed
    elif length >= 200:
        draw = False
        length = 0
        myresource.quantity += value

    resource = pygame.draw.rect(screen, foreground_colour, [75, y_coord - 15, 200, 30])
    pygame.draw.rect(screen, BACKGROUND, [80, y_coord - 10, 190, 20])
    pygame.draw.rect(screen, foreground_colour, [75, y_coord - 15, length, 30])
    quantity_text = font.render(str(round(myresource.quantity, 2)), True, WHITE)
    screen.blit(quantity_text, (285, y_coord - 8))
    resource_text = font.render(name, True, WHITE)
    screen.blit(resource_text, (5, y_coord - 8))
    return resource, length, draw


# Unused at present. Still in from 'notadventurecapitalist' version.
def draw_task(
    foreground_colour, background_colour, y_coord, value, draw, length, speed
):
    global score
    if draw and length < 200:
        length += speed
    elif length >= 200:
        draw = False
        length = 0
        score += value
    collide_object = pygame.draw.circle(screen, foreground_colour, (30, y_coord), 20, 5)
    pygame.draw.rect(screen, foreground_colour, [70, y_coord - 15, 200, 30])
    pygame.draw.rect(screen, background_colour, [75, y_coord - 10, 190, 20])
    pygame.draw.rect(screen, foreground_colour, [70, y_coord - 15, length, 30])
    value_text = font.render(str(round(value, 1)), True, WHITE)
    screen.blit(value_text, (25, y_coord - 8))
    return collide_object, length, draw


# Unused at present. Still in from 'notadventurecapitalist' version.
def draw_buttons(
    foreground_colour, background_colour, x_coord, cost, owned, manager_cost
):
    manager_button = pygame.draw.rect(screen, background_colour, [x_coord, 405, 50, 30])
    colour_button = pygame.draw.rect(screen, foreground_colour, [x_coord, 340, 50, 30])
    colour_cost = font.render(str(round(cost, 2)), True, BLACK)
    screen.blit(colour_cost, (x_coord + 6, 350))
    if not owned:
        manager_button = pygame.draw.rect(
            screen, foreground_colour, [x_coord, 405, 50, 30]
        )
        manager_text = font.render(str(round(manager_cost, 2)), True, background_colour)
        screen.blit(manager_text, (x_coord + 2, 410))
    else:
        manager_button = pygame.draw.rect(
            screen, background_colour, [x_coord, 405, 50, 30]
        )
    return colour_button, manager_button


def draw_tech_tree(foreground_colour, background_colour, x_coord, y_coord, tech_tree):
    title_text = font.render("Technology", True, foreground_colour)
    screen.blit(title_text, (x_coord, y_coord))
    for i, tech in enumerate(tech_tree):
        pygame.draw.rect(
            screen, foreground_colour, [x_coord, y_coord + (i * 35 + 35), 200, 30]
        )
        tech_text = font.render(tech_tree[tech].name, True, BLACK)
        screen.blit(tech_text, (x_coord + 6, y_coord + (i * 35 + 35)))


async def main():  # async for pygbag
    running = True
    global score
    # dt = 0

    # my_empire = Empire()
    if not running:  # added for pygbag, to replace pygame.quit
        return

    while running:
        clock.tick(FRAMERATE)
        # for business in businesses:
        #     if business["manager_owned"] and not business["draw"]:
        #         business["draw"] = True

        # fill the screen with a color to wipe away anything from last frame
        screen.fill(BACKGROUND)

        for resource, values in resources.items():
            values.collide_object, values.length, values.draw = draw_resource(
                values, resource
            )
            # business["colour_button"], business["manager_button"] = draw_buttons(
            #     business["colour"],
            #     BACKGROUND,
            #     business["button_location"],
            #     business["cost"],
            #     business["manager_owned"],
            #     business["manager_cost"],
            # )

        display_score = font.render(
            "Money: $" + str(round(score, 2)), True, WHITE, BACKGROUND
        )
        screen.blit(display_score, (10, 5))

        draw_tech_tree(ORANGE, WHITE, 600, 30, tech_tree)
        # buy_more = font.render("Buy More:", True, WHITE)
        # screen.blit(buy_more, (10, 315))
        # buy_managers = font.render("Buy Managers:", True, WHITE)
        # screen.blit(buy_managers, (10, 380))

        # Render the text
        # text_surface = font.render("Spaceships: ", True, WHITE)

        # Blit the text surface onto the main display surface
        # screen.blit(text_surface, (100, 250))  # Coordinates (100, 250)

        # spaceships_surface = font.render(f"{Empire.spaceships}", True, WHITE)
        # screen.blit(spaceships_surface, (100, 350))

        # delta_surface = font.render(f'{dt}', True, WHITE)
        # screen.blit(delta_surface, (0, 0))

        #        pygame.draw.circle(screen, "red", player_pos, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
        # if keys[pygame.K_w]:
        #     Empire.spaceships += 1
        #        if keys[pygame.K_s]:
        #            player_pos.y += 300 * dt
        #        if keys[pygame.K_a]:
        #            player_pos.x -= 300 * dt
        #        if keys[pygame.K_d]:
        #            player_pos.x += 300 * dt

        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for resource, values in resources.items():
                    if values.collide_object.collidepoint(event.pos):
                        values.draw = True

            #     for business in businesses:
            #         if business["task"].collidepoint(event.pos):
            #             business["draw"] = True
            #         if (
            #             business["manager_button"].collidepoint(event.pos)
            #             and score >= business["manager_cost"]
            #             and not business["manager_owned"]
            #         ):
            #             business["manager_owned"] = True
            #             score -= business["manager_cost"]
            #         if (
            #             business["colour_button"].collidepoint(event.pos)
            #             and score >= business["cost"]
            #         ):
            #             business["value"] += business["value_increase"]
            #             score -= business["cost"]
            #             business["cost"] += business["cost_increase"]

        # flip() the display to put your work on screen
        pygame.display.flip()

        # below added for pygbag
        await asyncio.sleep(0)  # Very important, and keep it 0

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        # dt = clock.tick(60)  #  / 1000

    pygame.quit()


# if __name__ == "__main__":
#     main()

asyncio.run(main())  # added for pygbag, remove earlier 'if' too
