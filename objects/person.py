from .base import Objects


class Person(Objects):
    def __init__(self, app, vao_name='hc', tex_id='hc',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(1.5, 1.5, 1.5)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()
