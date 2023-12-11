from objects import (
    Porteria_Visitant,
    Porteria_Local,
    Player_Local,
    Player_Visitant,
    Field,
    Grada,
    Ball,
    Stadium,
    Person,
    Referee,
    Stats,
    Fans,
    Cocacola,
    Point,
    )



class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self, data=None, prev_data=None):
        jugadors = []
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
        add(Stadium(app, pos=(61, 0, 27.5)))
        add(Field(app, pos=(61, 0, 27.5), rot=(0, 0, 0)))
        add(Ball(app, pos=(ball_pos_x, 2, ball_pos_y)))
        x = 0
        angle = 0
        for i in range(11):
            x = 0
            z = 20
            if players_local is not None:
                x = players_local.iloc[i]['x']
                z = players_local.iloc[i]['y']
                angle = players_local.iloc[i]['dir']
            add(Player_Local(app, pos=(x, 0.2, z), rot=(-90, angle, 0)))
            jugadors.append((x, 2.5, z))


        x=0
        angle = 0
        for i in range(11):
            x = 0
            z = -20
            if players_visitor is not None:
                x = players_visitor.iloc[i]['x']
                z = players_visitor.iloc[i]['y']
                angle = players_local.iloc[i]['dir']
            add(Player_Visitant(app, pos=(x, 0.2, z), rot=(-90, angle, 0)))
            jugadors.append((x, 2.5, z))

        add(Porteria_Local(app, pos=(0, 0, 27.5), rot=(0, 0, 0)))

        add(Porteria_Visitant(app, pos=(122, 0, 27.5), rot=(0, 180, 0)))
        add(Person(app, pos=(30, 0.2, 0)))
        add(Referee(app, pos=(110, 0.2, 56), rot=(0, 180, 0)))
        add(Referee(app, pos=(112, 0.2, 0), rot=(0, 0, 0)))
        add(Referee(app, pos=(90, 0.2, 10), rot=(0, 0, 0)))
        add(Fans(app, pos=(60, 27.5, 80), rot=(0, 0, 0), scale=(0.6, 1, 0.8)))
        add(Fans(app, pos=(60, 27.5, -30), rot=(0, 180, 0), scale=(0.6, 1, 0.8)))
        add(Fans(app, pos=(147, 27.5, 30), rot=(30, 90, 0), scale=(0.3, 1, 0.2)))
        add(Fans(app, pos=(-24, 27.5, 30), rot=(30, 90+180, 0), scale=(0.25, 1, 0.2)))
        
        add(Cocacola(app, pos=(-20, 47,-20), scale=(0.5, 0.5, 0.5), rot=(0, 45, 0)))
        add(Cocacola(app, pos=(143, 45, 75), scale=(0.45, 0.45, 0.45), rot=(0, 225, 0)))


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
            
        if self.app.estadisticas:
            p = self.app.WIN_SIZE
            s = p[0] / p[1]
            offset = (p[0] * 0.00160, s * .80, -4)
            add(stats.Stats(app, pos=(offset[0],offset[1],offset[2]),
                            scale=(0.005 * s, 0.0005, 0.007 * s), tex_id='stats1'))
            pos_objeto = (offset[0], offset[1]-1.2, offset[2])
            add(stats.Stats(app, pos=(pos_objeto[0],pos_objeto[1],pos_objeto[2]),
                            scale=(0.005 * s, 0.0005, 0.007 * s), tex_id='stats2'))
            pos_objeto = (offset[0], offset[1]-2.4, offset[2])
            add(stats.Stats(app, pos=(pos_objeto[0],pos_objeto[1],pos_objeto[2]),
                            scale=(0.005 * s, 0.0005, 0.007 * s), tex_id='stats3'))
        if prev_data is not None:
            for i in range(len(prev_data)):
                x = prev_data.iloc[i]['x']
                z = prev_data.iloc[i]['y']
                add(Point(app, pos=(x, 0.3, z), rot=(0, 0, 0)))

        return jugadors

    def render(self, data=None, prev_data=None):
        self.objects = []
        jugadors = self.load(data, prev_data)
        for obj in self.objects:
            obj.render()
        return jugadors