import game_framework
import Cactus_Family
import score_state
from pico2d import *

name = "TitleState"
image = None
menu_image = None
arrow = None
arrow_position = 300
menu_num = 1
bgm = None
select_sound = None
choose_sound = None


def choose_menu():
    if menu_num == 1:
        game_framework.change_state(Cactus_Family)
    elif menu_num == 2:
        game_framework.push_state(score_state)
    elif menu_num == 3:
        game_framework.quit()


def move_arrow(y_pos):
    global arrow_position, menu_num
    if y_pos == 0 and menu_num > 1:
        arrow_position += 100
        menu_num -= 1
    elif y_pos == 1 and menu_num < 3:
        arrow_position -= 100
        menu_num += 1


def enter():
    global image, menu_image, arrow, select_sound, choose_sound, bgm
    image = load_image('image_file\\title.png')
    menu_image = load_image('image_file\\menu.png')
    arrow = load_image('image_file\\arrow.png')
    select_sound = load_wav('sound_effect\\select.wav')
    select_sound.set_volume(100)
    choose_sound = load_wav('sound_effect\\choose.wav')
    choose_sound.set_volume(100)
    bgm = load_music('sound_effect\\Start_Menu.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()


def exit():
    global image, menu_image, arrow, bgm
    bgm.set_volume(0)
    del image, menu_image, arrow


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key in (SDLK_UP, SDLK_w):
                move_arrow(0)
                select_sound.play()
            elif event.key in (SDLK_DOWN, SDLK_s):
                move_arrow(1)
                select_sound.play()
            elif event.key in (SDLK_RETURN, SDLK_SPACE):
                choose_menu()
                choose_sound.play()
        elif event.type == SDL_QUIT:
            game_framework.quit()


def draw():
    clear_canvas()
    image.draw(450, 400)
    menu_image.draw(450, 200)
    arrow.draw(235, arrow_position)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass
