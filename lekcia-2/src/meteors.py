import pygame
import random

from .game_element import GameElement

class Meteors:
    def __init__(self, init_cout, init_speed, inc_count, inc_speed, meteor_image_path, ship_size, game_res):
        self.meteors=[]
        self.count=init_cout
        self.speed=init_speed
        self.inc_count=inc_count
        self.inc_speed=inc_speed
        self.meteor_image_path=meteor_image_path 
        self.ship_size=ship_size
        self.game_res=game_res
        self.generate()

    def generate(self):
        meteor_image=pygame.image.load(self.meteor_image_path) 
        for _ in range(self.count):
            meteor_pos=(
                random.choice(range(0, self.game_res[0] - meteor_image.get_width(), self.ship_size[0] + 10)),
                random.choice(range(0, -self.game_res[1], -(self.ship_size[1] + 10)))
            )
            self.meteors.append(GameElement(meteor_pos, self.meteor_image_path))
    
    def move(self):
        score_counter=0
        for meteor in self.meteors[:]:
            meteor.move((0, self.speed))
            if meteor.pos[1] > self.game_res[1]:
                self.meteors.remove(meteor)
                score_counter += 1
        
        if len(self.meteors) ==0:
            self.count += self.inc_count
            self.inc_speed += self.inc_speed
            self.generate()
        
        return score_counter
    
    def draw(self, window):
        for meteor in self.meteors:
            meteor.draw(window)
    
    def check_colision(self, game_object):
        for meteor in self.meteors:
            x_off = meteor.pos[0] - game_object.pos[0]
            y_off = meteor.pos[1] - game_object.pos[1]
            if game_object.mask.overlap(meteor.mask, (x_off, y_off)):
                return True
        return False