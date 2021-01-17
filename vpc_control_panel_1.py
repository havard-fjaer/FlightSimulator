
"""
Virpil VPC Control Panel #1
"""
import pygame
from SimConnect import *
from compass import *

class VpcControlPanel1:
    """
    Handles event from VPC Panel
    """
    def __init__(self, sim_connect):
        aircraft_events = AircraftEvents(sim_connect)
        self.aircraft_requests = AircraftRequests(sim_connect, _time=10)
        self.current_action = "none"
        
        # VOR1
        self.vor1_obi_inc = aircraft_events.find("VOR1_OBI_INC")
        self.vor1_obi_dec = aircraft_events.find("VOR1_OBI_DEC")
        self.vor1_set = aircraft_events.find("VOR1_SET")
        
        # VOR2
        self.vor2_obi_inc = aircraft_events.find("VOR2_OBI_INC")
        self.vor2_obi_dec = aircraft_events.find("VOR2_OBI_DEC")
        self.vor2_set = aircraft_events.find("VOR2_SET")
        
        



    def handle_event(self, event):
        if event.type == pygame.JOYBUTTONUP:
            print("Button up: {button}".format(button=event.button))
            if event.button == 36:
                self.current_action = "VOR1"
            elif event.button == 37:
                self.current_action = "VOR2"

            elif self.current_action == "VOR1":
                obs1 = int(self.aircraft_requests.get("NAV_OBS:1"))
                if event.button == 4:
                    if obs1 >= 350:
                        self.vor1_set(0)
                    else:
                        self.vor1_set(obs1+10)
                elif event.button == 5:
                    if obs1 <= 0:
                        self.vor1_set(350)
                    else:
                        self.vor1_set(obs1-10)
                elif event.button == 6:
                    self.vor1_set(0)
                elif event.button == 7:
                    self.vor1_obi_inc()
                elif event.button == 8:                
                    self.vor1_obi_dec()
                print(obs1)

            elif self.current_action == "VOR2":
                if event.button == 6:
                    self.vor2_set(0)
                elif event.button == 7:
                    self.vor2_obi_inc()
                elif event.button == 8:                
                    self.vor2_obi_dec()
                print(self.aircraft_requests.get("NAV_OBS:2"))



