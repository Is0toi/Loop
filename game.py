import sys
import pygame

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('cataclysm')
        self.window = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock() 
        #self.img = pygame.image.load()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_UP:
                        self.movement[0] = True
                    if event.type == pygame.K_DOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.type == pygame.K_UP:
                        self.movement[0] = False
                    if event.type == pygame.K_DOWN:
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(60)

Game().run()




