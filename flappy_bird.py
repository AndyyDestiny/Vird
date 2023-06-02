import pygame


class FlappyBird:

    def __init__(self, x, y):
        self.index = 0
        self.x = x
        self.y = y
        self.image_list = []
        for num in range(1, 4):
            image = pygame.image.load(f'bird{num}.png')
            self.image_list.append(image)
        self.image = self.image_list[self.index]
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0] * .46, self.image_size[1] * .46)
        scale_size = (self.image_size[0] * .46, self.image_size[1] * .46)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image = self.image_list[self.index]
        self.vel = 0
        self.clicked = False

    def update(self):
        self.vel += 0.5
        if self.vel > 8:
            self.vel = 8
        if self.rect.bottom < 553:
            self.rect.y += int(self.vel)
        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            self.clicked = True
            self.vel = -10
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

    def switch_image(self):
        self.image = self.image_list[self.index]
        self.image = pygame.transform.rotate(self.image_list[self.index], self.vel * -2)
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .46, self.image_size[1] * .46)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.index += 1
        if self.index > 2:
            self.index = 0

    def bird_dead(self):
        self.image = self.image_list[self.index]
        self.image = pygame.transform.rotate(self.image_list[self.index], -90)
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .47, self.image_size[1] * .47)
        self.image = pygame.transform.scale(self.image, scale_size)
