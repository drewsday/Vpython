from __future__ import division
from visual import *
scene.width = 800
scene.height = 800

#CONSTANTS
G = 6.7e-11
mEarth = 6e24
mcraft = 15e3
deltat= 60

#OBJECTS AND INITIAL VALUES
Earth = sphere(pos=(0,0,0), radius=6.4e6, color=color.white,material=materials.BlueMarble)
craft = sphere(pos=(-10*Earth.radius,0,0),radius=1e6,color=color.yellow)
trail = curve(color=craft.color) ## for leaving a trail behind spacecraft
vcraft = vector(0,2e3,0)
pcraft = mcraft*vcraft
t = 0

#CALCULATION LOOP: ALL REPEATED CALCULATIONS GO HERE
while t < 10*365*24*60*60:
    rate(100)
    force = G * mEarth * mcraft / mag(craft.pos)**2
    Force = (force*Earth.pos)
    pcraft = pcraft + Force*deltat
    craft.pos = craft.pos + (pcraft/mcraft)*deltat
    trail.append(pos=craft.pos)
    t = t + deltat
    