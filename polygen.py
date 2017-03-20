# -*- coding: utf-8 -*-
import numpy as np
import cv2
import math as m
#Importing Planar package to calculate the vertices of polygon
from planar import Polygon as p

#Making sure input is >3 as per polygon definition
s = int(raw_input('Enter no. of sides (min 3) : '))
while(s<3):
    s = int(raw_input('Please enter 3 or more sides to draw a Polygon : '))

#Laying out the background
jpg = np.zeros((100,100,1), np.uint8)
area = 0

#Itterating over calculation of polygon parameters until given condition (area >2000 & <6000) is satisfied
#Radius(r) of polygon calculated from a range between 25 to 43 (25 radius indicates a maximum possible area of 2000 if drawn as circle and 43 radius indicates a maximum possible area of 6000 if drawn as circle)
#Area of Polygon is calculated using the standard formula [(radius)²x(no. of sides)x(360÷(no. of sides))]÷2
while(area<2000 or area>6000):
    r = 25 + np.random.randint(0,18)
    deg = 360/s
    rad = (3.14*deg)/180
    area = (r*r*s*(m.sin(rad)))/2
    if (area>2000 and area<6000):
        #Once area condition is satisfied we start adding polygon vertices to the array(poly) using p.regular(for drawing a regular polygon)
        poly = p.regular(s,radius = r,center = (50,50), angle=0)
        break
        
#Lines are sequentially drawn from point 0 in array(poly) to point s and back to 0 in order to close the figure
for k in range(s-1):
    cv2.line(jpg,(int(poly[k][0]),int(poly[k][1])),(int(poly[k+1][0]),int(poly[k+1][1])),(255,255,255), 2)
    k = k+1
cv2.line(jpg,(int(poly[k][0]),int(poly[k][1])),(int(poly[0][0]),int(poly[0][1])),(255,255,255), 2)   

#Finally displaying the image and area of polygon and then saving it as per the given convention <n>__<P>.jpg
cv2.imshow('img', jpg)
name = str(s)+'_'+str(int(area))
print 'Area of Polygon = '+str(area)+' and the image has been save as '+str(name)+'.jpg'
name = str(s)+'_'+str(int(area))
cv2.imwrite(name+'.jpg', jpg)