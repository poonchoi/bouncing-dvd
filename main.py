import pygame
import random

# pygame initialize
pygame.init()

dimensions = (height, width) = (1920, 1080)
screen = pygame.display.set_mode(dimensions)
clock = pygame.time.Clock()
fps = 90

screen.fill((0, 0, 0))


class logo:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.img = pygame.image.load("dvd.png")
        scale = 250 / self.img.get_width()
        self.img = pygame.transform.scale(
            self.img, (250, int(self.img.get_height() * scale))
        )

    def move(self):
        self.position = [
            (self.velocity[0] + self.position[0]),
            (self.velocity[1] + self.position[1]),
        ]

    def check_collision(self):
        xpos = self.position[0]
        ypos = self.position[1]
        xvel = self.velocity[0]
        yvel = self.velocity[1]
        imgx = self.img.get_width()
        imgy = self.img.get_height()

        if (xpos <= 0) or (xpos >= width - imgx):
            xvel *= -1
        if (ypos <= 0) or (ypos >= height - imgy):
            yvel *= -1

        self.velocity = [xvel, yvel]

    def draw(self):
        x = self.position[0]
        y = self.position[1]
        coords = (x, y)
        screen.blit(self.img, coords)


class box:
    def __init__(self, position, velocity, color):
        self.position = position
        self.velocity = velocity
        self.color = color

    def move(self):
        self.position = [
            (self.velocity[0] + self.position[0]),
            (self.velocity[1] + self.position[1]),
        ]

    def draw(self):
        x = self.position[0]
        y = self.position[1]
        pygame.draw.rect(
            screen, self.color, pygame.Rect(x, y, 250, int((250 / 1024) * 590))
        )

    def check_collision(self):
        xpos = self.position[0]
        ypos = self.position[1]
        xvel = self.velocity[0]
        yvel = self.velocity[1]
        boxwidth = 250
        boxheight = int((250 / 1024) * 590)

        if (xpos <= 0) or (xpos >= width - boxwidth):
            xvel *= -1
            self.color = (
                random.randint(50, 150),
                random.randint(50, 150),
                random.randint(50, 150),
            )
        if (ypos <= 0) or (ypos >= height - boxheight):
            yvel *= -1
            self.color = (
                random.randint(50, 150),
                random.randint(50, 150),
                random.randint(50, 150),
            )

        self.velocity = [xvel, yvel]


dvd_logo = logo([width / 2, height / 2], [2, -2])
box = box([width / 2, height / 2], [2, -2], (255, 100, 43))
run = True

while run:
    clock.tick(fps)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    screen.fill((0, 0, 0))

    dvd_logo.check_collision()
    dvd_logo.move()

    box.check_collision()
    box.move()

    box.draw()
    dvd_logo.draw()
    pygame.display.update()

pygame.quit()
