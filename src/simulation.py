import sys
import pygame as pg

import config
from world import World

class Simulation:
    STARTING_FPS_LIMIT: int = 60
    
    def __init__(self, height: int, width: int, tile_size : int):
        pg.display.init()
        pg.font.init()
        pg.display.set_caption("Evolution Simulation")
        self.screen = pg.display.set_mode((width, height), pg.HWSURFACE | pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        self.height = height
        self.width = width
        self.tile_size = tile_size
        self.world = World(height, width, tile_size)
        
        self.fps_max_limit: int = self.STARTING_FPS_LIMIT
        self.increase_game_speed = False
        self.decrease_game_speed = False

    def simulate(self):
        """
        The main loop of the simulation. Updates the state of the animals and plants, handles their interactions,
        and manages the spawning of new animals and plants.
        """
        running = True
        is_paused = False
        
        while running:
            event = pg.event.poll()
            
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()
            
            #TODO enable spawning of animals and plants via mouse
            #TODO enable stat displaying of animals and plants by klicking on them via mouse
            #TODO implement settings panel
            #TODO implement menu panel
            
            if event.type == pg.KEYDOWN:
                print("Key Pressed", event.key)
                if event.key == pg.K_SPACE:
                    is_paused  = not is_paused
                elif event.key == pg.K_RETURN:
                    chance_to_spawn_animals = .001
                    self.world.spawn_animals(chance_to_spawn = chance_to_spawn_animals) 
                elif event.key == pg.K_1 and pg.key.get_mods() & pg.KMOD_ALT: 
                    config.draw_height_level = not config.draw_height_level
                    self.world.draw() 
                    pg.display.flip()
                elif event.key == pg.K_2 and pg.key.get_mods() & pg.KMOD_ALT: 
                    config.draw_animal_health = not config.draw_animal_health
                    print("Drawing animal health.")
                    self.world.draw() 
                    pg.display.flip()
                elif event.key == pg.K_3 and pg.key.get_mods() & pg.KMOD_ALT: 
                    config.draw_animal_energy = not config.draw_animal_energy
                    print("Drawing animal energy.")
                    self.world.draw() 
                    pg.display.flip()
                elif event.key == pg.K_UP and pg.key.get_mods() & pg.KMOD_SHIFT:
                    self.increase_game_speed = True
                    self.decrease_game_speed = False
                elif event.key == pg.K_DOWN and pg.key.get_mods() & pg.KMOD_SHIFT:
                    self.increase_game_speed = False
                    self.decrease_game_speed = True
                elif event.key == pg.K_r and pg.key.get_mods() & pg.KMOD_SHIFT:
                    self.world = World(self.height, self.width, self.tile_size)
                    self.world.draw() 
                    pg.display.flip() 
            
            if event.type == pg.KEYUP:
                if event.key == pg.K_UP and pg.key.get_mods() & pg.KMOD_SHIFT:
                    self.increase_game_speed = False
                elif event.key == pg.K_DOWN and pg.key.get_mods() & pg.KMOD_SHIFT:
                    self.decrease_game_speed = False
            
            if not is_paused:
                self.screen.fill((pg.Color("white")))  # Fill the screen with a white background
                self.world.update()
                self.world.draw() 
                self.stat_panel()
                pg.display.flip() 
                
            self.handle_game_speed()
            self.clock.tick(self.fps_max_limit)
            
    def handle_game_speed(self):   
        GAME_SPEED_CHANGE: int = 1
        MAX_FPS_LIMIT: int = 120
        
        if self.increase_game_speed and self.fps_max_limit + GAME_SPEED_CHANGE <= MAX_FPS_LIMIT:
            self.fps_max_limit += GAME_SPEED_CHANGE
        elif self.decrease_game_speed and self.fps_max_limit > GAME_SPEED_CHANGE:
            self.fps_max_limit -= GAME_SPEED_CHANGE
            
    def stat_panel(self):
        font_size = int(0.02 * self.height)
        panel_height = int(0.03 * self.height) 
        line_width: int = 2
        panel_color: pg.Color = pg.Color("grey")
        line_color: pg.Color = pg.Color("black")
        
        # Drawing base panel
        pg.draw.rect(self.screen, panel_color, pg.Rect(0, 0, self.width, panel_height))
        pg.draw.line(self.screen, line_color, (0, panel_height), (self.width, panel_height), width=line_width)
        
        stats_texts = self.generate_stat_text(font_size)
        
        # Drawing stat text
        text_height = (panel_height-(font_size/2))/2
        padding = 10
        x_offset = padding
        x_div = (padding * .5)
        for text in stats_texts:
            self.screen.blit(text, (x_offset, text_height))
            x_offset += text.get_width() + padding
            x_div += text.get_width() + padding
            # Drawing divider line
            pg.draw.line(self.screen, line_color, (x_div, 0), (x_div, panel_height), width=line_width)
            
    def generate_stat_text(self, font_size: int) -> list[pg.Surface]:
        stats_font = pg.font.Font(None, font_size)
        stat_color: pg.Color = pg.Color("black")
        
        stats_texts: list[pg.Surface] = []
        
        stats = [("FPS", round(self.clock.get_fps())), ("FPS Max Setting", round(self.fps_max_limit))]
        for label, value in stats:
            stats_texts.append(stats_font.render(f"{label}: {value}", True, stat_color))
        
        return stats_texts