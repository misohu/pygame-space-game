import pygame
import random
import sys

def generate_meteor(meteor_image):
    return {
        "mask": pygame.mask.from_surface(meteor_image),
        "x": random.choice(range(10, 440, 50)),
        "y": random.choice(range(-10, -500, -50))
    }

def check_colision(mask1, mask2, mask1_coords, mask2_coords):
    x_off = mask2_coords[0] - mask1_coords[0]
    y_off = mask2_coords[1] - mask1_coords[1]
    if mask1.overlap(mask2, (x_off, y_off)):
        return True
    else: 
        return False

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()

    bg = pygame.image.load("assets/background.jpg")
    ship = pygame.image.load("assets/ship.png") 
    meteor_img = pygame.image.load("assets/Meteor1.png")
    game_font = pygame.font.SysFont("comicsans", 50)

    ship_mask = pygame.mask.from_surface(ship)

    window = pygame.display.set_mode((500, 800))
    
    ship_coordinates_x=250
    ship_coordinates_y=720

    score=0
    meteors=[]
    meteor_speed=0
    meteor_increment=4
    meteor_count=0
    end = False

    while True:
        score_text = game_font.render(f"Score {score}", True, (255, 255, 255))

        if len(meteors) == 0: 
            meteor_speed += 1
            meteor_count += meteor_increment
            for i in range(meteor_count):
                meteors.append(generate_meteor(meteor_img))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if ship_coordinates_x > 10:
                ship_coordinates_x -= 5
        if keys[pygame.K_RIGHT]:
            if ship_coordinates_x < 440:
                ship_coordinates_x += 5  

        window.blit(bg, (0, 0))
        window.blit(ship, (ship_coordinates_x, ship_coordinates_y))

        if not end:
            for meteor in meteors[:]:
                window.blit(meteor_img, (meteor['x'], meteor['y']))
                meteor["y"] += meteor_speed
                if meteor["y"] > 800:
                    score += 1
                    meteors.remove(meteor)
                if check_colision(ship_mask, meteor['mask'], (ship_coordinates_x, ship_coordinates_y), (meteor['x'], meteor['y'])):
                    end=True
        
        if end:
            end_text = game_font.render(f"GAME OVER", True, (255, 255, 255))
            window.blit(end_text, (200, 400))

        window.blit(score_text, (350, 10))

        pygame.display.update()
        clock.tick(60)