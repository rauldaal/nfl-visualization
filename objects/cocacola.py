from .base import Objects


class Cocacola(Objects):
    def __init__(self, app, vao_name='cocacola', tex_id='cocacola',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(1,1,1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()