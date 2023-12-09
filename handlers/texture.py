import pygame as pg
import moderngl as mgl


class Texture:
    def __init__(self, ctx):
        self.ctx = ctx
        self.textures = {}
        self.textures['field'] = self.get_texture(path='textures/campo_2.jpg')
        self.textures['player_local'] = self.get_texture(path='textures/local_uniform.png')
        self.textures['player_visitant'] = self.get_texture(path='textures/away_uniform.png')
        self.textures['porteria_local'] = self.get_texture(path='textures/post.jpg')
        self.textures['porteria_visitant'] = self.get_texture(path='textures/post.jpg')
        self.textures['grada'] = self.get_texture(path='textures/GradaEscalera_3B.jpg')
        self.textures['ball'] = self.get_texture(path='textures/kahverengi.png')
        self.textures['stadium'] = self.get_texture(path='textures/stadium_base.png')
        self.textures['hc'] = self.get_texture(path='textures/coach.png')
        self.textures['referee'] = self.get_texture(path='textures/referee.png')
        self.textures['stats'] = self.get_texture(path='textures/aaa.jpeg')
        self.textures['fans'] = self.get_texture(path='textures/fans.jpg')
        self.textures['cocacola'] = self.get_texture(path='textures/cocacola.jpeg')

    def get_texture(self, path):
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))
        # mipmaps
        texture.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)
        texture.build_mipmaps()
        # AF
        texture.anisotropy = 32.0
        return texture

    def destroy(self):
        [tex.release() for tex in self.textures.values()]