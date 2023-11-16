from .vbo import VBO
from .shader_program import ShaderProgram


class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        # cube vao
        self.vaos['field'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['field'])

        # cat vao
        self.vaos['player_local'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['player_local'])
        
        self.vaos['player_visitant'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['player_visitant'])
        
        self.vaos['porteria_local'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['porteria_local'])
        
        self.vaos['porteria_visitant'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['porteria_visitant'])
        
        self.vaos['grada'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['grada'])
        self.vaos['ball'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['ball'])
        self.vaos['stadium'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['stadium'])
        self.vaos['hc'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['hc'])

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)])
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()