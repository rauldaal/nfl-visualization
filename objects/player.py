from .base import Objects
import glm

class Player_Local(Objects):
    def __init__(self, app, vao_name='player_local', tex_id='player_local',
                 pos=(0, 0, 0), rot=(-90, 0, 0), scale=(0.015,0.015,0.015)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()
        
    def update(self, pos, o):
        # change pos + orientation
        i = glm.mat4(1.0)
        rotation = glm.rotate(i, o) # m_model, self.rot.z, glm.vec3(0, 0, 1)
        transform = glm.translate(rotation, pos)
        # m_model = glm.translate(self.m_model, (0, 0, 0))
        # m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1)) # mirar o!!
        # m_model = glm.translate(m_model, pos)
        self.m_model = m_model * transform
        super().update()

class Player_Visitant(Objects):
    def __init__(self, app, vao_name='player_visitant', tex_id='player_visitant',
                 pos=(0, 0, 0), rot=(-90, 180, 0), scale=(0.015,0.015,0.015)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()
        
    def update(self, pos, o):
        # change pos + orientation
        m_model = glm.translate(self.m_model, (0, 0, 0))
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1)) # mirar o!!
        m_model = glm.translate(m_model, pos)
        self.m_model = m_model
        super().update()