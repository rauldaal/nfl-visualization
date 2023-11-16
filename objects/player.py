from .base import Objects


class Player_Local(Objects):
    def __init__(self, app, vao_name='player_local', tex_id='player_local',
                 pos=(0, 0, 0), rot=(-90, 180, 0), scale=(0.015,0.015,0.015)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()


class Player_Visitant(Objects):
    def __init__(self, app, vao_name='player_visitant', tex_id='player_visitant',
                 pos=(0, 0, 0), rot=(-90, 0, 0), scale=(0.015,0.015,0.015)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()