from .vao import VAO
from .texture import Texture


class Mesh:
    def __init__(self, app):
        self.app = app
        self.vao = VAO(app.ctx)
        self.texture = Texture(app.ctx)
    def add_voronoi_texture(self):
        self.texture.add_voronoi_texture()
    def add_stats_texture(self):
        self.texture.add_stats_texture()
    def destroy(self):
        self.vao.destroy()
        self.texture.destroy()