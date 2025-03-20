import pygame

# Инициализация Pygame
pygame.init()

# Установка размеров окна
width, height = 1600, 1600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Злой смайлик")

# Цвета
yellow = (255, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

# Заливка фона
screen.fill((255, 255, 255))

# Рисуем голову (желтый круг)
pygame.draw.circle(screen, yellow, (width // 2, height // 2), 150)

# Рисуем глаза (красные круги)
eye_radius = 20
eye_y = height // 2 - 50
left_eye_pos = (width // 2 - 70, eye_y)
right_eye_pos = (width // 2 + 70, eye_y)
pygame.draw.circle(screen, red, left_eye_pos, eye_radius)
pygame.draw.circle(screen, red, right_eye_pos, eye_radius)

# Рисуем зрачки (черные круги)
pupil_radius = 10
pygame.draw.circle(screen, black, left_eye_pos, pupil_radius)
pygame.draw.circle(screen, black, right_eye_pos, pupil_radius)

# Рисуем наклоненные брови
brow_height = 20  # Толщина бровей
brow_y = eye_y - 40

# Левая бровь (длиннее и толще)
left_brow_start = (width // 2 - 130, brow_y)  # Начинается дальше влево
left_brow_end = (width // 2 - 30, brow_y + 40)  # Заканчивается ниже
pygame.draw.line(screen, black, left_brow_start, left_brow_end, brow_height)

# Правая бровь (остается как было)
right_brow_start = (width // 2 + 40, brow_y + 30)
right_brow_end = (width // 2 + 100, brow_y)
pygame.draw.line(screen, black, right_brow_start, right_brow_end, brow_height)

# Рисуем прямоугольный рот
mouth_width = 120
mouth_height = 20
mouth_y = height // 2 + 80
pygame.draw.rect(screen, black, (width // 2 - mouth_width // 2, mouth_y, mouth_width, mouth_height))

# Обновление экрана
pygame.display.flip()

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Завершение работы Pygame
pygame.quit()