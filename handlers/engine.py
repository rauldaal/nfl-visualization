import pygame as pg
import moderngl as mgl
import glm
import sys


class GraphicsEngine:
    def __init__(self, win_size=(900, 900)):

        pg.init()

        self.WIN_SIZE = win_size

        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)

        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)

        self.ctx = mgl.create_context()

    def _load_objects(self, objects):
        self.players = {}
        for object in objects:
            self.players[object.id] = object

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.scene.destroy()
                pg.quit()
                sys.exit()

    def render(self):
        # clear framebuffer
        self.ctx.clear(color=(0, 0, 0))
        # render scene
        self.scene.render()

        pg.display.flip()

    def run(self):
        while True:
            self.check_events()
            self.render()



