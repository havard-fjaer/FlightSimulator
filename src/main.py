import pygame
from SimConnect import *
from adapters.vor_adapter import VorAdapter

def main():
    
    # Initialize program state
    DONE = False

    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((200, 50)) # Need this to pick up events
    clock = pygame.time.Clock()
    
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

    # Initialize SimConnect and adapters
    sim_connect = SimConnect()
    vor_adapter = VorAdapter(sim_connect)

    # Check for events
    while not DONE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                DONE = True
            vor_adapter.handle_event(event)
        clock.tick(20)

    # Quit
    sim_connect.exit()
    pygame.quit()

if __name__ == '__main__':
    main()