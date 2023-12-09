from .base import BaseModel
import glm

class Stats(BaseModel):
    def __init__(self, app, vao_name='field', tex_id='stats',
                 pos=(0, 0, 0), rot=(-90, 180, 0), scale=(0.008,0.001,0.012)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()
        
    def update(self):
        self.texture.use()
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(glm.mat4(1.0))
        self.program['m_model'].write(self.m_model)
        
    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_0'] = 0
        self.texture.use()
        # mvp
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(glm.mat4(1.0))
        self.program['m_model'].write(self.m_model)