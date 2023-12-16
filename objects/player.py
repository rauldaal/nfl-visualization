from .base import Objects
import glm

class Player_Local(Objects):
    def __init__(self, app, vao_name='player_local', tex_id='player_local',
                 pos=(0, 0, 0), rot=(-90, 180, 0), scale=(0.015,0.015,0.015)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.points = []
        self.on_init()
        
    def move(self, x, y, angle):
        self.pos = (x, self.pos[1], y)
        translation_vector = glm.vec3(self.pos[0], 0, self.pos[2])
        origin = glm.translate(glm.mat4(1.0), translation_vector)
        new_angle = glm.rotate(glm.mat4(1.0), glm.radians(angle), (0,1,0))
        stand_up = glm.rotate(glm.mat4(1.0), glm.radians(-90), (1,0,0))
        self.m_model = origin * glm.scale((0.015,0.015,0.015)) * new_angle * stand_up

class Player_Visitant(Objects):
    def __init__(self, app, vao_name='player_visitant', tex_id='player_visitant',
                 pos=(0, 0, 0), rot=(-90, 0, 0), scale=(0.015,0.015,0.015)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.points = []
        self.on_init()
        
    def move(self, x, y, angle):
        self.pos = (x, self.pos[1], y)
        translation_vector = glm.vec3(self.pos[0], 0, self.pos[2])
        origin = glm.translate(glm.mat4(1.0), translation_vector)
        new_angle = glm.rotate(glm.mat4(1.0), glm.radians(angle), (0,1,0))
        stand_up = glm.rotate(glm.mat4(1.0), glm.radians(-90), (1,0,0))
        self.m_model = origin * glm.scale((0.015,0.015,0.015)) * new_angle * stand_up
