from .base import Objects


class Porteria_Local(Objects):
    def __init__(self, app, vao_name='porteria_local', tex_id='porteria_local',
                 pos=(0, 0, 0), rot=(-90, -90, 90), scale=(0.3, 0.3, 0.25)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()


class Porteria_Visitant(Porteria_Local):
    def __init__(self, app, vao_name='porteria_visitant', tex_id='porteria_visitant',
                 pos=(0, 0, 0), rot=(180, 90, 180), scale=(0.3, 0.3, 0.25)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()
