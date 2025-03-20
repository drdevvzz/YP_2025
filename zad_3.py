
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1920, 1080))
screen.fill((255, 255, 255))
white = (255, 255, 255)
black = (0, 0, 0)
orange_color = (255, 165, 0)  # Оранжевый
skin_color = (255, 224, 189)  # Телесный

def draw_person(x_offset, y_offset):


    circle_center = (1920 // 2 + x_offset, 1080 + 100 + y_offset)
    circle_radius = 350
    circle(screen, orange_color, circle_center, circle_radius)


    five_color = (255, 165, 0)
    five_points = [
        (1520 // 2 - 80 + x_offset, 1980 // 2 + 100 + y_offset),
        (1520 // 2 + 80 + x_offset, 1980 // 2 + 100 + y_offset),
        (1520 // 2 + 85 + x_offset, 1980 // 2 - 50 + y_offset),
        (1520 // 2 + x_offset, 1980 // 2 - 200 + y_offset),
        (1520 // 2 - 85 + x_offset, 1980 // 2 - 50 + y_offset),
    ]
    polygon(screen, five_color, five_points)
    polygon(screen, black, five_points, 3)

    # Рисуем второй 5к
    five_points = [
        (2320 // 2 - 80 + x_offset, 1980 // 2 + 100 + y_offset),
        (2320 // 2 + 80 + x_offset, 1980 // 2 + 100 + y_offset),
        (2320 // 2 + 85 + x_offset, 1980 // 2 - 50 + y_offset),
        (2320 // 2 + x_offset, 1980 // 2 - 200 + y_offset),
        (2320 // 2 - 85 + x_offset, 1980 // 2 - 50 + y_offset),
    ]
    polygon(screen, five_color, five_points)
    polygon(screen, black, five_points, 3)


    oval_color = skin_color
    oval_rect = pygame.Rect(0, 0, 550, 700)
    oval_rect.center = (1920 // 2 + x_offset, 1080 // 2 + y_offset)
    ellipse(screen, oval_color, oval_rect)


    eye_color = (150, 150, 255)  # Цвет глаза
    oval_rect = pygame.Rect(0, 0, 100, 100)  # Размеры овала
    oval_rect.center = (1700 // 2 + x_offset, 1000 // 2 + y_offset)
    ellipse(screen, eye_color, oval_rect)


    oval_color = (0, 0, 0)  # Цвет зрачка
    oval_rect = pygame.Rect(0, 0, 20, 20)  # Размеры овала
    oval_rect.center = (1700 // 2 + x_offset, 1000 // 2 + y_offset)
    ellipse(screen, oval_color, oval_rect)


    oval_color = eye_color  # Цвет глаза
    oval_rect = pygame.Rect(0, 0, 100, 100)  # Размеры овала
    oval_rect.center = (2100 // 2 + x_offset, 1000 // 2 + y_offset)
    ellipse(screen, oval_color, oval_rect)


    oval_color = (0, 0, 0)  # Цвет зрачка
    oval_rect = pygame.Rect(0, 0, 20, 20)  # Размеры овала
    oval_rect.center = (2100 // 2 + x_offset, 1000 // 2 + y_offset)
    ellipse(screen, oval_color, oval_rect)


    nose_color = (101, 67, 33)
    nose_points = [
        (1920 // 2 - 30 + x_offset, 1080 // 2 + 50 + y_offset),
        (1920 // 2 + 30 + x_offset, 1080 // 2 + 50 + y_offset),
        (1920 // 2 + x_offset, 1350 // 2 - 50 + y_offset),
    ]
    polygon(screen, nose_color, nose_points)

    # Рисуем рот
    mouth_color = (255, 0, 0)
    mouth_points = [
        (2220 // 2 - 30 + x_offset, 1380 // 2 + 50 + y_offset),  # Левая нижняя вершина
        (1620 // 2 + 30 + x_offset, 1380 // 2 + 50 + y_offset),  # Правая нижняя вершина
        (1920 // 2 + x_offset, 1750 // 2 - 50 + y_offset),  # Верхняя вершина
    ]
    polygon(screen, mouth_color, mouth_points)


    arm_color = skin_color
    # Левая рука
    rect(screen, arm_color, (1920 // 2 - 300 + x_offset, 1080 // 2 + 200 + y_offset, 50, 200))  # Прямоугольник для руки
    # Правая рука
    rect(screen, arm_color, (1920 // 2 + 250 + x_offset, 1080 // 2 + 200 + y_offset, 50, 200))  # Прямоугольник для руки


    hair_color = (0, 0, 0)

    # Первый треугольник (левый)
    hair_points = [
        (1920 // 2 - 150 + x_offset, 1080 // 2 - 350 + y_offset),  # Верхняя вершина
        (1920 // 2 - 250 + x_offset, 1080 // 2 - 200 + y_offset),  # Левая вершина
        (1920 // 2 - 50 + x_offset, 1080 // 2 - 200 + y_offset),  # Правая вершина
    ]
    polygon(screen, hair_color, hair_points)


    hair_points = [
        (1920 // 2 + 150 + x_offset, 1080 // 2 - 350 + y_offset),  # Верхняя вершина
        (1920 // 2 + 50 + x_offset, 1080 // 2 - 200 + y_offset),  # Левая вершина
        (1920 // 2 + 250 + x_offset, 1080 // 2 - 200 + y_offset),  # Правая вершина
    ]
    polygon(screen, hair_color, hair_points)


    hair_points = [
        (1920 // 2 + x_offset, 1080 // 2 - 400 + y_offset),
        (1920 // 2 - 100 + x_offset, 1080 // 2 - 250 + y_offset),
        (1920 // 2 + 100 + x_offset, 1080 // 2 - 250 + y_offset),
    ]
    polygon(screen, hair_color, hair_points)


# прямоугольник
x1 = 0;
y1 = 0
x2 = 1920;
y2 = 150
N = 10
color = (0, 255, 0)
rect(screen, color, (x1, y1, x2 - x1, y2 - y1), 150)
rect(screen, black, (x1, y1, x2 - x1, y2 - y1), 3)  #obvodka

h = (x2 - x1) // (N + 1)
x = x1 + h

font = pygame.font.Font(None, 100)
text = font.render("MOZHNO DOMOI PLZ", True, black)

text_rect = text.get_rect(center=((x2 - x1) // 2, y2 // 2))
screen.blit(text, text_rect)


draw_person(700, 0)


draw_person(-700, 0)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()