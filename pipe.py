import pygame


class Pipe:

    def __init__(self, x, y, position):
        self.x = x
        self.y = y
        self.image = pygame.image.load("pipe.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0] * 0.7, self.image_size[1] * 0.5)
        scale_size = (self.image_size[0] * 0.7, self.image_size[1] * 0.5)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.delta = 3.5
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(150 / 2)]
        if position == -1:
            self.rect.topleft = [x, y + int(150 / 2)]

    def move_pipe(self):
        self.x = self.x - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
