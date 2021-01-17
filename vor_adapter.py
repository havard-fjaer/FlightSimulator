
"""
Connects joystick events to sim connect Omni Bearing Selector (OBS) variables and VHF omnidirectional radio range (VOR) events.
"""
import pygame
from SimConnect import *
from compass import *
import sim_connect_event
import sim_connect_variable

ACTION_VOR1 = "VOR1"
ACTION_VOR2 = "VOR2"

class VorAdapter:
    def __init__(self, sim_connect):
        aircraft_events = AircraftEvents(sim_connect)
        self.aircraft_requests = AircraftRequests(sim_connect, _time=10)
        self.current_action = None
        
        self.vor1_set = aircraft_events.find(sim_connect_event.VOR1_SET)
        self.vor2_set = aircraft_events.find(sim_connect_event.VOR2_SET)

    def handle_event(self, event):
        self.event_to_current_action(event)
        if not self.is_compass_event(event):
            return
        
        # VOR1
        if self.current_action == ACTION_VOR1:
            obs1 = self.event_to_compass(event, int(self.aircraft_requests.get(sim_connect_variable.NAV_OBS_1))) 
            print("Setting VOR1 to {degrees}".format(degrees=obs1.degrees))
            self.vor1_set(obs1.degrees)     

        # VOR2
        elif self.current_action == ACTION_VOR2:
            obs2 = self.event_to_compass(event, int(self.aircraft_requests.get(sim_connect_variable.NAV_OBS_1)))
            print("Setting VOR2 to {degrees}".format(degrees=obs2.degrees))
            self.vor2_set(obs2.degrees)

    def event_to_current_action(self, event):
        if event.type == pygame.JOYBUTTONUP:
            if event.button == 36:
                self.current_action = ACTION_VOR1
            elif event.button == 37:
                self.current_action = ACTION_VOR2
    
    def is_compass_event(self, event):
        if event.type != pygame.JOYBUTTONUP:
            return False        
        if event.button >= 0 and event.button <= 8:
            return True
        return False

    def event_to_compass(self, event, degrees):
        compass = Compass(degrees)
        if event.button == 0 or event.button == 3 or event.button == 6:
            compass.reset()
        elif event.button == 7:
            compass.inc()
        elif event.button == 8:                
            compass.dec()
        elif event.button == 4:
            compass.inc(5)
        elif event.button == 5:
            compass.dec(5)
        elif event.button == 1:
            compass.inc(30)
        elif event.button == 2:
            compass.dec(30)
        return compass


