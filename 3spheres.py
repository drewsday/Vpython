from __future__ import division
from visual import *

#first program for students to do
#helps introduce vectors in Vpython

ball1 = sphere(pos=(10,10,0),color=color.green, radius=1)
ball2 = sphere(pos=(-10,10,0),color=color.red, radius=1)
ball3 = sphere(pos=(0,0,0),color=color.blue,radius=1)

pointer1 = arrow(pos=(10,10,0),color=color.green,axis=(-20,0,0),shaftwidth=0.5)
pointer2 = arrow(pos=(-10,10,0),color=color.red,axis=(10,-10,0),shaftwidth=0.5)
pointer3 = arrow(pos=(0,0,0),color=color.blue,axis=(10,10,0),shaftwidth=0.5)