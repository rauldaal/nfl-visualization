import numpy as np
import moderngl as mgl
import pywavefront


class VBO:
    def __init__(self, ctx):
        self.vbos = {}
        self.vbos['field'] = Field(ctx)
        self.vbos['player_local'] = PlayerVBO(ctx)
        self.vbos['player_visitant'] = PlayerVBO(ctx)
        self.vbos['porteria_local'] = PorteriaVBO(ctx)
        self.vbos['porteria_visitant'] = PorteriaVBO(ctx)
        self.vbos['grada'] = GradaVBO(ctx)
        self.vbos['ball'] = BallVBO(ctx)
        self.vbos['stadium'] = Stadium(ctx)
        self.vbos['hc'] = Person(ctx)
        self.vbos['referee'] = Person(ctx)
        self.vbos['fans'] = Fans(ctx)

    def destroy(self):
        [vbo.destroy() for vbo in self.vbos.values()]


class BaseVBO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = self.get_vbo()
        self.format: str = None
        self.attribs: list = None

    def get_vertex_data(self): ...

    def get_vbo(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo

    def destroy(self):
        self.vbo.release()

class Field(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        #objs = pywavefront.Wavefront('models/cat/20430_Cat_v1_NEW.obj', cache=True, parse=True)
        #objs = pywavefront.Wavefront('models/stadium.obj', cache=True, parse=True)
        objs = pywavefront.Wavefront('models/field2/field.obj', cache=True, parse=True)

        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data

class Stadium(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        #objs = pywavefront.Wavefront('models/cat/20430_Cat_v1_NEW.obj', cache=True, parse=True)
        #objs = pywavefront.Wavefront('models/stadium.obj', cache=True, parse=True)
        objs = pywavefront.Wavefront('models/stadium/stadium6.obj', cache=True, parse=True)

        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data


class PlayerVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        #objs = pywavefront.Wavefront('models/cat/20430_Cat_v1_NEW.obj', cache=True, parse=True)
        #objs = pywavefront.Wavefront('models/stadium.obj', cache=True, parse=True)
        objs = pywavefront.Wavefront('models/player/player.obj', cache=True, parse=True)

        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
    
class PorteriaVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('models/goalpost/porteria_good.obj', cache=True, parse=True)

        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
    
class GradaVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('models/grada/grada.obj', cache=True, parse=True)

        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data


class BallVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('models/ball/ball.obj', cache=True, parse=True)

        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data

class Person(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('models/person/person.obj', cache=True, parse=True)

        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data

class Fans(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('models/fans/fans.obj', cache=True, parse=True)

        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
















