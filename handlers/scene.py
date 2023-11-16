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
    )



class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self, data=None):
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
        return jugadors

    def render(self, data=None):
        self.objects = []
        jugadors = self.load(data)
        for obj in self.objects:
            obj.render()
        return jugadors