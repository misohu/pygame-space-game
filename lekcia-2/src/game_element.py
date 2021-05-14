import pygame

class GameElement: 
    def __init__(self, pos, image_path, has_mask=True):
        self.pos=pos
        self.image=pygame.image.load(image_path)
        if has_mask:
            self.mask=pygame.mask.from_surface(self.image)
        else: 
            self.mask=None
    
    def draw(self, dest):
        dest.blit(self.image, self.pos)
    
    def move(self, offset):
        old_x, old_y=self.pos
        self.pos = (old_x + offset[0], old_y + offset[1])

    
