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
import pandas as pd



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
        self.show_path = False
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
        self.camera.position = glm.vec3(100000000,100000000,100000000)
        # mesh
        self.mesh = Mesh(self)

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
        # show path
        self.show_path = False
        # show menu
        self.show_menu = True
        # scene
        self.scene = Scene(self)
        # num_play
        # 0 --> id 39974
        # 9 --> id 2441
        # 8 --> id 3014
        # 7 --> id 1319
        # 6 --> id 1319
        self.play = 0 

        #data loader
        self.dataloader = DataLoader(
            players_df='data/players.csv',
            plays_df='data/plays.csv',
            week_df='data/allweeks.csv'
        )

        self.dataloader.load_example()
        self.dataloader.get_num_frames()
        self.frame = 1

        self.prev_data = None
        
        self.voronoi = False

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                pg.quit()
                sys.exit()
            
            elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE and not self.show_menu:
                self.paused = not self.paused

            elif event.type == pg.KEYDOWN and event.key == pg.K_o and not self.show_menu:
                self.dron = not self.dron
                self.espectator = False
                self.mister = False
                self.player = False
            
            elif event.type == pg.KEYDOWN and event.key == pg.K_m and not self.show_menu:
                self.mister = not self.mister
                self.espectator = False
                self.dron = False
                self.player = False
            
            elif event.type == pg.KEYDOWN and event.key == pg.K_e and not self.show_menu:
                self.espectator = not self.espectator
                self.mister = False
                self.dron = False
                self.player = False
            
            elif event.type == pg.KEYDOWN and event.key == pg.K_p and not self.show_menu: # si aixo esta apretat que al clicar al enter puguis anar saltant de jugadors fins al que vulguis
                self.player = not self.player
                self.mister = False
                self.dron = False
                self.espectator = False
            
            elif event.type == pg.KEYDOWN and event.key == pg.K_c and not self.show_menu:
                if self.player:
                    self.jugador += 1
                    if self.jugador > 21:
                        self.jugador = 0            
            elif event.type == pg.KEYDOWN and event.key == pg.K_h and not self.show_menu:
                self.estadisticas = not self.estadisticas                
            
            elif event.type == pg.KEYDOWN and event.key == pg.K_z and not self.show_menu:
                self.paused = not self.paused if self.paused == True else self.paused
                self.before = not self.before
            
            elif event.type == pg.KEYDOWN and event.key == pg.K_1 and not self.show_menu:
                self.show_path = not self.show_path

            elif event.type == pg.KEYDOWN and event.key == pg.K_0:
                self.show_menu = not self.show_menu
                if self.show_menu:
                    self.camera.position = glm.vec3(100000000,100000000,100000000)
                    self.dron = False
                    self.mister = False
                    self.dron = False
                    self.espectator = False
                    self.player = False
                else:
                    self.dron = True
            elif event.type == pg.KEYDOWN and event.key == pg.K_9 and self.show_menu:
                self.dataloader.load_example(2441)
                self.dataloader.get_num_frames()
                self.frame = 1
                self.show_menu = False
                self.dron = True
                self.play = 9
            elif event.type == pg.KEYDOWN and event.key == pg.K_8 and self.show_menu:
                self.dataloader.load_example(3014)
                self.dataloader.get_num_frames()
                self.frame = 1
                self.show_menu = False
                self.dron = True
                self.play = 8
            elif event.type == pg.KEYDOWN and event.key == pg.K_7 and self.show_menu:
                self.dataloader.load_example(1319)
                self.dataloader.get_num_frames()
                self.frame = 1
                self.show_menu = False
                self.dron = True
                self.play = 7
            elif event.type == pg.KEYDOWN and event.key == pg.K_6 and self.show_menu:
                self.dataloader.load_example(97)
                self.dataloader.get_num_frames()
                self.frame = 1
                self.show_menu = False
                self.dron = True
                self.play = 6
            elif event.type == pg.KEYDOWN and event.key == pg.K_5 and self.show_menu:
                self.dataloader.load_example()
                self.dataloader.get_num_frames()
                self.frame = 1
                self.show_menu = False
                self.dron = True
                self.play = 0

 
            elif event.type == pg.KEYDOWN and event.key == pg.K_v:
                self.paused = not self.paused
                self.voronoi = not self.voronoi
                
    
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

        if self.show_path:
            if self.frame == 1:
                self.prev_data = None
            if self.prev_data is None:
                self.prev_data = data.copy()
            else:
                self.prev_data = pd.concat([self.prev_data, data])


        # render scene
        jugadors = self.scene.render(data, self.prev_data, voronoi=self.voronoi) #aqui agafo les dades
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
    
    def get_camera(self,x,y,z,yaw,pitch):
        self.camera.position = glm.vec3(x,y,z)
        self.camera.yaw = yaw
        self.camera.pitch = pitch

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            # pg.display.set_caption('image')
            if self.dron:
                if self.play == 0:
                    self.get_camera(50,30,27.5,0,-35)  
                else:
                    self.get_camera(95,30,27.5,180,-35)

            if self.mister:
                if self.play == 0:
                    self.get_camera(30,3.5,0,13,0)
                elif self.play == 9 or self.play==7:
                    self.get_camera(30,3.5,0,45,0)
                elif self.play == 8:
                    self.get_camera(30,3.5,0,90,0)
                else:
                    self.get_camera(30,3.5,0,52,0)

            if self.espectator:
                if self.play == 0:
                    self.get_camera(80,35,70,-75,-45)
                else:
                    self.get_camera(80,35,70,-125,-38)

            self.camera.update()
            self.render()


    
