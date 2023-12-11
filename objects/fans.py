from .base import Objects

class Fans(Objects):
    def __init__(self, app, vao_name='fans', tex_id='fans', pos=(10, 3, 10), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()