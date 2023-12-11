from .base import Objects


class Point(Objects):
    def __init__(self, app, vao_name='point', tex_id='point',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(0.1,0.1,0.1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()