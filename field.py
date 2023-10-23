# basado en: https://www.youtube.com/watch?v=eJDIsFJN4OQ
import pygame as pg
import moderngl as mgl
import glm
import sys
from stl import mesh

import numpy as np

class Camera:
    def __init__(self, app):
        self.app = app
        self.aspec_ratio = app.WIN_SIZE[0]/app.WIN_SIZE[1]
        self.position =glm.vec3(1000,1000,1000)
        self.up = glm.vec3(1,0,0)
        # view_matrix
        self.m_view = self.get_view_matrix()
        # projection matrix
        self.m_proj = self.get_projection_matrix()
        
    def get_view_matrix(self):
        return glm.lookAt(self.position, glm.vec3(0), self.up)
    
    def get_projection_matrix(self):
        return glm.perspective(glm.radians(45), self.aspec_ratio, 0.1, 100)
    
class Field:
    def __init__(self,app, type):
        self.app = app
        self.ctx = app.ctx
        self.type = type
        self.vbo = self.get_vbo()
        self.shader_program = self.get_shader_program()
        self.vao = self.get_vao()
        self.m_model = self.get_model_matrix()
        self.on_init()
        
    def get_model_matrix(self):
        #m_model = glm.mat4()
        m_model = glm.rotate(glm.mat4(),glm.radians(0),glm.vec3(0,1,0))
        return m_model
        
    def on_init(self):
        self.shader_program['m_proj'].write(self.app.camera.m_proj)
        self.shader_program['m_view'].write(self.app.camera.m_view)
        scale_vector = glm.vec3(1000e-20, 1000e-20, 1000e-1000)
        scale_matrix = glm.scale(glm.mat4(1.0), scale_vector)
        self.m_model = scale_matrix*self.m_model
        self.shader_program['m_model'].write(self.m_model)

    def render(self):
        if self.type == None:
            self.vao.render()
        else:    
            self.vao.render(self.type)
        
    def destroy (self):
        self.vbo.release()
        self.shader_program.release()
        self.vao.release()
    
    def get_vao(self):
        vao = self.ctx.vertex_array(self.shader_program, [(self.vbo, '3f', 'in_position')])
        return vao
    
    def get_vertex_data(self):
        vertex_data = self.load_stl_model('3d_models/your_model.stl')
        vertex_data = vertex_data.vectors
        return np.reshape(vertex_data, (-1, 3))
    
    def load_stl_model(self, file_path):
        return mesh.Mesh.from_file(file_path)

    @staticmethod
    def get_data(vertices, indices): 
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

    def get_vbo(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo
    
    def get_shader_program(self):
        program = self.ctx.program(    
            vertex_shader='''
                #version 330
                layout (location = 0) in vec3 in_position;
                uniform mat4 m_proj;
                uniform mat4 m_view;
                uniform mat4 m_model;
                void main() {
                    gl_Position = m_proj * m_view * m_model * vec4(in_position, 1.0);
                }
            ''',
            fragment_shader='''
                #version 330
                layout (location = 0) out vec4 fragColor;
                void main() { 
                    vec3 color = vec3(1,1,0);
                    fragColor = vec4(color,1.0);
                }
            ''',
        )
        return program
    
        
class GraphicsEngine:
    def __init__(self, win_size=(900,900)):
        # init pygame modules
        pg.init()
        # window size
        self.WIN_SIZE = win_size
        # set opengl attr
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION,3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION,3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        # create opengl context
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        # detect and use exixting opengl context
        self.ctx = mgl.create_context()
        # camera
        self.camera = Camera(self)
        # scene
        # self.scene = Field(self)
        self.aa = Field(self, mgl.LINE_LOOP)
        
        
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.scene.destroy()
                pg.quit()
                sys.exit()
                
    def render(self):
        # clear framebuffer
        self.ctx.clear(color=(0,0,0))
        # render scene
        # self.scene.render()
        self.aa.render()
        # swap buffers
        pg.display.flip()
        
    def run(self):
         while True:
             self.check_events()
             self.render()
             
        
if __name__ == '__main__':
    app = GraphicsEngine((900, 500))
    app.run()
