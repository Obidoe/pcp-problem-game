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

        # set initial positions for dominoes in the set area
        for i, d in enumerate(self.dominos):
            d.x = 50 + i * 120
            d.y = 100
        
        # working area dominoes
        self.working_area_dominos = []
        # drag state
        self.dragged_domino = None
        # define areas
        self.working_area_y = 400
        self.working_area_height = 200
        
        self.running = True

    def is_in_working_area(self, y):
        # check if y cord is in working area
        return self.working_area_y <= y <= self.working_area_y + self.working_area_height

    def handle_mouse_down(self, pos):
        # check if clicking on a domino in the set 
        for d in self.dominos:
            if d.contains_point(pos[0], pos[1]):
                # create a copy of the domino for dragging
                new_domino = Domino()
                new_domino.top = d.top.copy()
                new_domino.bottom = d.bottom.copy()
                new_domino.x = d.x
                new_domino.y = d.y
                new_domino.start_drag(pos[0], pos[1])
                self.dragged_domino = new_domino
                return
        
        # check if clicking on a domino in the working area
        for d in self.working_area_dominos:
            if d.contains_point(pos[0], pos[1]):
                d.start_drag(pos[0], pos[1])
                self.dragged_domino = d
                return

    def handle_mouse_up(self, pos):
        if self.dragged_domino:
            # check if domino was dropped in working area
            if self.is_in_working_area(self.dragged_domino.y):
                if self.dragged_domino not in self.working_area_dominos:
                    self.working_area_dominos.append(self.dragged_domino)
                self.dragged_domino.in_working_area = True
            else:
                # if not in working area and was from working area, remove it
                if self.dragged_domino in self.working_area_dominos:
                    self.working_area_dominos.remove(self.dragged_domino)
            
            self.dragged_domino.stop_drag()
            self.dragged_domino = None

    def handle_mouse_motion(self, pos):
        if self.dragged_domino:
            self.dragged_domino.update_drag(pos[0], pos[1])

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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_down(event.pos)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.handle_mouse_up(event.pos)
                elif event.type == pygame.MOUSEMOTION:
                    self.handle_mouse_motion(event.pos)
            
            self.screen.fill((0, 135, 0))

            #draw working area background
            pygame.draw.rect(self.screen, (50, 100, 50), (0, self.working_area_y, self.screen_width, self.working_area_height))

            # label for set area
            font = pygame.font.Font(None, 36)
            text = font.render("Domino Set (Click and Drag)", True, (255, 255, 255))
            self.screen.blit(text, (20, 20))
            
            # label for working area
            text = font.render("Working Area (Drop Here)", True, (255, 255, 255))
            self.screen.blit(text, (20, self.working_area_y - 40))
            
            for d in self.dominos:
                d.draw(self.screen)
            
            # draw dominoes in working area
            for d in self.working_area_dominos:
                if d != self.dragged_domino:  # don't draw if currently being dragged
                    d.draw(self.screen)
            
            # draw dragged domino on top
            if self.dragged_domino:
                self.dragged_domino.draw(self.screen)

            # Draw dominos
            # for i, d in enumerate(self.dominos):
            #     d.draw(self.screen, 50 + i * 120, 100)
                
            pygame.display.flip()
            
        pygame.quit()
