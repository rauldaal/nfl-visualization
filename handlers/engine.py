import pygame as pg
import moderngl as mgl
import sys
import objects
import time
from .camera import Camera
from .light import Light
from .mesh import Mesh
from .scene import Scene
from .data_loader import DataLoader


class GraphicsEngine:
    def __init__(self, win_size=(1200, 780)):
        # init pygame modules
        pg.init()
        # window size
        self.WIN_SIZE = win_size
        # set opengl attr
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        # create opengl context
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        # mouse settings
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)
        # detect and use existing opengl context
        self.ctx = mgl.create_context()
        # self.ctx.front_face = 'cw'
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)
        # create an object to help track time
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0
        # light
        self.light = Light()
        # camera
        self.camera = Camera(self)
        # mesh
        self.mesh = Mesh(self)

        #data loader
        self.dataloader = DataLoader(
            players_df='data/players.csv',
            plays_df='data/plays.csv',
            week_df='data/allweeks.csv'
        )
        #self.dataloader.get_game(game_id=2021090900)
        #self.dataloader.get_play(play_id=2279)
        self.dataloader.load_example()
        self.dataloader.get_num_frames()
        self.frame = 1
        data = self.dataloader.get_frame_information(frames_id=self.frame)
        # scene
        self.scene = Scene(self, data)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                pg.quit()
                sys.exit()

    def update_frame_id(self):
        self.frame += 1
        if self.frame > self.dataloader.num_frames:
            self.frame = 1
        print("Numero de frames totales:", self.dataloader.num_frames)
        print("Numero de frame:", self.frame)

    def render(self):
        self.get_time()
        # clear framebuffer
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        # get new data
        data = self.dataloader.get_frame_information(frames_id=self.frame)
        # render scene
        self.scene.render(data)
        # swap buffers
        pg.display.flip()
        if (self.time - self.delta_time) > 0.1:
            self.delta_time = self.time
            self.update_frame_id()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.render()
            #self.delta_time = self.clock.tick(60)
