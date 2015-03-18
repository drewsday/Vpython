#spring_mass_sim.py

from visual import *
from visual.graph import *
from math import *

import sys
import os
#from PIL import ImageGrab

# This is my vPython simumilatiomn of mass spring system.
# Based on Rhett Allain's blog entry:
# http://www.wired.com/2014/07/how-do-you-model-a-spring/
#
# assume spring only vibrates in the vertical plane and is massless 
#
# slight improvements for generating images of output for animated gif
# with ImageMagik : ' convert -delay 20 *.png spring_d0.gif'
# 

############## System Constants : Change These #########################

# NOTE : k=2, m=1 critical damping occurs at beta=2.284727

k=2                        # spring constant
m=1.0                      # mass on end of spring
accg=9.8                   # acceleration due to gravity 
L0=1.0                     # natural length of spring 
height = 10                # initial height of spring/mass above floor
beta = 0.284727            # damping constant 
time = 30                  # number of seconds simulation runs for 

save_data = 0              # flags saving images of simulation 

#########################################################################

SaveDirectory=r'C:\Users\Tim\Documents\Teaching\Advanced Physics\Simulations\SHM\images'
image_num=100

g=vector(0,9.8,0)          

# setup the display
scene.x=0
scene.y=0
scene.width= 450
scene.height= 500

scene.title = "Sping-Mass System : m="+str(m)+", k="+str(k)+", L0="+str(L0)+", beta="+str(beta)
scene.center = (0,-6,0)

# boundaries to world 
ceiling = box(length=4, height=0.2, width=0, color=color.orange, pos=(0,0,0))
floor = box(length=4, height=0.2, width=0, color=color.orange, pos=(0,-(L0+height+1),0))

# initialize spring
spring = helix(pos=(0,0,0), axis=(0,-L0,0), radius=0.2, color=color.white)
spring.top = vector(0,0,0)                      # top of spring 
spring.bottom = vector(0,-L0,0)                 # bottom of spring 
spring.Le = vector(0,0,0)                       # extension of spring 

# initialize mass
mass = sphere(radius=0.5,color=color.white)     
mass.pos=spring.bottom                          # position of mass 
mass.m=m;                                       # mass of ... er ... mass        
mass.p=vector(0,0,0)                            # momentum vector of mass

# initialize time 
t  = 0.0                     # time counter
dt =  0.01                   # time steps for calculation

# initialize graphing
gdisplay(x=450,y=0,title="Position vs. Time for Sping-Mass System : m="+str(m)+", k="+str(k)+", L0="+str(L0)+", beta="+str(beta), xtitle='t/s', ytitle='y/m',width=800,height=500)
pos_curve = gcurve(color=color.blue)

# main calculation loop
while t<=time:

    rate(100)                                   

    #update the forces (damped)         
    F = k*spring.Le -m*g - beta*mass.p/m # F=-m*g-k*Le-beta*v

    # calculate the new momentum 
    mass.p=mass.p+F*dt                  # p_new = p_old+F*dt

    # update the position of the mass
    dy = mass.p*dt/m;                   # p*dt/m    
    mass.pos=mass.pos+dy                # y_new = y_old+p*dt/m

    # update spring length and extension
    spring.bottom = mass.pos
    spring.L=spring.top-spring.bottom   #spring length
    spring.Le=spring.L-vector(0,L0,0)   #the extension 
    spring.axis=-spring.L               #axis for spring

    # update graphs
    pos_curve.plot(pos=(t,spring.bottom.y))

    # image grab every 0.5 of a second in calculation time
#    if save_data==1 and (t*100)%50<1 :  
#      image=ImageGrab.grab(bbox=(0,0,1250,500))
#      saveas=os.path.join(SaveDirectory,str(image_num)+'.png')
#      image.save(saveas)
#      image_num+=1
        
    # time step
    t=t+dt
