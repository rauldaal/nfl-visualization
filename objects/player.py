from .base import Objects
import glm

class Player_Local(Objects):
    def __init__(self, app, vao_name='player_local', tex_id='player_local',
                 pos=(0, 0, 0), rot=(-90, 180, 0), scale=(0.04,0.04,0.04)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()
        
    def update(self, pos, o):
        # change pos + orientation
        reset_move = (-self.pos[0], -self.pos[1], -self.pos[2])
        m_model = glm.translate(self.m_model, reset_move)
        self.m_model = glm.translate(m_model, pos)
        self.pos = pos
        super().update()

class Player_Visitant(Objects):
    def __init__(self, app, vao_name='player_visitant', tex_id='player_visitant',
                 pos=(0, 0, 0), rot=(-90, 0, 0), scale=(0.04,0.04,0.04)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()
        
    def update(self, pos, o):
        # change pos + orientation
        reset_move = (-self.pos[0], -self.pos[1], -self.pos[2])
        m_model = glm.translate(self.m_model, reset_move)
        self.m_model = glm.translate(m_model, pos)
        self.m_model = m_model
        self.pos = pos
        super().update()