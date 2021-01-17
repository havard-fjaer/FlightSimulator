# FlightSimulator
Maps joystick events to SimConnnect events.

## Caveat
Uses pygame for picking up events from joysticks. However, pygame requires that its GUI is focused in order to pick up events. 
Thus, the whole thing stops working as soon as I get into the flight simulator. Need to fix this, or replace pygame with something else.
