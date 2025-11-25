import pygame
import random


class Domino:

    colors = {
        'RED': (255, 0, 0),
        'GREEN': (0, 255, 0),
        'BLUE': (0, 0, 255)
    }
    generated = set()
    difficulty = (0, 0)
    def __init__(self, x=0, y=0):
        while True:
            self.width = 80
            self.height = 160
            self.top = self.generate_domino(self.difficulty)
            self.bottom = self.generate_domino(self.difficulty)
            pair = (tuple(self.top), tuple(self.bottom))
            if pair not in Domino.generated:
                Domino.generated.add(pair)
                break
        
        # position and drag state
        self.x = x
        self.y = y
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0
        self.in_working_area = False
        self.highlighted = False  # for highlighting valid next dominoes

    #check if a point is inside this domino
    def contains_point(self, px, py): 
        return (self.x <= px <= self.x +self.width and self.y <= py <= self.y+self.height)

    def generate_domino(self, difficulty):

        # first we choose how many squares we will have
        num_squares = random.randint(1 + difficulty[0], 3 + difficulty[1])
        # then we generate the colored squares
        return [random.choice(list(self.colors.keys())) for i in range(num_squares)]

    #start dragging the domino
    def start_drag(self, mouse_x, mouse_y):
        self.dragging = True
        self.offset_x = mouse_x - self.x
        self.offset_y = mouse_y - self.y

    #update domino position while dragging
    def update_drag(self, mouse_x, mouse_y):
        if self.dragging:
            self.x = mouse_x - self.offset_x
            self.y = mouse_y - self.offset_y

    #stop dragging 
    def stop_drag(self):
        self.dragging = False

    # def draw(self, surface, x, y):
        # square_size = 10
        # spacing = 5

        # # draws domino base
        # pygame.draw.rect(surface, (255, 255, 255), (x, y, self.width, self.height))

        # # top and bottom dividing line
        # pygame.draw.line(surface, (0, 0, 0), (x, y + self.height / 2), (x + self.width, y + self.height / 2), 3)

        # # draws colored squares
        # for half, squares in enumerate([self.top, self.bottom]):
        #     n = len(squares)
        #     if n == 0:
        #         continue

        #     y_offset = y + half * (self.height / 2) + (self.height / 4 - square_size / 2)

        #     total_width = n * square_size + (n - 1) * spacing
        #     start_x = x + (self.width - total_width) / 2

        #     for i, color in enumerate(squares):
        #         rect_x = start_x + i * (square_size + spacing)
        #         pygame.draw.rect(surface, self.colors[color], (rect_x, y_offset, square_size, square_size))
    
    def draw(self, surface, x=None, y=None):
        #draw domino at a specified position or its stored position
        draw_x = x if x is not None else self.x
        draw_y = y if y is not None else self.y

        square_size = 10
        spacing = 5
        
        #draw domino base w/ border (highlight if this is a valid next domino)
        if self.highlighted:
            # Draw glowing yellow border for highlighted dominoes
            pygame.draw.rect(surface, (255, 255, 0), (draw_x - 4, draw_y - 4, self.width + 8, self.height + 8))
            pygame.draw.rect(surface, (255, 255, 0), (draw_x - 2, draw_y - 2, self.width + 4, self.height + 4))
        
        pygame.draw.rect(surface, (255, 255, 255), (draw_x, draw_y, self.width, self.height))
        pygame.draw.rect(surface, (0, 0, 0), (draw_x, draw_y, self.width, self.height), 2)
        pygame.draw.line(surface, (0, 0, 0), (draw_x, draw_y + self.height / 2), (draw_x + self.width, draw_y + self.height / 2), 3)

        for half, squares in enumerate([self.top, self.bottom]):
            n = len(squares)
            if n == 0:
                continue
            y_offset = draw_y + half * (self.height / 2) + (self.height / 4 - square_size / 2)
            total_width = n * square_size + (n - 1) * spacing
            start_x = draw_x + (self.width - total_width) / 2
            
            for i, color in enumerate(squares):
                rect_x = start_x + i * (square_size + spacing)
                pygame.draw.rect(surface, self.colors[color], (rect_x, y_offset, square_size, square_size))