from .base import Objects
import glm

class Ball(Objects):
    def __init__(self, app, vao_name='ball', tex_id='ball',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()
        
    def update(self, pos, o):
        # change pos + orientation
        m_model = glm.translate(self.m_model, (0, 0, 0))
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1)) # mirar o!!
        m_model = glm.translate(m_model, pos)
        self.m_model = m_model
        super().update()
