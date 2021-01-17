import pygame
from SimConnect import *
from vor_adapter import VorAdapter

# State
DONE = False

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((200, 50))

# Initialize joysticks
joysticks = []
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()
print("Found devices:")
for i in range(joystick_count):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[i].init()
    print("{name} - ID: {id}".format(
            name=joysticks[i].get_name(),
            id=joysticks[i].get_id(),
        ))

# SimConnect and adapters
sim_connect = SimConnect()
vor_adapter = VorAdapter(sim_connect)

# Check for events
while not DONE:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            DONE = True
        vor_adapter.handle_event(event)

# Quit
sim_connect.exit()
pygame.quit()
