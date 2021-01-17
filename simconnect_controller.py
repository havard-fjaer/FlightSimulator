"""
Maps controllers to SimConnect
"""
import pygame
from SimConnect import *
from vpc_control_panel_1 import VpcControlPanel1

# pygame
pygame.init()
screen = pygame.display.set_mode((200, 50))
DONE = False
clock = pygame.time.Clock()
pygame.joystick.init()
joysticks = []
joystick_count = pygame.joystick.get_count()

# SimConnect


sm = SimConnect()




vpc_panel = VpcControlPanel1(sm)

print("Found devices:")
for i in range(joystick_count):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[i].init()
    print("{name} - ID: {id}".format(
            name=joysticks[i].get_name(),
            id=joysticks[i].get_id(),
        ))




while not DONE:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            DONE = True
        vpc_panel.handle_event(event)


pygame.quit()
