from .base import Objects
import glm


class Ball(Objects):
    def __init__(self, app, vao_name='ball', tex_id='ball',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(2, 2, 2)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def move(self, x, y):
        self.pos = (x, self.pos[1], y)
        translation_vector = glm.vec3(self.pos[0], self.pos[1], self.pos[2])
        origin = glm.translate(glm.mat4(1.0), translation_vector)
        self.m_model = origin * glm.scale((2,2,2))
