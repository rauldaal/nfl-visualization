import glm


class Camera:
    def __init__(self, app):
        self.app = app
        self.aspec_ratio = app.WIN_SIZE[0]/app.WIN_SIZE[1]
        self.position = glm.vec3(4, 3, 3)
        self.up = glm.vec3(0, 1, 0)
        # view_matrix
        self.m_view = self.get_view_matrix()
        # projection matrix
        self.m_proj = self.get_projection_matrix()

    def get_view_matrix(self):
        return glm.lookAt(self.position, glm.vec3(0), self.up)

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(45), self.aspec_ratio, 0.1, 100)
