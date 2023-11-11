from .base import Objects


class Stadium(Objects):
    def __init__(self, app, vao_name='stadium', tex_id='stadium',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(1,1,1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()