from model import *


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        add(Cube(app, pos=(0,0,0)))
        
        x=0
        for i in range(11):                
            add(Cat(app, pos=(x, 0, -20)))
            if i%2==0:
                x+=1.5*(i+1)
            else:
                x-=1.5*(i+1)

        x=0
        for i in range(11):                
            add(Cat_visitante(app, pos=(x, 0, 20)))
            if i%2==0:
                x+=1.5*(i+1)
            else:
                x-=1.5*(i+1)

        #porterias
        add(Porteria(app, pos= (0,0,38)))

                #porterias
        add(Porteria(app, pos= (0,0,-38)))

        

    def render(self):
        for obj in self.objects:
            obj.render()