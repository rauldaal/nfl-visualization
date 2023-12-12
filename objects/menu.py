from .base import BaseModel
import glm

class Menu(BaseModel):
    def __init__(self, app, vao_name='field', tex_id='menu',
                 pos=(0, 0, 0), rot=(-90, 180, 0), scale=(0.08,0.2,0.08)):
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

        # Set up perspective projection matrix to cover the entire screen
        screen_width, screen_height = 1600,780
        aspect_ratio = screen_width / screen_height
        fov = 45.0  # Adjust the field of view as needed

        m_proj = glm.perspective(glm.radians(fov), aspect_ratio, 0.1, 100.0)
        self.program['m_proj'].write(m_proj)

        # mvp
        self.program['m_view'].write(glm.mat4(1.0))
        self.program['m_model'].write(self.m_model)
