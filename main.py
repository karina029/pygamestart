from pygame import *
#створи вікно гри
win = display.set_mode((1100, 600))
display.set_caption("Run")
display.set_icon(image.load('sprite2.png'))
#задай фон сцени
background = transform.scale(image.load('background.png'), (1100, 600))

x1,y1= 100, 300
x2,y2 = 300, 300
x3, y3 = 500, 300
sprite1 = transform.scale(image.load('sprite1.png'), (100, 100))
sprite2 = transform.scale(image.load('sprite2.png'), (100, 100))
sprite3 = transform.scale(image.load('sprite3.png'), (100, 100))
speed = 10
#створи 2 спрайти та розмісти їх на сцені

#оброби подію «клік за кнопкою "Закрити вікно"»
run = True
clock = time.Clock()

while run:
    for e in event.get():
        if e.type == QUIT:
            print("Author: Karyna Sorokina")
            run = False
    win.blit(background, (0,0))
    win.blit(sprite1,(x1, y1))
    win.blit(sprite2, (x2, y2))
    win.blit(sprite3, (x3, y3))

    '''if sprite.spritecollide(sprite1, sprite2):
        print("Game over")'''

    keys_pressed = key.get_pressed()

    if keys_pressed[K_w] and y1 > 0:
        y1 -= speed
    if keys_pressed[K_s] and y1 < 500:
        y1 += speed
    if keys_pressed[K_a] and x1 > 0:
        x1 -= speed
    if keys_pressed[K_d] and x1 < 1000:
        x1 += speed

    if keys_pressed[K_UP] and y2 > 0:
        y2 -= speed
    if keys_pressed[K_DOWN] and y2 < 500:
        y2 += speed
    if keys_pressed[K_LEFT] and x2 > 0:
        x2 -= speed
    if keys_pressed[K_RIGHT] and x2 < 1000:
        x2 += speed

    if keys_pressed[K_t] and y3 > 0:
        y3 -= speed
    if keys_pressed[K_g] and y3 < 500:
        y3 += speed
    if keys_pressed[K_f] and x3 > 0:
        x3 -= speed
    if keys_pressed[K_h] and x3 < 1000:
        x3 += speed

    display.update()
    clock.tick(40)