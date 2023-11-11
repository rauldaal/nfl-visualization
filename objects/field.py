from .base import Objects

class Field(Objects):
    def __init__(self, app, vao_name='field', tex_id='field', pos=(0, 0, 0), rot=(0, 90, 0), scale=(2, 2, 2)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()