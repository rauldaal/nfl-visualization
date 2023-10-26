
import glm
import numpy as np


class Ball:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.vbo = self.get_vbo()
        self.shader_program = self.get_shader_program()
        self.vao = self.get_vao(self.vbo)
        self.m_model = self.get_model_matrix()
        self.on_init()

    def get_model_matrix(self):
        m_model = glm.rotate(glm.mat4(), glm.radians(45), glm.vec3(0, 1, 0))
        return m_model

    def on_init(self):
        self.shader_program['light.position'].write(self.app.light.position)
        self.shader_program['light.Ia'].write(self.app.light.Ia)
        self.shader_program['light.Id'].write(self.app.light.Id)
        self.shader_program['m_proj'].write(self.app.camera.m_proj)
        self.shader_program['m_view'].write(self.app.camera.m_view)
        self.shader_program['m_model'].write(self.m_model)

    def render(self):
        self.vao.render()

    def destroy(self):
        self.vbo.release()
        self.shader_program.release()
        self.vao.release()

    def get_vao(self, vbo):
        vao = self.ctx.vertex_array(self.shader_program, [(vbo, '3f 3f 3f', 'in_color', 'in_normal', 'in_position')])
        return vao

    def get_vertex_data(self, num_phi_samples=10, num_theta_samples=10):
        vertices = [# Vertices para el cubo
                    (0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0),
                    (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1),
                    # Vertices para el triangulo
                    (0.5, 1, 1), (0.5, 1.5, 1), (0, 1.5, 0), (1, 1.5, 0),
                    ]

        indices = [(0, 1, 2), (0, 2, 3), (4, 5, 6), (4, 6, 7),
                   (0, 1, 5), (0, 5, 4), (2, 3, 7), (2, 7, 6),
                   (0, 3, 7), (0, 7, 4), (1, 2, 6), (1, 6, 5),
                   (3, 2, 11), (3, 10, 11), (9, 10, 11)]

        vertex_data = self.get_data(vertices, indices)
        return vertex_data
