from domino import Domino
import pygame


class Game:

    def __init__(self):
        # pygame setup
        pygame.init()
        self.clock = pygame.time.Clock()

        self.delta_time = 0.1
        self.screen_width = 1280
        self.screen_height = 720
        self.fps = 60

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("PCP Problem Game")
        
        # Domino Generation
        self.domino_index = 0
        self.dominos = [Domino() for i in range(10)]
        
        self.running = True
    
    def run(self):
        print('Starting game...')

        # Domino Debug
        for d in self.dominos:
            print(f'Domino {self.domino_index}:')
            print(f'Top: {d.top}')
            print(f'Bottom: {d.bottom}\n')
            self.domino_index += 1
        
        while self.running:
            
            # frame rate timing
            self.delta_time = self.clock.tick(self.fps) / 1000
            self.delta_time = max(0.001, min(0.1, self.delta_time))
            
            # EVENT HANDLER
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.screen.fill((0, 135, 0))
            
            # Draw dominos
            for i, d in enumerate(self.dominos):
                d.draw(self.screen, 50 + i * 120, 100)
                
            pygame.display.flip()
            
        pygame.quit()
