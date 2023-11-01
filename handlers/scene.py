from objects import Porteria_Visitant, Porteria_Local, Player_Local, Player_Visitant, Field, Grada, Ball
import numpy as np


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self, data=None):
        app = self.app
        add = self.add_object
        
        ball_pos_x = 0
        ball_pos_y = 0

        if data is not None:
            ball_pos_x = data[data['nflId'].isna()]['x'].values[0]
            ball_pos_y = data[data['nflId'].isna()]['y'].values[0]

        add(Field(app, pos=(0,0,0)))
        add(Ball(app, pos=(ball_pos_x, 2, ball_pos_y)))

        x=0
        for i in range(11):                
            add(Player_Local(app, pos=(x, 0, -20)))
            if i%2==0:
                x+=1.5*(i+1)
            else:
                x-=1.5*(i+1)

        x=0
        for i in range(11):                
            add(Player_Visitant(app, pos=(x, 0, 20)))
            if i%2==0:
                x+=1.5*(i+1)
            else:
                x-=1.5*(i+1)

        #porterias
        add(Porteria_Local(app, pos= (0,0,-38)))

        #porterias
        add(Porteria_Visitant(app, pos= (0,0,38)))
        '''

         x=0
        for i in range(50):                
            add(Grada(app, pos= (20,0,x)))
            if i%2==0:
                x+=1.5*(i+1)
            else:
                x-=1.5*(i+1)
        '''

        x=0
        n = 20
        y = 0
        for p in range(0,8):
            for i in range(50):                
                add(Grada(app, pos= (-n,p,x)))
                if i%2==0:
                    x+=1.5*(i+1)
                else:
                    x-=1.5*(i+1)
            x=0
            n+=2
            y+=0.5
               

    def render(self, data=None):
        self.objects = []
        self.load(data)
        for obj in self.objects:
            obj.render()