from pygame_app import *
from drawer import *
from octa import *
from transform import *
 
axisX = (1, 0, 0);
axisY = (0, 1, 0)
axisZ = (0, 0, 1)

norm1Z = (1, 1, 1)
norm2Z = (-1, 1, 1)
norm3Z = (-1, -1, 1)
norm4Z = (1, -1, 1)

vert2 = (1, 1, 0)
 
class App:
    def __init__(self):
        print('__init__');
        
        self._running = True
        self.clock = None
        self.msec = None
        
        self.light = (1, 2, 3)

        self.octa = Octahedron([0, 0, 2])
 
    def on_init(self):
        print('on_init');
        
        pygame.init()
        self._running = True
        
        display = (400, 400)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
        
        gluPerspective(45, 1, 0.1, 50.0)
        glTranslatef(0.0, 0.0, -15)
        
        angle = 45
        
        # ~ rotate(angle, norm1Z)
        
        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)
        glCullFace(GL_BACK)

        self.clock = pygame.time.Clock()
 
    def on_event(self, event):
        print('on_event');
        
        if event.type == pygame.QUIT:
            self._running = False
            
            
    def on_loop(self):
        print('on_loop')
        # ~ handle Events
        # 
        # ~ glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        #
        # ~ do Transformations And Drawing 
        #
        # ~ pg.display.flip()
        #
        # ~ pg.time.wait(1)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        self.msec = self.clock.tick()
        # ~ print(self.msec)

        faces = self.octa.getFaces()
        # ~ print(faces)

        glBegin(GL_TRIANGLES)
        for face in faces:
            color = shade(face, blues, self.light)

            for vertex in face:
                glColor3fv((color[0], color[1], color[2]))
                glColor3fv((color[0], color[1], color[2]))
                glVertex3fv(vertex)
        glEnd()

        rotate_by_time(self.msec, axisZ)

        pygame.display.flip()

    
    def on_render(self):
        print('on_render');
        
    def on_cleanup(self):
        print('on_event');
        
        pygame.quit()
     
    def on_execute(self):
        print('on_execute');
        
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
                
            self.on_loop()
            
            self.on_render()
            
            print('--')
            
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
