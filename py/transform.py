from OpenGL.GL import (glClear, glTranslatef, glEnable, glBegin,
    GL_CULL_FACE, GL_DEPTH_TEST, GL_BACK, GL_COLOR_BUFFER_BIT,
    GL_DEPTH_BUFFER_BIT, glBegin, GL_TRIANGLES, glColor3fv, glVertex3fv,
    glCullFace, glEnd, glRotatef
)
 
from OpenGL.GLU import gluPerspective

def rotate(angle, axis):
    glRotatef(angle, axis[0], axis[1], axis[2])
   
def getAngle(msec):
    degrees_per_sec = 360./5.
    degrees_per_msec = degrees_per_sec / 1000.
    
    return msec * degrees_per_msec;

def rotate_by_time(msec, axis):
    angle = getAngle(msec)
    
    axisX = (1, 0, 0);
    axisY = (0, 1, 0)
    axisZ = (0, 0, 1)
    
    rotate(angle, axis)
