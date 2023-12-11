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
import glm



class GraphicsEngine:
    def __init__(self, win_size=(1200, 780)):
        # pause the scene
        self.paused = False
        #camera dron
        self.dron = False
        # camera mister
        self.mister = False    
        # camera espectator
        self.espectator = False
        # camera backgrounds
        self.before = False
        # camera player
        self.player = False
        # camera change player
        self.jugador = 0
        # estadisticas
        self.estadisticas = False
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
        # scene
        self.scene = Scene(self)

        #data loader
        self.dataloader = DataLoader(
            players_df='data/players.csv',
            plays_df='data/plays.csv',
            week_df='data/allweeks.csv'
        )
        self.dataloader.load_example()
        self.dataloader.get_num_frames()
        self.frame = 1

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                pg.quit()
                sys.exit()
            
            elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                self.paused = not self.paused

            elif event.type == pg.KEYDOWN and event.key == pg.K_o:
                self.dron = not self.dron
                self.espectator = False
                self.mister = False
                self.player = False
            
            elif event.type == pg.KEYDOWN and event.key == pg.K_m:
                self.mister = not self.mister
                self.espectator = False
                self.dron = False
                self.player = False
            
            elif event.type == pg.KEYDOWN and event.key == pg.K_e:
                self.espectator = not self.espectator
                self.mister = False
                self.dron = False
                self.player = False
            
            elif event.type == pg.KEYDOWN and event.key == pg.K_p: # si aixo esta apretat que al clicar al enter puguis anar saltant de jugadors fins al que vulguis
                self.player = not self.player
                self.mister = False
                self.dron = False
                self.espectator = False
            
            elif event.type == pg.KEYDOWN and event.key == pg.K_c:
                if self.player:
                    self.jugador += 1
                    if self.jugador > 21:
                        self.jugador = 0
            
            elif event.type == pg.KEYDOWN and event.key == pg.K_h:
                self.estadisticas = not self.estadisticas                
            
            elif event.type == pg.KEYDOWN and event.key == pg.K_z:
                self.paused = not self.paused if self.paused == True else self.paused
                self.before = not self.before
            
            elif event.type == pg.KEYDOWN and event.key == pg.K_1:
                self.show_path = not self.show_path
    
    def update_frame_id(self):
        self.frame += 1
        if self.frame > self.dataloader.num_frames:
            self.frame = 1
    
    def update_before_frame_id(self):
        self.frame -= 1
        if self.frame < 1:
            self.frame = 1

    def render(self):
        self.get_time()
        # clear framebuffer
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        # get new data
        data = self.dataloader.get_frame_information(frames_id=self.frame)
        prev_data = None
        if self.show_path:
            prev_data=self.dataloader.get_prev_frame_information(frames_id=self.frame)
        # render scene
        jugadors = self.scene.render(data, prev_data)  #aqui agafo les dades
        if self.player:
            jugadors = jugadors[self.jugador]
            self.camera.position = glm.vec3(jugadors[0], jugadors[1], jugadors[2]) #aqui vaig actualitzant la info de la posicio de la camera
        # swap buffers
        pg.display.flip()
        if (self.time - self.delta_time) > 0.1 and not self.paused:
            self.delta_time = self.time
            if not self.before:
                self.update_frame_id()
            else:
                self.update_before_frame_id()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            # pg.display.set_caption('image')
            if self.dron:
                self.camera.position = glm.vec3(50,30,27.5)
                self.camera.yaw = 0
                self.camera.pitch = -35  
            if self.mister:
                self.camera.position = glm.vec3(30,3.5,0)
                self.camera.yaw = 13 
                self.camera.pitch =0  
            if self.espectator:
                self.camera.position = glm.vec3(80,18,70)
                self.camera.yaw = -82
                self.camera.pitch = -25  
            self.camera.update()
            self.render()


    
