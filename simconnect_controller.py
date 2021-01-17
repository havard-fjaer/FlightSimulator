"""
Maps controllers to SimConnect
"""
import pygame

pygame.init()
screen = pygame.display.set_mode((200, 50))
DONE = False
clock = pygame.time.Clock()
pygame.joystick.init()
joysticks = []

joystick_count = pygame.joystick.get_count()
print("Found devices:")
for i in range(joystick_count):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[i].init()
    print("{name} - ID: {id}".format(
            name=joysticks[i].get_name(),
            id=joysticks[i].get_id(),
        ))

while not DONE:
# Possible joystick actions: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN, JOYBUTTONUP, JOYHATMOTION
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            DONE = True


    for i in range(joystick_count):
        joystick = joysticks[i]

        name = joystick.get_name()

        axes = joystick.get_numaxes()
        for j in range(axes):
            axis = joystick.get_axis(j)

        buttons = joystick.get_numbuttons()
        for j in range(buttons):
            button = joystick.get_button(j)

        hats = joystick.get_numhats()
        for j in range(hats):
            hat = joystick.get_hat(j)

    clock.tick(20)

pygame.quit()
