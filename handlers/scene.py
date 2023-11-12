from objects import Porteria_Visitant, Porteria_Local, Player_Local, Player_Visitant, Field, Grada, Ball
import numpy as np


class Scene:
    def __init__(self, app):
        self.app = app
        # self.objects = []
        self.objects = dict()
        self.load()

    def add_object(self, obj, obj_id):
        # self.objects.append(obj)
        if obj_id in self.objects.keys():
            raise IndexError(f'{obj_id}')
        self.objects[obj_id] = obj
        
    def update_object(self, obj_id, pos, o=None):
        if obj_id not in self.objects.keys():
            raise IndexError
        self.objects[obj_id].update(pos, o)
        
    def load(self, data=None):
        app = self.app
        add = self.add_object

        ball_pos_x = 0
        ball_pos_y = 0
        players_local = None
        players_visitor = None

        if data is not None:
            ball_pos_x = data[data['nflId'].isna()]['x'].values[0]
            ball_pos_y = data[data['nflId'].isna()]['y'].values[0]
            teams = data['team'].unique().tolist()
            players_local = data[data['team'] == teams[0]]
            players_visitor = data[data['team'] == teams[1]]

        add(Field(app, pos=(26.7, 0, 60)), 'field')
        add(Ball(app, pos=(ball_pos_x, 2, ball_pos_y)), 'ball')

        # Local Team
        # Get id from data
        x=0
        for i in range(11):
            x = 0
            z =20
            if players_local is not None:
                z = players_local.iloc[i]['x']
                x = players_local.iloc[i]['y']
            add(Player_Local(app, pos=(x, 0, z)), f'player_{i}')
            #if i%2==0:
            #    x+=1.5*(i+1)
            #else:
            #    x-=1.5*(i+1)

        # Visit Team
        # Get id from data
        x=0
        for i in range(11, 22):
            x = 0
            z = -20
            if players_visitor is not None:
                x = players_visitor.iloc[i]['x']
                z = players_visitor.iloc[i]['y']          
            add(Player_Visitant(app, pos=(z, 0, x)), f'player_{i}')
            #if i%2==0:
            #    x+=1.5*(i+1)
            #else:
            #    x-=1.5*(i+1)

        #porterias
        add(Porteria_Local(app, pos=(0,0,-38)), 'porteria_local')

        #porterias
        add(Porteria_Visitant(app, pos=(0,0,38)), 'porteria_vis')
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
                add(Grada(app, pos= (-n,p,x)), f'grada_{-n},{p},{x}')
                if i%2==0:
                    x+=1.5*(i+1)
                else:
                    x-=1.5*(i+1)
            x=0
            n+=2
            y+=0.5

    def render(self, data=None):
        # self.objects = []
        # self.load(data)
        for i, obj in self.objects.items():
            pos = (0,0,0)
            o = None
            if 'player' in i or 'ball' in i:
                # coger nueva posicion + o from DATA
                pos = (0,0,0)
                o = None
                obj.update(pos, o=None)
            else:
                obj.update()
            obj.render()