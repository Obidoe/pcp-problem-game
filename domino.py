import pygame
import random


class Domino:

    colors = {
        'RED': (255, 0, 0),
        'GREEN': (0, 255, 0),
        'BLUE': (0, 0, 255)
    }
    generated = set()

    def __init__(self):
        while True:
            self.width = 80
            self.height = 160
            self.top = self.generate_domino()
            self.bottom = self.generate_domino()
            pair = (tuple(self.top), tuple(self.bottom))
            if pair not in Domino.generated:
                Domino.generated.add(pair)
                break

    def generate_domino(self):

        # first we choose how many squares we will have
        num_squares = random.randint(1, 3)
        # then we generate the colored squares
        return [random.choice(list(self.colors.keys())) for i in range(num_squares)]

    def draw(self, surface, x, y):
        square_size = 10
        spacing = 5

        # draws domino base
        pygame.draw.rect(surface, (255, 255, 255), (x, y, self.width, self.height))

        # top and bottom dividing line
        pygame.draw.line(surface, (0, 0, 0), (x, y + self.height / 2), (x + self.width, y + self.height / 2), 3)

        # draws colored squares
        for half, squares in enumerate([self.top, self.bottom]):
            n = len(squares)
            if n == 0:
                continue

            y_offset = y + half * (self.height / 2) + (self.height / 4 - square_size / 2)

            total_width = n * square_size + (n - 1) * spacing
            start_x = x + (self.width - total_width) / 2

            for i, color in enumerate(squares):
                rect_x = start_x + i * (square_size + spacing)
                pygame.draw.rect(surface, self.colors[color], (rect_x, y_offset, square_size, square_size))
            

