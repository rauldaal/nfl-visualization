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
    Menu,
    )
from math import isnan
from .stats_generator import Voronoi_Generator


class Scene:
    def __init__(self, app, data):
        self.app = app
        self.objects = []
        self.static_objects = []
        self.moving_objects = dict()
        self.vg = Voronoi_Generator()
        self.load(data)

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self, data=None, prev_data=None, voronoi=False):
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
        # add(Stadium(app, pos=(61, 0, 27.5)))
        # add(Field(app, pos=(61, 0, 27.5), rot=(0, 0, 0)))
        # add(Ball(app, pos=(ball_pos_x, 2, ball_pos_y)))
        self.static_objects.append(Stadium(app, pos=(61, 0, 27.5)))
        self.static_objects.append(Field(app, pos=(61, 0, 27.5), rot=(0, 0, 0)))
        self.moving_objects['ball'] = Ball(app, pos=(ball_pos_x, 2, ball_pos_y))
        x = 0
        angle = 0
        for i in range(11):
            x = 0
            z = 20
            if players_local is not None:
                x = players_local.iloc[i]['x']
                z = players_local.iloc[i]['y']
                angle = players_local.iloc[i]['dir']
            # add(Player_Local(app, pos=(x, 0.2, z), rot=(-90, angle, 0)))
            player_id = str(int(players_local.iloc[i]['nflId']))
            self.moving_objects[player_id] = Player_Local(app, pos=(x, 0.2, z), rot=(-90, angle, 0))
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
            # add(Player_Visitant(app, pos=(x, 0.2, z), rot=(-90, angle, 0)))
            player_id = str(int(players_visitor.iloc[i]['nflId']))
            self.moving_objects[player_id] = Player_Visitant(app, pos=(x, 0.2, z), rot=(-90, angle, 0))
            jugadors.append((x, 2.5, z))

        self.static_objects.append(Porteria_Local(app, pos=(0, 0, 27.5), rot=(0, 0, 0)))
        self.static_objects.append(Porteria_Visitant(app, pos=(122, 0, 27.5), rot=(0, 180, 0)))
        self.static_objects.append(Person(app, pos=(30, 0.2, 0)))
        self.static_objects.append(Referee(app, pos=(110, 0.2, 56), rot=(0, 180, 0)))
        self.static_objects.append(Referee(app, pos=(112, 0.2, 0), rot=(0, 0, 0)))
        self.static_objects.append(Referee(app, pos=(90, 0.2, 10), rot=(0, 0, 0)))
        self.static_objects.append(Fans(app, pos=(60, 27.5, 80), rot=(0, 0, 0), scale=(0.6, 1, 0.8)))
        self.static_objects.append(Fans(app, pos=(60, 27.5, -30), rot=(0, 180, 0), scale=(0.6, 1, 0.8)))
        self.static_objects.append(Fans(app, pos=(147, 27.5, 30), rot=(30, 90, 0), scale=(0.3, 1, 0.2)))
        self.static_objects.append(Fans(app, pos=(-24, 27.5, 30), rot=(30, 90+180, 0), scale=(0.25, 1, 0.2)))
        self.static_objects.append(Cocacola(app, pos=(-20, 47,-20), scale=(0.5, 0.5, 0.5), rot=(0, 45, 0)))
        self.static_objects.append(Cocacola(app, pos=(143, 45, 75), scale=(0.45, 0.45, 0.45), rot=(0, 225, 0)))

        # if prev_data is not None:
        #     for i in range(len(prev_data)):
        #         x = prev_data.iloc[i]['x']
        #         z = prev_data.iloc[i]['y']
        #         self.static_objects.append(Point(app, pos=(x, 0.3, z), rot=(0, 0, 0)))

        return jugadors

    def render(self, data=None, prev_data=None, voronoi=False):
        offset = (1.9, 1.2, -4)  
        jugadors = []
        pos_objeto = (offset[0], offset[1], offset[2])
        if self.app.show_menu:
            m = Menu(self.app, pos=(0,0,-15))
            m.render()
        else:
            if self.app.estadisticas:
                p = self.app.WIN_SIZE
                s = p[0] / p[1]
                offset = (p[0] * 0.00160, s * .80, -4)
                s1 = Stats(self.app, pos=(offset[0],offset[1],offset[2]),
                                scale=(0.005 * s, 0.0005, 0.007 * s), tex_id='stats1')
                pos_objeto = (offset[0], offset[1]-1.2, offset[2])
                s2 = Stats(self.app, pos=(pos_objeto[0],pos_objeto[1],pos_objeto[2]),
                                scale=(0.005 * s, 0.0005, 0.007 * s), tex_id='stats2')
                pos_objeto = (offset[0], offset[1]-2.4, offset[2])
                s3 = Stats(self.app, pos=(pos_objeto[0],pos_objeto[1],pos_objeto[2]),
                                scale=(0.005 * s, 0.0005, 0.007 * s), tex_id='stats3')
                s1.render()
                s2.render()
                s3.render()
            for obj in self.static_objects:
                obj.render()
            for player_id in data['nflId']:
                if isnan(player_id):
                    continue
                x = data[data['nflId'] == player_id]['x'].values[0]
                z = data[data['nflId'] == player_id]['y'].values[0]
                angle = data[data['nflId'] == player_id]['dir']
                player_id = str(int(player_id))
                player = self.moving_objects[player_id]
                player.move(x, z, angle)
                player.render()
                player.points.append((x, z))
                if prev_data:
                    num_points = min(prev_data, len(player.points))
                    for point in player.points[-num_points:]:
                        p = Point(self.app, pos=(point[0], 0.3, point[1]), rot=(0, 0, 0))
                        p.render()
                jugadors.append((x, 2.5, z))
            ball_pos_x = data[data['nflId'].isna()]['x'].values[0]
            ball_pos_y = data[data['nflId'].isna()]['y'].values[0]
            self.moving_objects['ball'].move(ball_pos_x, ball_pos_y)
            self.moving_objects['ball'].render()
            if voronoi:
                self.vg.compute_voronoi(data=data, frame=self.app.frame)
                self.app.mesh.add_voronoi_texture()
                v = Field(self.app, pos=(61, 0.1, 27.5), rot=(0, 180, 0), vao_name='voronoi', tex_id='voronoi')
                v.render()
        return jugadors