import sys
import pygame

class Game:
    def __init__(self):

        #window and main game loop setup
        pygame.init()
        pygame.display.set_caption('cataclysm')
        self.window = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()

        #load and set up the character
        self.img = pygame.image.load('./data/assets/finalwalk.gif')
        self.img = pygame.transform.scale(self.img, (100, 100))
        self.img_pos = [160, 260] 
        self.movement = [False, False, False, False]  #[up, down, left, right]

    def run(self):
        while True:

            #movement controls
            if self.movement[0]:  #up
                self.img_pos[1] -= 2
            if self.movement[1]:  #down
                self.img_pos[1] += 2
            if self.movement[2]:  #left
                self.img_pos[0] -= 2
            if self.movement[3]:  #right
                self.img_pos[0] += 2

            self.window.fill((0, 0, 0))
            self.window.blit(self.img, self.img_pos)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.movement[0] = True
                    if event.key == pygame.K_s:
                        self.movement[1] = True
                    if event.key == pygame.K_a:
                        self.movement[2] = True
                    if event.key == pygame.K_d:
                        self.movement[3] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.movement[0] = False
                    if event.key == pygame.K_s:
                        self.movement[1] = False
                    if event.key == pygame.K_a:
                        self.movement[2] = False
                    if event.key == pygame.K_d:
                        self.movement[3] = False

            pygame.display.update()
            self.clock.tick(60)

Game().run()