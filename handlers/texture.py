import pygame as pg
import moderngl as mgl


class Texture:
    def __init__(self, ctx):
        self.ctx = ctx
        self.textures = {}
        self.textures['field'] = self.get_texture(path='models/cat/campo_2_1.jpg')
        self.textures['player_local'] = self.get_texture(path='models/cat/equipacion_local.jpg')
        self.textures['player_visitant'] = self.get_texture(path='models/cat/equipacion_visitante.jpg')
        self.textures['porteria_local'] = self.get_texture(path='models/cat/post.jpg')
        self.textures['porteria_visitant'] = self.get_texture(path='models/cat/post.jpg')
        self.textures['grada'] = self.get_texture(path='models/GradaEscalera_3B.jpg')
        self.textures['ball'] = self.get_texture(path='textures/beyaz.png')




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