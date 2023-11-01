from .base import Objects


class Grada(Objects):
    def __init__(self, app, vao_name='grada', tex_id='grada',
                 pos=(0, 0, 0), rot=(0, -90, 0), scale=(0.4,0.4,0.2)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()